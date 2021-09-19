import functools
import time
import typing
from typing import Optional

import aioredis
from fastapi.responses import JSONResponse
from loguru import logger


class Ratelimiter:
    """
    Ratelimiter class. Used for implementing
    ratelimits on API routes. Uses the token bucket
    ratelimiting algorithm.

    :param requests: The number of requests that can be sent in a given period.
    :param period: The time period in which requests can be sent.
    :param cooldown: The cooldown time that is applied if a user goes over the
    limit of requests per a given period.
    :param redis_host: Used to define the host for the redis database
    used. Defaults to `"redis"`.
    :param redis_port: Used to define the port used for the redis
    database. Defaults to `6379`.
    """

    def __init__(
        self,
        requests: int,
        period: int,
        cooldown: int,
        redis_host: Optional[str] = "redis",
        redis_port: Optional[int] = 6379,
    ) -> None:
        self.requests = requests
        self.period = period
        self.cooldown = cooldown

        self.redis = aioredis.Redis(
            host=redis_host, port=redis_port, decode_responses=True
        )

    async def key_exists(self, key: str) -> bool:
        """
        Check if the given key exists in the
        redis database.

        :param key: The key to be used in the
        redis database.
        :return: boolean.
        """

        exists = await self.redis.exists(key)
        return exists

    async def register(
        self, key: str, requests: int, period: int, cooldown: int
    ) -> dict:
        """
        Used to register a new request into
        the redis database.

        :param key: The key to be used to name the registered hash in the redis database.
        :param requests: The number of requests that can be sent in a given period.
        :param period: The time period in which requests can be sent.
        :param cooldown: The cooldown time that is applied if a user goes over the
        limit of requests per a given period.
        :return: A dict containing the data registered.
        """

        data = {
            "requests": requests,
            "period": period,
            "cooldown": cooldown,
            "last_check": time.time(),
            "bucket": requests,
        }

        await self.redis.hmset(key, data)
        return data

    async def get_data(self, key: str) -> dict:
        """
        Retrieves data from the redis database used
        using the given key and returns it as a python
        dict.

        :param key: The key to be used in the redis
        database.
        :return: A dict containing the data retrieved from
        the redis db.
        """

        data = await self.redis.hgetall(key)
        return data

    async def update_data(self, key: str, bucket: int, last_check: int) -> None:
        """
        Updates the bucket for a given key in the
        redis database.

        :param key: The key used in the redis database
        for the hash.
        :param bucket: The new bucket.
        :param last_check: The new time that the ratelimit was last
        checked.
        """

        await self.redis.hset(key, "bucket", bucket)
        await self.redis.hset(key, "last_check", last_check)

    def limit(
        self,
        requests: Optional[int] = None,
        period: Optional[int] = None,
        cooldown: Optional[int] = None,
    ) -> typing.Callable:
        """
        Decorator method used to wrap API routes
        that need to be ratelimited.

        :param requests: The number of requests that can be sent in a given period.
        If not provided, uses the value set in initialization of the class.
        :param period: The time period in which requests can be sent.
        If not provided, uses the value set in initialization of the class.
        :param cooldown: The cooldown time that is applied if a user goes over the
        limit of requests per a given period. If not provided, uses the
        value set in initialization of the class.
        :return: Wrapped callable.
        """
        requests, period, cooldown = (
            self.requests if not requests else requests,
            self.period if not period else period,
            self.cooldown if not cooldown else cooldown,
        )

        def wrapper(handler):
            @functools.wraps(handler)
            async def route_wrapper(*args, **kwargs):
                request = kwargs["request"]
                ip = request.client.host
                key = f"hash:{ip}"

                exists = await self.key_exists(key)

                if not exists:
                    data = await self.register(key, requests, period, cooldown)
                    current = data["current"]
                else:
                    data = await self.get_data(key)
                    current = time.time()

                time_passed = current - float(data["last_check"])
                last_check = current

                bucket, ratelimited = self.is_ratelimited(
                    int(data["requests"]),
                    float(data["period"]),
                    float(data["bucket"]),
                    time_passed,
                )

                if ratelimited:
                    logger.info(f"Request from host {ip} dropped")
                    await self.update_data(key, bucket, last_check)
                    response = JSONResponse(
                        content={
                            "message": "You are being ratelimited, try again later."
                        },
                        status_code=429,
                    )
                else:
                    logger.info(f"Request from host {ip} accepted")
                    await self.update_data(key, bucket, last_check)
                    response = await handler(*args, **kwargs)

                return response

            return route_wrapper

        return wrapper

    def is_ratelimited(
        self,
        requests: int,
        period: float,
        bucket: float,
        time_passed: int,
    ) -> typing.Tuple[int, bool]:
        """
        Checks whether a request is ratelimited or not
        based on the given information.

        :param requests: Number of requests that can be sent in
        a specified time period.
        :param period: Time period in which requests can be sent
        in.
        :param bucket: Bucket of "tokens", in this case requests
        that is used for the ratelimiting algorithm.
        :param time_passed: The time passed between the last
        check and the current time.
        :return: Tuple of integer and boolean. Integer indicates
        the update bucket, and boolean specifies whether the the
        request was ratelimited or not.
        """

        bucket = bucket + time_passed * (requests / period)

        if bucket > requests:
            bucket = requests

        if bucket < 1:
            return bucket, True
        else:
            bucket = bucket - 1
            return bucket, False
