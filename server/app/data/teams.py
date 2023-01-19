from fpl import FPL
import aiohttp


async def get_all_teams():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        teams = await fpl.get_teams(return_json=True)
    return teams

