# Deployment Strategy

This document details the deployment architecture for the Groundwater Intelligence Platform.

## Environment Variables
Environment variables should be managed using a `.env` file in development and secret managers in production.
Required variables:
- `DATABASE_URL`: Connection string for PostgreSQL/MySQL.
- `API_KEY_SECRET`: Secret key for JWT authentication.
- `FRONTEND_URL`: CORS origin for the frontend application.
- `ENVIRONMENT`: `development`, `staging`, or `production`.

## Folder Layout
Deployment configurations will reside in the repository root:
- `Dockerfile`: Multi-stage build for the FastAPI backend.
- `docker-compose.yml`: Local and simple deployment orchestration (Backend + Database + Redis).
- `frontend/Dockerfile`: Build for the frontend application (served via Nginx).

## Docker Strategy
- **Backend Image**: Based on `python:3.10-slim`. Installs `requirements.txt`, copies `ml/artifacts/`, and runs via Uvicorn.
- **Frontend Image**: Based on `node:alpine`. Builds the Vite app and serves static files using an Nginx alpine image.
- **Database Image**: Standard `postgres:15-alpine` or `mysql:8` image.

## Backend Deployment
- **Platform**: AWS ECS, Google Cloud Run, or a dedicated VPS.
- **Scaling**: The FastAPI service is stateless (assuming ML models are loaded in memory from the baked-in `artifacts/` folder or downloaded from an S3 bucket on startup). It can be scaled horizontally.

## Frontend Deployment
- **Platform**: Vercel, Netlify, or an Nginx container.
- **Routing**: Client-side routing must be configured properly if using Nginx (redirect all requests to `index.html`).

## Database Deployment
- **Platform**: Managed database service (AWS RDS, Google Cloud SQL) for production reliability and automated backups.
- **Migrations**: Alembic should be used for database migrations prior to starting the application container.

## Logging
- Backend logs (generated via `loguru`) should be structured in JSON format for easy ingestion.
- **Aggregation**: Logs forwarded to AWS CloudWatch, Datadog, or an ELK stack.

## Monitoring
- **Health Checks**: 
  - FastAPI: `/health` endpoint returning `{"status": "ok"}`.
  - Database connection check included in the health endpoint.
- **Metrics**: Expose Prometheus metrics from FastAPI for tracking request latency, error rates, and inference times.

## CI/CD
- **GitHub Actions**: 
  1. On Pull Request: Run `pytest`, `flake8`, and `mypy`.
  2. On Merge to `main`: Build Docker images, push to container registry (e.g., Docker Hub, ECR), and trigger a deployment webhook.
