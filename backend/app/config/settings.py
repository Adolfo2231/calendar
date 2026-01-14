from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """Base configuration settings"""
    
    # Application
    APP_NAME: str = "Calendar API"
    VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    
    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./calendar.db"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    
    # JWT
    JWT_SECRET: str = "your-secret-key-change-in-production"  # Same as SECRET_KEY by default
    JWT_ALGORITHM: str = "HS256"  # Same as ALGORITHM by default
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Access token expires in 30 minutes
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7  # Refresh token expires in 7 days
    
    # CORS
    CORS_ORIGINS: str = "http://localhost:3000"
    
    # OpenAI API (para MCP Server con ChatGPT)
    OPENAI_API_KEY: str = ""
    
    # MCP Server (opcional)
    MCP_SERVER_URL: str = "http://localhost:8000/mcp"
    
    # Email (mínimo necesario)
    MAIL_USERNAME: str = ""
    MAIL_PASSWORD: str = ""
    MAIL_FROM: str = ""
    MAIL_PORT: int = 587
    MAIL_SERVER: str = ""
    # Email opcionales (pueden estar en .env pero tienen valores por defecto)
    MAIL_FROM_NAME: str = ""  # Opcional, si no se especifica usa el email
    MAIL_TLS: bool = False  # Opcional, se detecta automáticamente según puerto
    MAIL_SSL: bool = False  # Opcional, se detecta automáticamente según puerto
    
    class Config:
        env_file = ".env"
        case_sensitive = True

