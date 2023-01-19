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
