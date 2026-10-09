import asyncio

from app.parsing import structured_profile


class ExtractionProvider:
    async def json(self, messages, schema, name):
        return {
            "education": [],
            "projects": [{"title": "知识库项目", "organization": "", "period": "", "description": "使用 Python 开发 RAG 系统"}],
            "work_experience": [],
            "skills": ["Python", "RAG", "Kubernetes"],
            "summary": "AI 应用开发",
            "evidence": [
                {"field": "skills", "value": "Python", "quote": "Python"},
                {"field": "skills", "value": "RAG", "quote": "RAG"},
                {"field": "projects", "value": "知识库项目", "quote": "使用 Python 开发 RAG 知识库"},
                {"field": "skills", "value": "Kubernetes", "quote": "原文没有这段"},
            ],
        }


def test_structured_profile_keeps_only_exact_source_evidence():
    text = "项目经历：使用 Python 开发 RAG 知识库。"
    profile = asyncio.run(structured_profile(text, "AI应用开发", ExtractionProvider()))

    assert profile.parsing_mode == "LLM_STRUCTURED"
    assert profile.skills == ["Python", "RAG"]
    assert [item.quote for item in profile.evidence] == ["Python", "RAG", "使用 Python 开发 RAG 知识库"]
    assert profile.projects[0].title == "知识库项目"
    assert profile.evidence[0].start == text.index("Python")
    assert any("缺少原文证据" in warning for warning in profile.warnings)
