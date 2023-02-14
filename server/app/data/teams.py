from fpl import FPL
import aiohttp
import csv
import os
from typing import Any, Union

from app.schemas import Team, Result, Fixture, TeamMatches
from app.data.year import get_year
from app.redis_utils import cache

dir_path = os.path.dirname(os.path.realpath(__file__))


@cache
async def get_all_teams() -> list[Team]:
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        teams: list[Any] = await fpl.get_teams(return_json=True)
    return [Team(**team) for team in teams]


@cache
async def get_team(id: int) -> Union[Team, None]:
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        try:
            team: Any = await fpl.get_team(id, return_json=True)
        except ValueError:
            return None
    return Team(**team)


@cache
async def get_all_fpl_matches() -> list[Union[Result, Fixture]]:
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        matches: Any = await fpl.get_fixtures(return_json=True)
    return [
        Result(**match) if match['finished'] else Fixture(**match) 
        for match in matches
        ]


@cache
async def get_fpl_team_matches(id: int) -> Union[TeamMatches, None]:
    matches = await get_all_fpl_matches()
    team_matches = [match for match in matches if match.team_h == id or match.team_a == id]
    if len(team_matches) == 0:
        return None
    team_results = [match for match in team_matches if isinstance(match, Result)]
    team_fixtures = [match for match in team_matches if isinstance(match, Fixture)]
    return TeamMatches(
        results=team_results,
        fixtures=team_fixtures
    )
