from pydantic_settings import BaseSettings
import os

# Build absolute path to backend directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DB_PATH = os.path.join(BASE_DIR, "bhu_jal.db")

class Settings(BaseSettings):
    PROJECT_NAME: str = "Groundwater Intelligence Platform API"
    API_V1_STR: str = "/api/v1"
    
    # Environment variables can override these
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    SCHEDULER_ENABLED: bool = os.getenv("SCHEDULER_ENABLED", "true").lower() == "true"
    
    # Dummy variables for future usage
    DATABASE_URL: str = os.getenv("DATABASE_URL", f"sqlite:///{DB_PATH}")
    API_KEY_SECRET: str = os.getenv("API_KEY_SECRET", "")
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")

    model_config = {
        "case_sensitive": True,
        "env_file": ".env"
    }

settings = Settings()
