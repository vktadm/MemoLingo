# Makefile for FastAPI application

# Configuration
APP_MODULE = main:app
HOST = 0.0.0.0
PORT = 8000
LOG_LEVEL = info

.PHONY: run-prod run-dev

run-prod:
	@echo "Starting production server (Gunicorn + Uvicorn workers)..."
	gunicorn -c gunicorn_config.py $(APP_MODULE)

run-dev:
	@echo "Starting development server (Uvicorn with auto-reload)..."
	uvicorn $(APP_MODULE) \
		--host $(HOST) \
		--port $(PORT) \
		--reload \
# 		--log-level $(LOG_LEVEL)