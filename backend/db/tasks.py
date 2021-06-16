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

async def new_user(connection: asyncpg.Connection, id: str, tokenhash: str, username: str, passhash: str):
    logger.info("Attempting to add a new user to DB")
    try:
        await connection.execute(f"INSERT INTO USERS VALUES({id}, '{tokenhash}', '{username}', '{passhash}');")
        logger.info("Successfully added a new user to DB")
    except Exception as e:
        logger.error("Exception occured while trying to add a user to database")
        logger.error(e)

async def new_server(connection: asyncpg.Connection, server_id: str, owner_id: str, server_name: str):
    logger.info("Attempting to add a server to DB")
    try:
        await connection.execute(f"INSERT INTO SERVERS VALUES('{server_id}', '{owner_id}', '{server_name}');")
        logger.info("Successfully added a server to DB")
    except Exception as e:
        logger.error("Exception occured while trying to add a server to database")
        logger.error(e)

async def new_message(connection: asyncpg.Connection, message_id: str, timesent: int, sender_id: str, server_id: str, message_content: str):
    logger.info("Attempting to add a new message to DB")
    try:
        await connection.execute(f"INSERT INTO MESSAGES VALUES('{message_id}', '{timesent}', '{sender_id}', '{server_id}', '{message_content}');")
        logger.info("Successfully added a new message to DB")
    except Exception as e:
        logger.error("Exception occured while trying to add a message to database")
        logger.error(e)

async def get_messages(connection: asyncpg.Connection, server_id: str):
    logger.info("Attempting to get messages from DB")
    try:
        messages = await connection.fetch(f"SELECT * FROM MESSAGES WHERE server_id='{server_id}'")
        logger.info("Successfully retrieved messages from DB")
        return messages
    except Exception as e:
        logger.error("Exception occured while fetching messages from DB")
        logger.error(e)
