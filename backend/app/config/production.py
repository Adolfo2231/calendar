from .settings import Settings

class ProductionSettings(Settings):
    """Production environment configuration"""
    
    DEBUG: bool = False
    ENVIRONMENT: str = "production"
    # DATABASE_URL should be set via environment variable
    # DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/calendar_db"
    
    class Config:
        env_file = ".env.production"

