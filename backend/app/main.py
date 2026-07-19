from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from core.logger import logger
from core.exceptions import AppBaseException, app_exception_handler, generic_exception_handler
from api.v1.router import api_router

from services.scheduler import scheduler_service

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up Groundwater Intelligence Platform API...")
    if settings.SCHEDULER_ENABLED:
        scheduler_service.start()
    yield
    if settings.SCHEDULER_ENABLED:
        scheduler_service.shutdown()
    logger.info("Shutting down API...")

def get_application() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        description="API for the Groundwater Intelligence Platform",
        version="0.1.0",
        lifespan=lifespan
    )

    # Setup CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.FRONTEND_URL, "http://localhost:3000", "http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register Exception Handlers
    app.add_exception_handler(AppBaseException, app_exception_handler)  # type: ignore
    app.add_exception_handler(Exception, generic_exception_handler)  # type: ignore

    # Include API Routers
    app.include_router(api_router, prefix=settings.API_V1_STR)



    @app.get("/")
    def root():
        return {"message": "Welcome to the Groundwater Intelligence Platform API. See /docs for documentation."}

    return app

app = get_application()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
