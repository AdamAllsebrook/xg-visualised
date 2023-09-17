# Check if the cache needs updating every so often
import os
import asyncio
import time
from app.data.year import get_year
from app.data.players import get_all_players, get_player, get_player_matches, get_player_shots, get_all_shots_against_teams
from app.data.teams import get_all_teams, get_team_fixtures
from app.redis_utils import init_redis, reset_cache, is_cached


async def update_players():
    year = await get_year()
    players = await reset_cache(get_all_players, year)

    for id, player in players.items():
        is_player_cached = await is_cached(get_player, id, year)
        cached_player = await get_player(id, year)
        if not is_player_cached or cached_player != player:
            reason = 'cache was out of date' if is_player_cached else 'no cache existed'
            await reset_cache(get_player, id, year)
            await reset_cache(get_player_matches, id, year)
            await reset_cache(get_player_shots, id, year)
            print(f'{id} {player.player_name} updated: {reason}')
        else:
            print(f'{id} {player.player_name} not updated')

    await get_all_shots_against_teams(year)


async def update_teams():
    year = await get_year()
    teams = await reset_cache(get_all_teams, year)
    for team in teams:
        await reset_cache(get_team_fixtures, team.title, year)


async def update_year():
    await reset_cache(get_year)


async def update_cache():
    print(f'Updating cache at {time.strftime("%H:%M:%S")}')
    init_redis()
    await update_year()
    await update_players()
    print('Completed player update')
    await update_teams()
    print('Completed team update')
    print(f'Completed cache update at {time.strftime("%H:%M:%S")}')
