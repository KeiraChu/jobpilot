import io
import json
import re
from pathlib import Path

from docx import Document
from pypdf import PdfReader

SKILLS = {
    "python", "java", "javascript", "typescript", "vue", "react", "spring boot",
    "fastapi", "mysql", "postgresql", "redis", "docker", "kubernetes", "git",
    "pytorch", "tensorflow", "transformers", "llm", "rag", "agent", "langchain",
    "langgraph", "mcp", "function calling", "prompt engineering", "pgvector",
    "milvus", "elasticsearch", "neo4j", "机器学习", "深度学习", "大模型",
    "向量数据库", "知识图谱", "自然语言处理", "数据分析",
}


def extract_file_text(filename: str, content: bytes) -> str:
    suffix = Path(filename).suffix.lower()
    if suffix == ".pdf":
        return "\n".join(page.extract_text() or "" for page in PdfReader(io.BytesIO(content)).pages)
    if suffix == ".docx":
        return "\n".join(p.text for p in Document(io.BytesIO(content)).paragraphs)
    if suffix in {".txt", ".md"}:
        return content.decode("utf-8", errors="ignore")
    raise ValueError("仅支持 PDF、DOCX、TXT、Markdown 文件")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_skills(text: str) -> list[str]:
    lowered = text.lower()
    return sorted(skill for skill in SKILLS if skill.lower() in lowered)


def heuristic_profile(text: str, target_role: str = ""):
    from app.schemas import Experience, ResumeProfile

    clean = normalize(text)
    sections = re.split(r"(?=教育经历|项目经历|工作经历|实习经历|专业技能|技能)", text)
    projects, education, work = [], [], []
    for section in sections:
        item = Experience(description=normalize(section)[:1500])
        if section.startswith("项目经历"):
            projects.append(item)
        elif section.startswith("教育经历"):
            education.append(item)
        elif section.startswith(("工作经历", "实习经历")):
            work.append(item)
    return ResumeProfile(
        target_role=target_role,
        education=education,
        projects=projects,
        work_experience=work,
        skills=extract_skills(clean),
        summary=clean[:800],
        confidence=0.65 if extract_skills(clean) else 0.4,
        warnings=["当前使用规则解析，请确认技能和经历是否完整。"],
    )


def _profile_schema() -> dict:
    experience = {
        "type": "object", "additionalProperties": False,
        "properties": {key: {"type": "string"} for key in ("title", "organization", "period", "description")},
        "required": ["title", "organization", "period", "description"],
    }
    evidence = {
        "type": "object", "additionalProperties": False,
        "properties": {"field": {"type": "string"}, "value": {"type": "string"}, "quote": {"type": "string"}},
        "required": ["field", "value", "quote"],
    }
    return {
        "type": "object", "additionalProperties": False,
        "properties": {
            "education": {"type": "array", "items": experience},
            "projects": {"type": "array", "items": experience},
            "work_experience": {"type": "array", "items": experience},
            "skills": {"type": "array", "items": {"type": "string"}},
            "summary": {"type": "string"},
            "evidence": {"type": "array", "items": evidence},
        },
        "required": ["education", "projects", "work_experience", "skills", "summary", "evidence"],
    }


async def structured_profile(text: str, target_role: str, provider):
    """Extract a profile while requiring every claimed field to cite an exact source span."""
    from app.schemas import Experience, ResumeProfile, SourceEvidence

    if provider is None:
        return heuristic_profile(text, target_role)
    messages = [
        {"role": "system", "content": (
            "你是简历结构化解析器。只能提取原文明确出现的信息，不得推测或补全。"
            "每项技能和重要经历必须提供一段逐字存在于原文的 quote；无法提供原文证据的内容不要输出。"
        )},
        {"role": "user", "content": json.dumps({"target_role": target_role, "resume_text": text[:50_000]}, ensure_ascii=False)},
    ]
    try:
        payload = await provider.json(messages, _profile_schema(), "resume_profile")
        evidence = []
        supported_values = set()
        for item in payload.get("evidence", []):
            quote = str(item.get("quote", "")).strip()
            start = text.find(quote)
            if not quote or start < 0:
                continue
            value = str(item.get("value", "")).strip()
            evidence.append(SourceEvidence(field=str(item.get("field", "")), value=value, quote=quote, start=start, end=start + len(quote)))
            supported_values.add(value.lower())
        skills = [skill for skill in payload.get("skills", []) if str(skill).lower() in supported_values]
        warnings = []
        if len(skills) != len(payload.get("skills", [])):
            warnings.append("部分缺少原文证据的技能已被移除。")
        def supported_experiences(items: list[dict], category: str) -> list[Experience]:
            accepted = []
            for item in items:
                title = str(item.get("title", "")).lower()
                if any(category in source.field.lower() or (title and source.value.lower() == title) for source in evidence):
                    accepted.append(Experience.model_validate(item))
            return accepted
        education = supported_experiences(payload.get("education", []), "education")
        projects = supported_experiences(payload.get("projects", []), "project")
        work = supported_experiences(payload.get("work_experience", []), "work")
        if len(education) + len(projects) + len(work) < sum(len(payload.get(key, [])) for key in ("education", "projects", "work_experience")):
            warnings.append("部分缺少原文证据的经历已被移除。")
        return ResumeProfile(
            target_role=target_role,
            education=education,
            projects=projects,
            work_experience=work,
            skills=skills,
            summary=normalize(text)[:1200],
            confidence=min(0.95, 0.55 + 0.04 * len(evidence)),
            evidence=evidence,
            parsing_mode="LLM_STRUCTURED",
            warnings=warnings,
        )
    except Exception:
        profile = heuristic_profile(text, target_role)
        profile.warnings = ["结构化模型解析失败，已降级为规则解析，请人工确认结果。"]
        return profile
