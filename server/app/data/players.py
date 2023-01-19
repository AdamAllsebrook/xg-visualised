from fpl import FPL
from understat import Understat
import aiohttp
import os
import csv

from app.data.year import get_year

dir_path = os.path.dirname(os.path.realpath(__file__))


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


async def get_fpl_player(id):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        player = await fpl.get_player(id, return_json=True)
    return player


async def get_understat_player_matches(fpl_id, year=None):
    id = get_understat_id(fpl_id)
    if year is None:
        year = await get_year()
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        matches = await understat.get_player_matches(id, {'season': str(year)})
    return matches


async def get_understat_player_seasons(fpl_id):
    id = get_understat_id(fpl_id)
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        grouped_stats = await understat.get_player_grouped_stats(id)
    return grouped_stats['season']


async def get_player(fpl_id):
    player = await get_fpl_player(fpl_id)

    return player


def get_id_index():
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


def get_understat_id(fpl_id):
    return get_id_index()[fpl_id]
