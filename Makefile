# Makefile for FastAPI application

# Configuration
APP_MODULE = app:app
HOST = 127.0.0.1
PORT = 8000
LOG_LEVEL = info

.PHONY: run-prod run-dev d-up d-down freeze

run-prod:
	@echo "Starting production server (Gunicorn + Uvicorn workers)..."
	gunicorn -c gunicorn_config.py $(APP_MODULE)

run-dev:
	@echo "Starting development server (Uvicorn with auto-reload)..."
	uvicorn $(APP_MODULE) \
		--host $(HOST) \
		--port $(PORT) \
		--reload \
		--log-level $(LOG_LEVEL)

d-up:
	@echo "Start docker container"
	docker-compose up -d

d-down:
	@echo "Stop docker container"
	docker-compose down

freeze:
	@echo "Saving dependencies to requirements.txt"
	pip freeze > requirements.txt