# JobPilot AI 求职决策平台

JobPilot 是一个面向学生和初入职场用户的 AI 求职决策平台。系统将简历解析为可确认的能力画像，通过职位混合匹配、硬条件过滤和可解释重排返回推荐结果，并生成受事实约束的简历建议、面试问题与 60 天学习计划。

本仓库用于求职作品展示和技术交流。仓库只包含合成简历与脱敏演示职位，不包含真实求职者数据、招聘决策或生产密钥。代码采用 MIT License；界面图片等视觉素材的使用边界见 [ASSET_NOTICE.md](ASSET_NOTICE.md)。

> 项目不会替用户编造工作经历、项目、技能或量化结果。所有 AI 生成内容均停留在 `WAITING_FOR_REVIEW`，由用户确认后才能采用。

## 核心能力

- PDF、DOCX、TXT、Markdown 简历解析与标准化技能抽取
- 中英文文本相关度、技能覆盖率、求职方向和城市硬条件组成的可解释排序
- 匹配证据、缺失技能、风险提示与分数拆解
- 面向目标职位的简历修改建议、面试问题和学习路线
- 没有模型密钥时使用确定性算法运行；配置兼容 OpenAI 的模型服务后可扩展结构化生成
- JWT 登录、用户身份由服务端解析、AI 服务内部鉴权
- Prometheus 指标、推荐离线评测、CI 和 Docker Compose

## 架构

```text
Vue 2 Web
   │ /api
Spring Boot ── MySQL / Redis
   │ internal API
FastAPI AI Service ── parser / hybrid ranker / career workflow
   │
PostgreSQL + pgvector（向量索引表与全文索引基础设施）
```

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
```

当前 12 条脱敏评测样例覆盖多个目标职位，并计算 Recall@K、Precision@K 与 MRR。公开演示数据只用于回归，真实上线前仍需建立人工标注集。

## 安全与隐私

- 简历属于敏感个人信息，不写入日志，不提交真实简历到仓库。
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

- PostgreSQL 已提供 pgvector 与全文索引结构；大规模职位库应将当前请求内排序升级为持久化召回 + Cross-Encoder 重排。
- 扫描版 PDF 需要接入 OCR 服务，当前会明确提示无法提取文本。
- 推荐效果必须通过扩充后的脱敏标注集验证，不应使用页面上的匹配分代替业务效果评测。

## 公开仓库安全说明

- 演示账号和默认密码只用于本地运行，公网部署前必须删除或替换。
- `.env.example` 中的值均为占位符或本地开发默认值，生产环境必须单独配置密钥和密码。
- 不要向 Issue、日志、测试数据或仓库提交真实简历、邮箱、手机号和招聘记录。
- 发现安全问题时请按照 [SECURITY.md](SECURITY.md) 私下联系仓库维护者。
