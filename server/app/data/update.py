# Check if the cache needs updating every so often

from arq import cron

from app.data.year import *
from app.data.players import *
from app.data.teams import *
from app.redis_utils import init_redis


init_redis()


async def update_players(ctx):
    players = await get_all_players()

    for player in players:
        await get_fpl_player(player['id'], reset_cache=True)
        cached_understat_player = await get_understat_player_seasons(player['id'])
        new_understat_player = await get_understat_player_seasons(player['id'], reset_cache=True)
        if cached_understat_player != new_understat_player:
            await get_understat_player_matches(player['id'], year=None, reset_cache=True)


async def update_teams(ctx):
    teams = await get_all_teams()

    do_update_matches = False
    for team in teams:
        cached_team = await get_team(team['id'])
        new_team = await get_team(team['id'], reset_cache=True)
        if cached_team != new_team:
            do_update_matches = True
    if do_update_matches:
        await get_all_fpl_matches(reset_cache=True)
        for team in teams:
            await get_fpl_team_matches(team['id'], reset_cache=True)


async def update_year(ctx):
    await get_year(reset_cache=True)


class WorkerSettings:
    cron_jobs = [
        cron(update_year, minute={0, 30}),
        cron(update_players, minute={0, 30}),
        cron(update_teams, minute={0, 30}),
    ]
