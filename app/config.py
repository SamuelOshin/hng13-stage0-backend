from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """Application settings"""
    
    # User Information
    USER_EMAIL: str = "your.email@example.com"
    USER_NAME: str = "Your Full Name"
    USER_STACK: str = "Python/FastAPI"
    
    # API Configuration
    API_TITLE: str = "Profile API"
    API_VERSION: str = "1.0.0"
    PORT:  int = 7001
    HOST: str = "0.0.0.0"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()

settings = get_settings()