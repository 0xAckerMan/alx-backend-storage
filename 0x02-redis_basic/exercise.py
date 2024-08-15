#!/usr/bin/env python3
"""
contains the defination of redis
"""
import redis
from typing import Union
import uuid


class Cache:
    """
    Define a method for handling redis cache ops
    """

    def __init__(self) -> None:
        """
        Initialize redis client
        Attr:
            self._redis(redis.Redis): redis client
        """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in redis
        """
        key = str(uuid.uuid4())
        self.__redis.set(key, data)
        return key
