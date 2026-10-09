from app.schemas import PositionInput


POSITIONS = [
    PositionInput(position_id=1, company="示例科技", title="AI应用开发实习生", description="Python FastAPI 大模型应用 RAG Agent 向量检索 Prompt Engineering Docker 模型评测", address="上海"),
    PositionInput(position_id=2, company="数据智能实验室", title="NLP算法实习生", description="PyTorch Transformers 自然语言处理 模型训练 评测 推理优化", address="北京"),
    PositionInput(position_id=3, company="云启网络", title="Java后端实习生", description="Java Spring Boot MySQL Redis 接口设计 测试 Docker", address="深圳"),
    PositionInput(position_id=4, company="星河智能", title="大模型应用开发实习生", description="Python FastAPI LangChain RAG 向量数据库 检索评测 Prompt 服务部署", address="杭州"),
    PositionInput(position_id=5, company="远航科技", title="Agent开发实习生", description="Python LLM Function Calling 工作流编排 多Agent Docker 自动化测试", address="上海"),
    PositionInput(position_id=6, company="知行教育", title="教育AI应用实习生", description="智能备课 题目生成 知识库 RAG 结构化输出 内容安全 教师反馈", address="北京"),
    PositionInput(position_id=7, company="云杉数据", title="大模型评测实习生", description="评测集 准确率 召回率 Groundedness 延迟 Bad Case Python 数据分析", address="上海"),
    PositionInput(position_id=8, company="极光产品实验室", title="AI产品经理实习生", description="AI产品 需求分析 Prompt 原型 效果评测 用户反馈 算法工程协作", address="杭州"),
    PositionInput(position_id=9, company="矩阵安全", title="AI安全实习生", description="Prompt Injection 敏感信息保护 模型输出治理 红队评测 Python LLM", address="北京"),
    PositionInput(position_id=10, company="海纳搜索", title="搜索推荐实习生", description="召回 排序 特征工程 推荐离线评测 Python SQL 向量检索 AB测试", address="上海"),
    PositionInput(position_id=11, company="开源云端", title="Python后端实习生", description="Python FastAPI PostgreSQL Redis API 测试 日志 监控 Docker", address="杭州"),
    PositionInput(position_id=12, company="智联咨询", title="AI数据运营实习生", description="数据清洗 标注规范 模型输出抽检 评测集 问题归因 SQL Python", address="上海"),
    PositionInput(position_id=13, company="模型工场", title="机器学习平台实习生", description="模型服务 推理监控 MLOps GPU调度 Python Kubernetes Docker Prometheus", address="深圳"),
    PositionInput(position_id=14, company="创想交互", title="AI前端开发实习生", description="Vue TypeScript 流式对话 引用展示 AI工作台 REST API SSE 前端性能", address="上海"),
    PositionInput(position_id=15, company="数语科技", title="知识工程实习生", description="文档解析 知识抽取 Embedding 向量数据库 检索质量 Python RAG PostgreSQL", address="杭州"),
]


# 每类画像由人工标注相关岗位，再使用四种措辞验证同一求职意图的表达变化。
ARCHETYPES = [
    (["AI应用开发", "大模型应用开发", "RAG开发", "人工智能应用开发"], "Python FastAPI RAG pgvector Prompt Engineering Docker 大模型应用项目", [1, 4, 6, 15]),
    (["NLP算法", "自然语言处理", "文本算法", "语言模型算法"], "PyTorch Transformers 自然语言处理 模型训练与推理优化", [2]),
    (["Java后端", "Java服务端", "后端开发", "服务端开发"], "Java Spring Boot MySQL Redis 接口开发与自动化测试", [3]),
    (["RAG应用开发", "知识库开发", "检索增强生成", "大模型知识库"], "文档解析 Embedding 向量数据库 混合检索 引用评测 Python", [1, 4, 6, 15]),
    (["Agent开发", "智能体开发", "工作流编排", "大模型Agent"], "Python LLM Function Calling 工作流编排 Agent 自动化测试", [1, 5]),
    (["教育AI应用", "智能教育开发", "AI备课应用", "教育大模型应用"], "智能备课 知识库 RAG 结构化输出 内容审核 教师反馈", [1, 4, 6]),
    (["大模型评测", "AI质量评测", "模型效果评估", "大模型测试"], "Python 数据分析 评测集 Bad Case 召回率 Groundedness 延迟", [7, 12]),
    (["AI产品经理", "人工智能产品", "大模型产品", "AI产品设计"], "需求分析 Prompt 原型设计 效果评测 用户访谈 跨团队协作", [8]),
    (["AI安全", "大模型安全", "模型治理", "生成式AI安全"], "Python LLM Prompt Injection 敏感信息保护 输出治理 红队评测", [9]),
    (["搜索推荐", "推荐系统", "智能搜索", "召回排序"], "Python SQL 召回 排序 向量检索 推荐离线评测 AB测试", [10, 15]),
    (["Python后端", "Python服务端", "FastAPI后端", "API开发"], "Python FastAPI PostgreSQL Redis API Docker 日志监控", [1, 4, 11]),
    (["AI数据运营", "模型数据运营", "数据标注运营", "AI质量运营"], "SQL Python 数据清洗 标注规范 模型输出抽检 评测集维护", [7, 12]),
    (["机器学习平台", "MLOps平台", "模型工程平台", "推理平台"], "Python Kubernetes Docker Prometheus 模型服务 推理监控 MLOps", [13]),
    (["AI前端开发", "智能应用前端", "大模型前端", "AI工作台开发"], "Vue TypeScript SSE 流式对话 引用展示 REST API 前端性能", [14]),
    (["知识工程", "知识库工程", "文档智能", "知识检索"], "Python 文档解析 知识抽取 Embedding pgvector RAG 检索质量", [4, 6, 15]),
]


PREFIXES = [
    "项目经验：",
    "在课程与个人项目中完成：",
    "具备相关实践，包括：",
    "目标岗位所需能力：",
]


def _resume_variant(evidence: str, variant: int) -> str:
    tokens = evidence.split()
    if variant == 0:
        return PREFIXES[variant] + evidence
    if variant == 1:
        return PREFIXES[variant] + " ".join(tokens[::2])
    if variant == 2:
        return PREFIXES[variant] + evidence + " Git 团队协作 Vue"
    return PREFIXES[variant] + "，".join(tokens)


def benchmark_profiles():
    return [
        {
            "case_id": f"{index:02d}-{variant + 1}",
            "target_role": target_roles[variant],
            "resume_text": _resume_variant(evidence, variant),
            "relevant_position_ids": relevant_ids,
        }
        for index, (target_roles, evidence, relevant_ids) in enumerate(ARCHETYPES, start=1)
        for variant in range(len(PREFIXES))
    ]
