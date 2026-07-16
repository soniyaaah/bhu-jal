from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Groundwater Intelligence Platform API"
    API_V1_STR: str = "/api/v1"
    
    # Environment variables can override these
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # Dummy variables for future usage
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    API_KEY_SECRET: str = os.getenv("API_KEY_SECRET", "")
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")

    model_config = {
        "case_sensitive": True,
        "env_file": ".env"
    }

settings = Settings()
