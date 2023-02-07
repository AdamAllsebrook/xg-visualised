from fpl import FPL
import aiohttp
import csv
import os

from app.data.year import get_year
from app.redis_utils import cache

dir_path = os.path.dirname(os.path.realpath(__file__))


@cache
async def get_all_teams():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        teams = await fpl.get_teams(return_json=True)
    return teams


@cache
async def get_team(id):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        team = await fpl.get_team(id, return_json=True)
    return team


@cache
async def get_all_fpl_matches():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        matches = await fpl.get_fixtures(return_json=True)
    return matches


@cache
async def get_fpl_team_matches(id):
    matches = await get_all_fpl_matches()
    team_matches = [match for match in matches if match['team_h'] == id or match['team_a'] == id]
    team_results = [match for match in team_matches if match['finished'] == True]
    team_fixtures = [match for match in team_matches if match['finished'] == False]
    return {
        'results': team_results,
        'fixtures': team_fixtures
    }
