import os
from redis import asyncio as aioredis
import functools
import pickle
from typing import Callable, Any, ParamSpec, TypeVar, Awaitable


REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')


P = ParamSpec('P')
R = TypeVar('R')


def generate_cache_key(func: Callable[P, Awaitable[R]], *args: P.args, **kwargs: P.kwargs) -> str:
    cache_key = func.__name__ + ':' + ':'.join([str(v) for v in list(args) + list(kwargs.values())])
    return cache_key


def init_redis():
    global redis
    redis = aioredis.from_url(REDIS_URL)


def cache(func: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]:
    @functools.wraps(func)
    async def wrapper(*args: P.args, **kwargs: P.kwargs):
        cache_key = generate_cache_key(func, *args, **kwargs)
        value = await redis.get(cache_key)
        if value is None:
            value = await func(*args, **kwargs)
            bytes_value = pickle.dumps(value)
            await redis.set(cache_key, bytes_value)
        else:
            value = pickle.loads(value)
        
        return value
    return wrapper


async def reset_cache(func: Callable[P, Awaitable[R]], *args: P.args, **kwargs: P.kwargs) -> Awaitable[R]:
    cache_key = generate_cache_key(func, *args, **kwargs)
    await redis.delete(cache_key)
    return await func(*args, **kwargs)


async def is_cached(func: Callable[P, Awaitable[R]], *args: P.args, **kwargs: P.kwargs) -> bool:
    cache_key = generate_cache_key(func, *args, **kwargs)
    return await redis.exists(cache_key)
