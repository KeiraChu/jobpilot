import logging
import time
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, File, Form, Header, HTTPException, UploadFile
from prometheus_client import Counter, Histogram, make_asgi_app

from app.config import Settings, get_settings
from app.evaluation import evaluate
from app.parsing import extract_file_text, heuristic_profile
from app.provider import ModelProvider
from app.position_store import PositionIndex
from app.recommender import recommend_positions
from app.schemas import (CareerPlan, CareerPlanRequest, EvaluationCase, EvaluationResult,
                         ParseRequest, RecommendRequest, RecommendResponse, ResumeProfile, PlanStep)

provider: ModelProvider | None = None
position_index: PositionIndex | None = None
logger = logging.getLogger(__name__)
REQUESTS = Counter("jobpilot_ai_requests_total", "AI requests", ["endpoint", "status"])
LATENCY = Histogram("jobpilot_ai_latency_seconds", "AI latency", ["endpoint"])


@asynccontextmanager
async def lifespan(_: FastAPI):
    global provider, position_index
    settings = get_settings()
    if settings.api_key:
        provider = ModelProvider(settings)
        if settings.use_position_index:
            try:
                position_index = PositionIndex(settings.database_url)
                await position_index.connect()
            except Exception:
                logger.exception("position index unavailable; recommendations will use request-local fallback")
                position_index = None
    yield
    if provider:
        await provider.close()
        provider = None
    if position_index:
        await position_index.close()
        position_index = None


app = FastAPI(title="JobPilot AI Service", version="1.0.0", lifespan=lifespan)
app.mount("/metrics", make_asgi_app())


def authorize(x_internal_api_key: str = Header(default=""), settings: Settings = Depends(get_settings)):
    if settings.environment != "development" and x_internal_api_key != settings.internal_api_key:
        raise HTTPException(401, "invalid internal API key")


@app.get("/health")
async def health():
    return {"status": "ok", "model_enabled": bool(get_settings().api_key), "position_index_ready": position_index is not None}


@app.post("/v1/resumes/parse", response_model=ResumeProfile, dependencies=[Depends(authorize)])
async def parse_resume(request: ParseRequest):
    # 确定性解析保证无模型密钥也可演示；大模型增强可在此结果上做严格 Schema 补全。
    return heuristic_profile(request.text, request.target_role)


@app.post("/v1/resumes/files", response_model=ResumeProfile, dependencies=[Depends(authorize)])
async def parse_resume_file(file: UploadFile = File(...), target_role: str = Form(default="")):
    content = await file.read()
    if len(content) > 20 * 1024 * 1024:
        raise HTTPException(413, "文件不能超过 20MB")
    try:
        text = extract_file_text(file.filename or "resume.txt", content)
    except ValueError as exc:
        raise HTTPException(415, str(exc)) from exc
    if len(text.strip()) < 10:
        raise HTTPException(422, "未提取到有效简历文本；扫描版 PDF 请先进行 OCR")
    return heuristic_profile(text, target_role)


@app.post("/v1/matches/recommend", response_model=RecommendResponse, dependencies=[Depends(authorize)])
async def recommend(request: RecommendRequest):
    started = time.perf_counter()
    outcome = await recommend_positions(request, provider, get_settings().rerank_candidates, position_index)
    LATENCY.labels("recommend").observe(time.perf_counter() - started)
    REQUESTS.labels("recommend", "success").inc()
    warnings = list(outcome.warnings)
    if not request.profile.skills:
        warnings.append("简历未识别到技能，推荐结果主要基于文本语义，请先确认解析结果。")
    return RecommendResponse(
        algorithm_version=outcome.algorithm_version,
        ranking_mode=outcome.ranking_mode,
        results=outcome.results,
        warnings=warnings,
    )


@app.post("/v1/workflows/career-plan", response_model=CareerPlan, dependencies=[Depends(authorize)])
async def career_plan(request: CareerPlanRequest):
    missing = request.match.missing_skills[:6]
    suggestions = [f"在已有项目中补充能证明“{skill}”的具体任务与结果；若没有相关经历，不要添加。" for skill in missing]
    questions = [f"请结合真实项目说明你如何使用或理解 {skill}。" for skill in (request.match.matched_skills + missing)[:8]]
    plan = [PlanStep(
        week=i + 1,
        goal=f"掌握并验证 {skill}",
        actions=[f"完成 {skill} 的最小实践", "编写测试或评测记录", "将真实成果整理为 STAR 项目表述"],
        evidence="可运行代码、测试结果或技术笔记",
    ) for i, skill in enumerate(missing[: min(8, max(1, request.horizon_days // 7))])]
    return CareerPlan(
        target_role=request.match.position.title,
        resume_suggestions=suggestions or ["保持现有事实，补充项目背景、个人动作和可验证结果。"],
        interview_questions=questions or ["介绍一个最能体现你解决问题能力的项目，并说明你的个人贡献。"],
        learning_plan=plan,
    )


@app.post("/v1/evaluations/recommendation", response_model=EvaluationResult, dependencies=[Depends(authorize)])
async def evaluate_recommendation(case: EvaluationCase):
    return evaluate(case)
