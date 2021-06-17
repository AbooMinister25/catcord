import typing
import asyncpg
from loguru import logger
from backend.core.config import DATABASE_URL


class Database:
    def __init__(self, database_url: str = DATABASE_URL):
        self.url = database_url

    async def __aenter__(self) -> typing.Optional[asyncpg.Connection]:
        logger.info("Attempting to connect to database")

        try:
            self.conn = await asyncpg.connect(self.url)
            logger.success("Successfully connected to database")
            return self.conn
        except Exception as e:
            logger.error("Exception occured while attempting to connect to database")
            logger.error(e)

    async def __aexit__(self, exc_type, exc, tb):
        if isinstance(exc, Exception):
            logger.error(
                f"The following exception occured while interacting with database: {exc_type}"
            )
            logger.error(exc)
        if self.conn:
            logger.info("Closing database connection")
            await self.conn.close()