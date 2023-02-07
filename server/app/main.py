from typing import Union
from fastapi import FastAPI

from app.api_v1.api import api_router
from app.redis_utils import init_redis
from app.data.init import init_cache_values
from app.data.update import update_year, update_players, update_teams


app = FastAPI()
app.include_router(api_router)


@app.on_event('startup')
async def init():
    init_redis()
    await init_cache_values()
