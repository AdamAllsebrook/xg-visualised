from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api_v1.api import api_router
from app.redis_utils import init_redis
from app.data.init import init_cache_values
from app.data.update import update_year, update_players, update_teams


app = FastAPI()
app.include_router(api_router)

origins = [
    'http://localhost:5173',
    'localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
async def init():
    init_redis()
    await init_cache_values()
