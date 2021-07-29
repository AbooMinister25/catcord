from tortoise import Tortoise

from src.core.config import DATABASE_URL


async def init_orm():
    await Tortoise.init(
        db_url=DATABASE_URL, modules={"models": ["src.database.models"]}
    )

    await Tortoise.generate_schemas()
