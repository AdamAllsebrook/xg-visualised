# Check if the cache needs updating every so often

from arq import cron
from app.redis_utils import reset_cache

from app.data.year import *
from app.data.players import *
from app.data.teams import *
from app.redis_utils import init_redis


init_redis()


async def update_players(ctx: dict[Any, Any], *args: Any, **kwargs: Any) -> Any:
    players = await get_all_players()

    for player in players:
        await reset_cache(get_fpl_player, player.id)
        cached_understat_player = await get_understat_player_seasons(player.id)
        new_understat_player = reset_cache(get_understat_player_seasons, player.id)
        if cached_understat_player != new_understat_player:
            await reset_cache(get_understat_player_matches, player.id, year=None)
            await reset_cache(get_understat_player_shots, player.id, year=None)


async def update_teams(ctx: dict[Any, Any], *args: Any, **kwargs: Any):
    teams = await get_all_teams()

    do_update_matches = False
    for team in teams:
        cached_team = await get_team(team.id)
        new_team = await reset_cache(get_team, team.id)
        if cached_team != new_team:
            do_update_matches = True
    if do_update_matches:
        await reset_cache(get_all_fpl_matches)
        for team in teams:
            await reset_cache(get_fpl_team_matches, team.id)


async def update_year(ctx: dict[Any, Any], *args: Any, **kwargs: Any):
    await reset_cache(get_year)


class WorkerSettings:
    cron_jobs = [
        cron(update_year, minute={0, 30}),
        cron(update_players, minute={0, 30}),
        cron(update_teams, minute={0, 30}),
    ]
