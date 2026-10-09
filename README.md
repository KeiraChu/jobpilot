# JobPilot AI 求职决策平台

JobPilot 是一个面向学生和初入职场用户的 AI 求职决策平台。系统将简历解析为可确认的能力画像，通过职位混合匹配、硬条件过滤和可解释重排返回推荐结果，并生成受事实约束的简历建议、面试问题与 60 天学习计划。

本仓库用于求职作品展示和技术交流。仓库只包含合成简历与脱敏演示职位，不包含真实求职者数据、招聘决策或生产密钥。代码采用 MIT License；界面图片等视觉素材的使用边界见 [ASSET_NOTICE.md](ASSET_NOTICE.md)。

> 项目不会替用户编造工作经历、项目、技能或量化结果。所有 AI 生成内容均停留在 `WAITING_FOR_REVIEW`，由用户确认后才能采用。

## 核心能力

- PDF、DOCX、TXT、Markdown 简历解析；模型结构化提取必须附带可定位的原文证据，失败时降级为规则解析
- Embedding 语义召回、技能证据和硬条件组成的混合排序，并对候选集执行大模型结构化重排
- 匹配证据、缺失技能、风险提示、分数拆解与单项技能补强收益估算
- 面向目标职位的简历修改建议、面试问题和学习路线
- 模型重排只能引用简历已识别的技能证据；没有模型密钥或调用失败时自动降级为可解释基线
- JWT 登录、用户身份由服务端解析、AI 服务内部鉴权
- Prometheus 指标、推荐离线评测、CI 和 Docker Compose
- 返回解析与推荐各阶段耗时、Token、估算费用和标准化降级原因

## 架构

```text
Vue 2 Web
   │ /api
Spring Boot ── MySQL / Redis
   │ internal API
FastAPI AI Service ── parser / embedding retrieval / LLM reranker / career workflow
   │
PostgreSQL + pgvector（岗位向量持久化、HNSW 与全文检索）
```

配置 pgvector 后，推荐链路先增量同步发生变化的岗位向量，再使用 HNSW 向量检索与全文检索通过 RRF 融合召回候选；候选集结合技能证据排序，最后由大模型执行结构化重排。模型返回的证据必须通过技能白名单校验，不读取性别、年龄、照片等属性；数据库、Embedding 或重排失败时逐级降级，不影响基本推荐。每条推荐返回决策轨迹，并明确“补强收益”不代表录用概率。详细分层与取舍见 [架构说明](docs/architecture.md)。

旧的 BERT、Doc2Vec、Neo4j 脚本和手工联调测试归档在 `experiments/`，不再进入在线推荐链路或 CI。在线系统不依赖本机 Socket、固定模型路径或硬编码推荐结果。

## 快速启动

```bash
cp .env.example .env
docker compose up --build
```

- Web：<http://localhost:8080>
- Java API：<http://localhost:8088>
- AI API 文档：<http://localhost:8000/docs>
- AI 指标：<http://localhost:8000/metrics>

首次启动会写入十五个脱敏演示职位。生产环境必须替换 JWT Secret、内部服务密钥和数据库密码。

演示账号为 `demo_candidate / Demo@2026`，样例简历位于 `demo/AI应用开发实习生-脱敏简历.md`。首次启动实际写入 15 个脱敏职位，完整讲解顺序见 [面试演示手册](docs/demo-guide.md)。

## 关键接口

| 接口 | 说明 |
| --- | --- |
| `POST /upload` | 上传简历并返回能力画像与职位推荐 |
| `POST /resume/submit` | 使用在线表单内容进行推荐 |
| `POST /ai/career-plan` | 基于选中职位生成人工审核中的准备计划 |
| `POST /v1/resumes/files` | AI 服务文件解析 |
| `POST /v1/matches/recommend` | 混合评分与解释 |
| `POST /v1/evaluations/recommendation` | Recall@K、Precision@K、MRR 计算 |

## 评测

```bash
cd ai-service
pytest -q
python evals/run.py
python evals/run_real.py --limit 5  # 配置真实模型后先运行少量付费验证
```

当前评测集包含 15 类候选人画像，每类加入目标岗位别名、部分技能缺失和无关技能噪声，共形成 60 条脱敏合成回归样例。可解释基线在该数据集上的 Recall@5 为 82.78%、Precision@5 为 31.33%、MRR 为 91.39%。详细口径见 [评测说明](docs/evaluation.md)。这些结果只用于离线回归，不能代表真实招聘效果；Embedding 与模型重排仍需在配置真实模型后单独评测。

## 安全与隐私

- 简历属于敏感个人信息，不写入日志，不提交真实简历到仓库。
- 演示页面明确提示使用脱敏简历；配置外部模型后，简历文本会发送至所配置的 Embedding 和大模型服务，生产环境必须补充用户授权、隐私政策及数据保留说明。
- 上传限制为 20MB，并只解析明确允许的文档格式。
- Java API 使用 JWT；用户 ID 由后端登录态确定。
- Java 与 AI 服务之间使用独立内部密钥。
- 密码使用 BCrypt；验证码成功后立即失效，日志不记录验证码。
- 注册验证码与用户名、邮箱绑定，带发送频率限制，注册接口必须消费短时验证状态。
- 旧版本使用 SHA-256 保存的本地测试账号无法直接兼容 BCrypt；升级后请重新注册测试账号，生产迁移应单独执行一次性密码重置方案。
- AI 输出仅提供建议，不能用于自动拒绝候选人或进行歧视性筛选。

## 目录

```text
ai-service/   FastAPI AI 编排、解析、排序和评测
backend/      Spring Boot 业务 API、鉴权和数据访问
frontend/     Vue Web 与 AI 求职助手页面
infra/        MySQL 与 pgvector 初始化脚本
experiments/  早期离线实验和手工联调记录（不参与在线服务）
```

## 后续工程边界

- 当前已实现持久化向量与全文混合召回；职位规模继续扩大后，应将岗位同步拆为独立离线任务，并评估 Cross-Encoder 或学习排序模型。
- 扫描版 PDF 需要接入 OCR 服务，当前会明确提示无法提取文本。
- 推荐效果必须通过扩充后的脱敏标注集验证，不应使用页面上的匹配分代替业务效果评测。

## 公开仓库安全说明

- 演示账号和默认密码只用于本地运行，公网部署前必须删除或替换。
- `.env.example` 中的值均为占位符或本地开发默认值，生产环境必须单独配置密钥和密码。
- 不要向 Issue、日志、测试数据或仓库提交真实简历、邮箱、手机号和招聘记录。
- 发现安全问题时请按照 [SECURITY.md](SECURITY.md) 私下联系仓库维护者。
