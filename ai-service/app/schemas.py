from typing import Literal

from pydantic import BaseModel, Field


class Experience(BaseModel):
    title: str = ""
    organization: str = ""
    period: str = ""
    description: str = ""


class SourceEvidence(BaseModel):
    field: str
    value: str
    quote: str
    start: int = Field(ge=0)
    end: int = Field(ge=0)


class ResumeProfile(BaseModel):
    target_role: str = ""
    city_preferences: list[str] = Field(default_factory=list)
    education: list[Experience] = Field(default_factory=list)
    projects: list[Experience] = Field(default_factory=list)
    work_experience: list[Experience] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    summary: str = ""
    confidence: float = Field(default=0.6, ge=0, le=1)
    evidence: list[SourceEvidence] = Field(default_factory=list)
    parsing_mode: Literal["HEURISTIC", "LLM_STRUCTURED"] = "HEURISTIC"
    warnings: list[str] = Field(default_factory=list)
    stage_latency_ms: dict[str, float] = Field(default_factory=dict)
    model_usage: dict[str, float | int | str] = Field(default_factory=dict)
    telemetry_id: str = ""


class ParseRequest(BaseModel):
    text: str = Field(min_length=10, max_length=100_000)
    target_role: str = ""


class PositionInput(BaseModel):
    position_id: int
    company: str
    title: str
    salary: str = ""
    education: str = ""
    description: str = ""
    address: str = ""


class RecommendRequest(BaseModel):
    user_id: str
    profile: ResumeProfile
    positions: list[PositionInput] = Field(min_length=1, max_length=5000)
    top_k: int = Field(default=10, ge=1, le=50)


class ScoreBreakdown(BaseModel):
    semantic: float
    skill_coverage: float
    preference: float
    hard_constraints: float


class SkillGapAction(BaseModel):
    skill: str
    estimated_score_gain: float
    evidence_requirement: str


class MatchResult(BaseModel):
    position: PositionInput
    score: float
    breakdown: ScoreBreakdown
    matched_skills: list[str]
    missing_skills: list[str]
    evidence: list[str]
    reasons: list[str]
    risks: list[str]
    improvement_actions: list[SkillGapAction] = Field(default_factory=list)
    decision_trace: list[str] = Field(default_factory=list)


class RecommendResponse(BaseModel):
    algorithm_version: str = "hybrid-embedding-llm-rerank-v1"
    ranking_mode: Literal["BASELINE", "EMBEDDING", "LLM_RERANK"] = "BASELINE"
    results: list[MatchResult]
    warnings: list[str] = Field(default_factory=list)
    stage_latency_ms: dict[str, float] = Field(default_factory=dict)
    model_usage: dict[str, float | int | str] = Field(default_factory=dict)
    fallback_reasons: list[str] = Field(default_factory=list)
    telemetry_id: str = ""


class CareerPlanRequest(BaseModel):
    profile: ResumeProfile
    match: MatchResult
    horizon_days: int = Field(default=60, ge=7, le=180)


class PlanStep(BaseModel):
    week: int
    goal: str
    actions: list[str]
    evidence: str


class CareerPlan(BaseModel):
    status: Literal["WAITING_FOR_REVIEW"] = "WAITING_FOR_REVIEW"
    target_role: str
    resume_suggestions: list[str]
    interview_questions: list[str]
    learning_plan: list[PlanStep]
    guardrail: str = "仅可重写已有事实；新增经历、技能和量化结果必须由用户确认。"


class EvaluationCase(BaseModel):
    relevant_position_ids: list[int]
    ranked_position_ids: list[int]
    k: int = 10


class EvaluationResult(BaseModel):
    recall_at_k: float
    precision_at_k: float
    reciprocal_rank: float
