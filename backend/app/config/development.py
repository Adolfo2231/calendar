from .settings import Settings

class DevelopmentSettings(Settings):
    """Development environment configuration"""
    
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = "sqlite+aiosqlite:///./calendar.db"
    
    class Config:
        env_file = ".env.development"

