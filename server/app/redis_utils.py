# import asyncio
from redis import asyncio as aioredis
import functools
import pickle
from typing import Callable, Any, ParamSpec, TypeVar, Awaitable


P = ParamSpec('P')
R = TypeVar('R')

def init_redis():
    global redis
    redis = aioredis.from_url("redis://localhost:6379")


def cache(func: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]:
    @functools.wraps(func)
    async def wrapper(*args: P.args, **kwargs: P.kwargs):
        cache_key = func.__name__ + ':' + ':'.join([str(v) for v in list(args) + list(kwargs.values())])
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
    cache_key = func.__name__ + ':' + ':'.join([str(v) for v in list(args) + list(kwargs.values())])
    await redis.delete(cache_key)
    return func(*args, **kwargs)
