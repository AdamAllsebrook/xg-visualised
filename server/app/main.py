import os
import asyncio
import uvicorn
import logging
import sys
from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware

from app.api_v1.api import api_router
from app.redis_utils import init_redis
from scheduler import app as app_rocketry


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


class Server(uvicorn.Server):
    """
    Customized uvicorn.Server

    Uvicorn server overrides signals and we need to include
    Rocketry to the signals.
    """

    def handle_exit(self, sig: int, frame) -> None:
        app_rocketry.session.shut_down()
        return super().handle_exit(sig, frame)


async def main():
    "Run Rocketry and FastAPI"
    server = Server(config=uvicorn.Config(app, host=host, port=port, workers=1, loop="asyncio"))

    api = asyncio.create_task(server.serve())
    sched = asyncio.create_task(app_rocketry.serve())

    await asyncio.wait([sched, api])

if __name__ == "__main__":
    # Print Rocketry's logs to terminal
    logger = logging.getLogger("rocketry.task")
    logger.addHandler(logging.StreamHandler())

    # Run both applications
    asyncio.run(main())
