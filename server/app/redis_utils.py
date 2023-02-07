# import asyncio
from redis import asyncio as aioredis
import functools
import pickle


def init_redis():
    global redis
    redis = aioredis.from_url("redis://localhost:6379")


def cache(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        reset_cache = 'reset_cache' in kwargs and kwargs['reset_cache']
        # avoid kwargs intended for decorator to be used in the cache key
        kwargs.pop('reset_cache', None)
        cache_key = func.__name__ + ':' + ':'.join([str(v) for v in list(args) + list(kwargs.values())])
        value = await redis.get(cache_key)
        if value is None or reset_cache:
            value = await func(*args, **kwargs)
            bytes_value = pickle.dumps(value)
            await redis.set(cache_key, bytes_value)
        else:
            value = pickle.loads(value)
        
        return value
    return wrapper
