import typing
import asyncpg
from backend.core.config import DATABASE_URL
from backend.core.logger import Logger

logger = Logger(mode="file", filename="database.log")


class Database:
    def __init__(self, database_url: str = DATABASE_URL):
        self.url = database_url

    async def __aenter__(self) -> typing.Optional[asyncpg.Connection]:
        await logger.info("Attempting to connect to database")

        try:
            self.conn = await asyncpg.connect(self.url)
            await logger.success("Successfully connected to database")
            return self.conn
        except:
            await logger.error(
                "Exception occured while attempting to connect to database", exc=True
            )

    async def __aexit__(self, exc_type, exc, tb):
        if isinstance(exc, Exception):
            await logger.error(
                f"The following exception occured while interacting with database: {exc_type}",
                exc=True,
            )
            await logger.error(str(exc))
        if self.conn:
            await logger.info("Closing database connection")
            await self.conn.close()
