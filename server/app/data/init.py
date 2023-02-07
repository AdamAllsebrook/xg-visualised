# Call all functions to store the values in the cache

from tqdm import tqdm
# from aiohttp.client_exceptions import ClientConnectorError

from app.data.year import *
from app.data.players import *
from app.data.teams import *


async def init_cache_values():
    await get_year()

    players = await get_all_players()
    for player in tqdm(players):
        await get_fpl_player(player['id'])
        await get_understat_player_matches(player['id'])
        await get_understat_player_seasons(player['id'])

    teams = await get_all_teams()
    for team in tqdm(teams):
        await get_team(team['id'])
        await get_fpl_team_matches(team['id'])
