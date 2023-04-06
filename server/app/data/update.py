# Check if the cache needs updating every so often

from arq import cron
from typing import Any

from app.data.year import get_year
from app.data.players import get_all_players, get_player, get_player_matches, get_player_shots, get_all_shots_against_teams
from app.data.teams import get_all_teams, get_team_fixtures
from app.redis_utils import init_redis, reset_cache, is_cached


init_redis()


async def update_players(ctx: dict[Any, Any], *args: Any, **kwargs: Any) -> Any:
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


async def update_teams(ctx: dict[Any, Any], *args: Any, **kwargs: Any):
    year = await get_year()
    teams = await get_all_teams(year=year)
    for team in teams:
        await reset_cache(get_team_fixtures, team.title, year=year)


async def update_year(ctx: dict[Any, Any], *args: Any, **kwargs: Any):
    await reset_cache(get_year)


class WorkerSettings:
    cron_jobs = [
        cron(update_year, minute=[0, 30]),
        cron(update_players, minute=[0, 30]),
        cron(update_teams, minute=[0, 30]),
    ]
