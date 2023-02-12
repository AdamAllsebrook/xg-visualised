from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api_v1.api import api_router
from app.redis_utils import init_redis


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
