# Check if the cache needs updating every so often
import os
import asyncio
import time
from app.data.year import get_year
from app.data.players import get_all_players, get_player, get_player_matches, get_player_shots, get_all_shots_against_teams
from app.data.teams import get_all_teams, get_team_fixtures
from app.redis_utils import init_redis, reset_cache, is_cached


async def update_players():
    players = await get_all_players()
    year = await get_year()

    for id, player in players.items():
        is_player_cached = await is_cached(get_player, id)
        cached_understat_player = await get_player(id)
        new_understat_player = await reset_cache(get_player, id)
        if not is_player_cached or cached_understat_player != new_understat_player:
            print(f'updating data for {player.player_name} ({"no cache existed" if not is_player_cached else "cache was out of date"})')
            await reset_cache(get_player_matches, id, year=year)
            await reset_cache(get_player_shots, id, year=year)

    await get_all_shots_against_teams(year=year)


async def update_teams():
    year = await get_year()
    teams = await get_all_teams(year=year)
    for team in teams:
        await reset_cache(get_team_fixtures, team.title, year=year)


async def update_year():
    await reset_cache(get_year)


async def update_cache():
    interval = int(os.getenv('CACHE_UPDATE_INTERVAL', 60 * 60 * 24))
    print(f'Starting cache with interval {interval} seconds')
    while True:
        init_redis()
        await update_year()
        await update_players()
        await update_teams()
        print(f'Completed cache update at {time.strftime("%H:%M:%S")}, interval is {interval} seconds')
        time.sleep(interval)

