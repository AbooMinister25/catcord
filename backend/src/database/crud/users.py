from typing import Union

from loguru import logger
from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from src.database.database import async_session
from src.database.models import User


async def get_user_dal():
    async with async_session() as session:
        async with session.begin():
            yield UserDAL(session)


class UserDAL:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    async def create_user(
        self,
        username: str,
        password: str,
        email: str,
        uid: str,
        token: str,
    ) -> None:
        user = User(
            user_id=uid, token=token, username=username, password=password, email=email
        )
        self.db_session.add(user)
        await self.db_session.flush()

    async def check_email_exists(self, email: str) -> bool:
        logger.info(f"Attempting to find user with email {email}")

        emails = await self.db_session.execute(select(User).where(User.email == email))

        return emails.scalar()

    async def get_public_user_info(self, uid: str) -> Union[str, None]:
        logger.info(f"Attempting to get public user info for user with UID {uid}")

        users = await self.db_session.execute(select(User).where(User.user_id == uid))

        user = users.scalars().first()

        if not user:
            logger.info(f"No user with UID {uid}")
            return

        logger.success(
            f"Successfully retrieved public user info for user with UID {uid}"
        )
        return user.username

    async def auth_with_password(self, password: str, uid: str) -> bool:
        logger.info(f"Attempting to authorize user with uid {uid} in database")

        users = await self.db_session.execute(select(User).where(User.user_id == uid))
        user = users.scalars().first()

        if not user:
            logger.info(f"No user with UID {uid}")
            return False

        if password != user.password:
            logger.info(
                f"Authentication for user with UID {uid} faled. Invalid password"
            )
            return False

        logger.success(f"Successfully authorized user with UID {uid}")
        return True

    async def update_user_token(self, uid: str, token: str) -> None:
        logger.info(
            f"Attempting to modify API token for user with UID {uid} in database"
        )

        query = update(User).where(User.user_id == uid)
        query = query.values(token=token)

        query.execution_options(synchronize_session="fetch")
        await self.db_session.execute(query)

    async def auth_with_token(self, token: str, uid: str) -> bool:
        logger.info(f"Attempting to authorize user with token {token} in database")

        user = await self.db_session.execute(
            select(User).filter_by(User.user_id == uid)
        ).first()

        if not user:
            logger.info(f"No user with UID {uid}")
            return False

        if token != user.token:
            logger.info(f"Authentication for user with UID {uid} failed. Invalid token")
            return False

        logger.success(f"Successfully authorized user with UID {uid}")
        return True
