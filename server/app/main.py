from typing import Union
from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.models import Server

from app.api_v1.api import api_router
from app.redis_utils import init_redis


def custom_generate_unique_id(route: APIRoute):
    return f'{route.tags[0]}-{route.name}'


app = FastAPI(
    servers=[{'url': 'http://localhost:8000'}], 
    generate_unique_id_function=custom_generate_unique_id
    )
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
