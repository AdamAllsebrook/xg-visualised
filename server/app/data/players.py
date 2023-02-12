from fpl import FPL
from understat import Understat
import aiohttp
import os
import csv

from app.data.year import get_year
from app.redis_utils import cache

dir_path = os.path.dirname(os.path.realpath(__file__))


@cache
async def get_all_players():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players(return_json=True)
    players = [
        player
        for player in players
        if player['status'] != 'u'
    ]
    return players


@cache
async def get_fpl_player(fpl_id):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        player = await fpl.get_player(fpl_id, return_json=True)
    return player


@cache
async def get_understat_player_matches(fpl_id, year=None):
    id = await get_understat_id(fpl_id)
    if id == -1:
        return None
    if year is None:
        year = await get_year()
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        matches = await understat.get_player_matches(id, {'season': str(year)})
        # get which team the player played for in each match
        for match in matches:
            match_players = await understat.get_match_players(match['id'])
            # players who played for the home team
            h_ids = [player['player_id'] for player in match_players['h'].values()]
            if id in h_ids:
                match['h_a'] = 'h'
            else:
                match['h_a'] = 'a'
    return matches


@cache
async def get_understat_player_seasons(fpl_id):
    id = await get_understat_id(fpl_id)
    if id == -1:
        return None
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        grouped_stats = await understat.get_player_grouped_stats(id)
    return grouped_stats['season']


@cache
async def get_id_index():
    id_index = {}
    with open(os.path.join(dir_path, 'index', 'id_dict.csv'), encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = None
        for row in reader:
            if header is None:
                header = row
                continue
            id_index[int(row[header.index('FPL_ID')])
                     ] = row[header.index('Understat_ID')]
    return id_index


async def get_understat_id(fpl_id):
    index = await get_id_index()
    if fpl_id in index:
        return index[fpl_id]
    else:
        return -1
