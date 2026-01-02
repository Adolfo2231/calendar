from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.config import settings
from app.models import BaseModel, User  # Importar modelos para que SQLAlchemy los registre

# Crear engine asíncrono usando configuración
engine = create_async_engine(
    settings.DATABASE_URL, 
    echo=settings.DEBUG  # Solo mostrar SQL en desarrollo
)

# Crear session factory
AsyncSessionLocal = async_sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

async def get_db() -> AsyncSession:
    """Dependency para obtener sesión de BD"""
    async with AsyncSessionLocal() as session:
        yield session

async def init_db():
    """Crear todas las tablas en la base de datos"""
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)

