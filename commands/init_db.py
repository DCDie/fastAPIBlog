from apps.users.models import User
from config.settings import engine


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)
