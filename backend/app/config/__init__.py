# Config package
import os
from .settings import Settings
from .development import DevelopmentSettings
from .production import ProductionSettings

def get_settings() -> Settings:
    """Get settings based on environment"""
    env = os.getenv("ENVIRONMENT", "development").lower()
    
    if env == "production":
        return ProductionSettings()
    else:
        return DevelopmentSettings()

# Export default settings
settings = get_settings()

__all__ = ["settings", "Settings", "DevelopmentSettings", "ProductionSettings", "get_settings"]
