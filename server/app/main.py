import os
import uvicorn
import sys
from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every

from app.api_v1.api import api_router
from app.redis_utils import init_redis
from app.data.update import update_cache


host = sys.argv[1] if len(sys.argv) > 1 else '0.0.0.0'
port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000


def custom_generate_unique_id(route: APIRoute):
    return f'{route.tags[0]}-{route.name}'


SERVER_URL = os.getenv('SERVER_URL', 'http://localhost:8000')


app = FastAPI(
    servers=[{'url': SERVER_URL}],
    generate_unique_id_function=custom_generate_unique_id
)
app.include_router(api_router)

origins = [
    'http://localhost:5173',
    'localhost:5173',
    'http://xgvisualised.com',
    'http://www.xgvisualised.com',
    'https://xgvisualised.com',
    'https://www.xgvisualised.com',
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


@app.on_event("startup")
@repeat_every(seconds=60 * 60 * 24)
async def update_cache_task():
    print('updating cache')
    await update_cache()


if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)
