"""
Application configuration module.
Loads settings from environment variables.
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./dashboard.db")
    
    # Application
    APP_NAME: str = os.getenv("APP_NAME", "Dashboard Analytics")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # API
    API_V1_PREFIX: str = "/api/v1"


settings = Settings()
