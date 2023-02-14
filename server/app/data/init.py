# Call all functions to store the values in the cache

import asyncio
from tqdm import tqdm
from aiohttp.client_exceptions import ClientConnectorError

from app.data.year import *
from app.data.players import *
from app.data.teams import *
from app.redis_utils import init_redis


async def init_cache_values():
    for i in range(20):
        try:
            await get_year()

            players = await get_all_players()
            for player in tqdm(players):
                await get_fpl_player(player.id)
                await get_understat_player_matches(player.id, year=None)
                await get_understat_player_shots(player.id, year=None)
                await get_understat_player_seasons(player.id)

            teams = await get_all_teams()
            for team in tqdm(teams):
                await get_team(team.id)
                await get_fpl_team_matches(team.id)
        except ClientConnectorError:
            print(f'Connection error {i}/20.')

async def startup(ctx):
    init_redis()

async def shutdown(ctx):
    print('Finished!')


if __name__ == '__main__':
    init_redis()
    asyncio.run(init_cache_values())
 