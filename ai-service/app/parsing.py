import io
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
    )

