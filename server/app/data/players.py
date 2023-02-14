from dataclasses import dataclass
from fpl import FPL
from understat import Understat
import aiohttp
import os
import csv
from typing import Any, Union

from app.schemas import Player, Match, Season, Shot
from app.data.year import get_year
from app.redis_utils import cache


@cache
async def get_all_players() -> list[Player]:
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        fpl_players: list[Any] = await fpl.get_players(return_json=True)
    players = [
        Player(**player)
        for player in fpl_players
        if player['status'] != 'u'
    ]
    return players


@cache
async def get_fpl_player(fpl_id: int) -> Union[Player, None]:
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        try:
            fpl_player: Any = await fpl.get_player(fpl_id, return_json=True)
        except ValueError:
            return None
    return Player(**fpl_player)


@cache
async def get_understat_player_matches(fpl_id: int, year: Union[int, None] = None) -> Union[list[Match], None]:
    id = await get_understat_id(fpl_id)
    if id == -1:
        return None

    if year is None:
        year = await get_year()
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        matches: list[Any] = await understat.get_player_matches(id, {'season': str(year)})
        # find out which team the player played for in each match
        for match in matches:
            match_players: Any = await understat.get_match_players(match['id'])
            # players who played for the home team
            h_ids: list[int] = [player['player_id']
                                for player in match_players['h'].values()]
            if id in h_ids:
                match['h_a'] = 'h'
            else:
                match['h_a'] = 'a'
    return [Match(**match) for match in matches]


@cache
async def get_understat_player_shots(fpl_id: int, year: Union[int, None] = None) -> Union[list[Shot], None]:
    id = await get_understat_id(fpl_id)
    if id == -1:
        return None

    if year is None:
        year = await get_year()
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        shots = await understat.get_player_shots(id, {'season': str(year)})
    return [Shot(**shot) for shot in shots]


@cache
async def get_understat_player_seasons(fpl_id: int) -> Union[list[Season], None]:
    id = await get_understat_id(fpl_id)
    if id == -1:
        return None

    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        grouped_stats: Any = await understat.get_player_grouped_stats(id)
    return [Season(**season) for season in grouped_stats['season']]


@cache
async def get_id_index() -> dict[int, int]:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    id_index: dict[int, int] = {}
    with open(os.path.join(dir_path, 'index', 'id_dict.csv'), encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header: Union[None, list[str]] = None
        for row in reader:
            if header is None:
                header = row
                continue
            fpl_id = int(row[header.index('FPL_ID')])
            understat_id = int(row[header.index('Understat_ID')])
            id_index[fpl_id] = understat_id
    return id_index


async def get_understat_id(fpl_id: int) -> int:
    index = await get_id_index()
    if fpl_id in index:
        return index[fpl_id]
    else:
        return -1
