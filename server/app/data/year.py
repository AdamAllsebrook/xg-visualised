from fpl import FPL
import aiohttp


async def get_year():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        gameweek_1 = await fpl.get_gameweek(1, return_json=True)
    return int(gameweek_1['deadline_time'][:4])


async def get_year_full():
    year = await get_year()
    return str(year) + '/' + str(year+1)[-2:]