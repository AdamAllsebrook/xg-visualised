from fpl import FPL
import aiohttp
from typing import Any

from app.redis_utils import cache


@cache
async def get_year() -> int:
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        gameweek_1: Any = await fpl.get_gameweek(1, return_json=True)
    return int(gameweek_1['deadline_time'][:4])


async def get_year_full() -> str:
    year = await get_year()
    return str(year) + '/' + str(year+1)[-2:]