# 真实模型评测报告

- 状态：尚未执行
- 原因：仓库和测试环境不保存真实模型 API Key。
- 小规模验证：`PYTHONPATH=. python evals/run_real.py --limit 5`
- 完整评测：`PYTHONPATH=. python evals/run_real.py`

脚本会实际执行结构化简历解析、Embedding 排序和大模型重排，并记录 Recall@5、Precision@5、MRR、排序模式、延迟、Token 和估算费用。未执行前，不应声称真实模型带来了指标提升。
