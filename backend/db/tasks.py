import typing
import asyncpg
from loguru import logger
from backend.core.config import DATABASE_URL


async def get_db() -> typing.Optional[asyncpg.Connection]:
    logger.info("Attempting to connect to DB")

    try:
        conn = await asyncpg.connect(DATABASE_URL)
        logger.info("Successfully connected to database")
        return conn
    except Exception as e:
        logger.error("Exception occured while attempting to connect to database")
        logger.error(e)
