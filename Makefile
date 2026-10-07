.PHONY: up down test eval
up:
	docker compose up --build
down:
	docker compose down
test:
	cd ai-service && pytest -q
	cd backend && mvn test
	cd frontend && npm run build
eval:
	cd ai-service && PYTHONPATH=. python evals/run.py
