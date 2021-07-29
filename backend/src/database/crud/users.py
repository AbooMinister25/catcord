from typing import Union

from loguru import logger

from src.database.models import Users


async def create_user(
    username: str,
    password: str,
    email: str,
    uid: str,
    token: str,
) -> None:
    user = Users(
        user_id=uid, token=token, username=username, password=password, email=email
    )
    await user.save()


async def check_email_exists(email: str) -> bool:
    logger.info(f"Attempting to find user with email {email}")

    email_exists = await Users.filter(email=email).exists()

    if email_exists:
        logger.info(f"Email {email} already exists")
        return True

    logger.info(f"Email {email} does not exist")
    return False


async def get_public_user_info(uid: str) -> Union[str, None]:
    logger.info(f"Attempting to get public user info for user with UID {uid}")

    user = await Users.filter(user_id=uid).first()
    if not user:
        logger.info(f"No user with UID {uid}")
        return None

    logger.success(f"Successfully retrived public user info for user with UID {uid}")
    return user.username


async def auth_with_password(password: str, uid: str) -> bool:
    logger.info(f"Attempting to authorize user with uid {uid} in database")

    user = await Users.filter(user_id=uid).first()

    if not user:
        logger.info(f"No user with UID {uid}")
        return False

    if password != user.password:
        logger.info(f"Authentication for user with UID {uid} failed. Invalid password")
        return False

    logger.success(f"Successfully authorized user with UID {uid}")
    return True


async def update_user_token(password: str, uid: str, token: str) -> None:
    logger.info(f"Attempting to modify API token for user with UID {uid} in database")

    authorized = await auth_with_password(password, uid)
    if authorized:
        user = await Users.filter(user_id=uid).first()
        user.token = token
        await user.save()
        logger.success(f"Successfully updated API token for user with uid {uid}")
    else:
        logger.info(
            f"Authentication for user with uid {uid} failed, invalid credentials"
        )


async def auth_with_token(token: str, uid: int) -> bool:
    logger.info(
        f"Attempting to authorize user with token: | {token} | in database with token"
    )

    user = await Users.filter(user_id=uid).first()

    if not user:
        logger.info(f"No user with UID {uid}")
        return False

    if token != user.token:
        logger.info(f"Authentication for user with UID {uid} failed. Invalid Token")
        return False

    logger.success(f"Successfully authorized user token for user with UID {uid}")
    return True
