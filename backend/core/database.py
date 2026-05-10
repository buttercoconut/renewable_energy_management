import asyncpg
from .config import settings

async def get_pool():
    return await asyncpg.create_pool(dsn=settings.DATABASE_URL)
