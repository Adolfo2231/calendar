from .settings import Settings

class DevelopmentSettings(Settings):
    """Development environment configuration"""
    
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = "sqlite+aiosqlite:///./calendar.db"
    
    class Config(Settings.Config):
        env_file = ".env"  # Usar .env para desarrollo
        case_sensitive = True

