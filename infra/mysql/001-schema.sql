CREATE TABLE IF NOT EXISTS user (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(64) NOT NULL UNIQUE,
  password VARCHAR(100) NOT NULL,
  email VARCHAR(128) NOT NULL UNIQUE,
  phone VARCHAR(32), state TINYINT NOT NULL DEFAULT 1
);
CREATE TABLE IF NOT EXISTS positions (
  position_id INT PRIMARY KEY AUTO_INCREMENT,
  company VARCHAR(128) NOT NULL, title VARCHAR(128) NOT NULL,
  salary VARCHAR(64), education VARCHAR(64), description TEXT NOT NULL,
  hiring_manager VARCHAR(64), last_active VARCHAR(64), address VARCHAR(128),
  INDEX idx_position_title (title), INDEX idx_position_company (company)
);
INSERT INTO positions(company,title,salary,education,description,address) VALUES
('示例科技','AI应用开发实习生','200-300元/天','本科','使用 Python、FastAPI 开发大模型应用，负责 RAG、Agent、向量检索、Prompt Engineering、Docker 部署与模型评测。','上海'),
('数据智能实验室','NLP算法实习生','250-350元/天','硕士优先','使用 PyTorch、Transformers 完成自然语言处理、模型训练、评测与推理优化。','北京'),
('云启网络','Java后端实习生','180-250元/天','本科','负责 Java、Spring Boot、MySQL、Redis 后端服务开发，参与接口设计、测试和 Docker 部署。','深圳'),
('星河智能','大模型应用开发实习生','220-320元/天','本科','基于 Python、FastAPI 和 LangChain 构建 RAG 应用，负责向量数据库、检索评测、Prompt 优化与服务部署。','杭州'),
('远航科技','Agent 开发实习生','250-350元/天','本科','开发工具调用、工作流编排和多 Agent 协作能力，要求熟悉 Python、LLM、Function Calling、Docker 和自动化测试。','上海'),
('知行教育','教育 AI 应用实习生','180-260元/天','本科','参与智能备课与题目生成产品，负责知识库、RAG、结构化输出、内容安全和教师反馈闭环。','北京'),
('云杉数据','大模型评测实习生','180-280元/天','本科','建设大模型应用评测集，分析准确率、召回率、Groundedness、延迟和 Bad Case，要求熟悉 Python 与数据分析。','上海'),
('极光产品实验室','AI 产品经理实习生','180-250元/天','本科','负责 AI 产品需求分析、Prompt 方案、原型、效果评测和用户反馈，能够与算法及工程团队协作。','杭州'),
('矩阵安全','AI 安全实习生','220-320元/天','硕士优先','研究 Prompt Injection、敏感信息保护、模型输出治理和红队评测，熟悉 Python 与 LLM 应用。','北京'),
('海纳搜索','搜索推荐实习生','220-320元/天','本科','负责召回、排序、特征工程和推荐离线评测，熟悉 Python、SQL、向量检索和 A/B 测试。','上海'),
('开源云端','Python 后端实习生','180-260元/天','本科','使用 Python、FastAPI、PostgreSQL、Redis 开发 API，负责测试、日志、监控和 Docker 部署。','杭州'),
('智联咨询','AI 数据运营实习生','150-220元/天','本科','负责数据清洗、标注规范、模型输出抽检、评测集维护和问题归因，要求掌握 SQL 与基础 Python。','上海'),
('模型工场','机器学习平台实习生','250-350元/天','硕士优先','参与模型服务、推理监控、MLOps 和 GPU 资源调度，熟悉 Python、Kubernetes、Docker 与 Prometheus。','深圳'),
('创想交互','AI 前端开发实习生','180-280元/天','本科','使用 Vue、TypeScript 开发流式对话、引用展示与 AI 工作台，理解 REST API、SSE 和前端性能优化。','上海'),
('数语科技','知识工程实习生','200-300元/天','本科','负责文档解析、知识抽取、Embedding、向量数据库与检索质量分析，熟悉 Python、RAG 和 PostgreSQL。','杭州');
CREATE TABLE IF NOT EXISTS recommendation_feedback (
  id BIGINT PRIMARY KEY AUTO_INCREMENT, user_id INT NOT NULL, position_id INT NOT NULL,
  action VARCHAR(32) NOT NULL, reason VARCHAR(255), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_feedback_user (user_id)
);
INSERT IGNORE INTO user(user_id,username,password,email,phone,state) VALUES
(10001,'demo_candidate','$2a$10$7exF6/xwsz8pp0kJz1J3qOVqoTchsf/E98Q4DKG926wmGQJVAx3D.','demo-candidate@example.com','13800000001',1);
