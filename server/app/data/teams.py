from fpl import FPL
from understat import Understat
import aiohttp
import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

from app.data.year import get_year


async def get_all_teams():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        teams = await fpl.get_teams(return_json=True)
    return teams


async def get_team(id):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        team = await fpl.get_team(id, return_json=True)
    return team


async def get_all_fpl_matches():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        matches = await fpl.get_fixtures(return_json=True)
    return matches


async def get_fpl_team_matches(id):
    matches = await get_all_fpl_matches()
    team_matches = [match for match in matches if match['team_h'] == id or match['team_a'] == id]
    team_results = [match for match in team_matches if match['finished'] == True]
    team_fixtures = [match for match in team_matches if match['finished'] == False]
    return {
        'results': team_results,
        'fixtures': team_fixtures
    }


async def get_understat_team_matches(id, year=None):
    team_name = await get_understat_team_name(id)
    if year is None:
        year = await get_year()
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        matches = await understat.get_team_results(team_name, {'season': str(year)})
    return matches


async def get_teams_index():
    team_names_index = {}
    with open(dir_path + '/index/team_index.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, row in enumerate(reader):
            if i > 0:
                if len(row[1]) == 0:
                    team_names_index[row[0]] = row[0]
                else:
                    team_names_index[row[0]] = row[1]

    teams = await get_all_teams()
    team_ids_index = {}
    for team in teams:
        team_ids_index[team['id']] = team_names_index[team['name']]

    return team_names_index, team_ids_index


async def get_understat_team_name(fpl_id):
    _, teams_index = await get_teams_index()
    return teams_index[fpl_id]
