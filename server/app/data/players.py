from understat import Understat
import aiohttp
import os
import csv
from typing import Any, Union

from app.schemas import Player, Match, Season, Shot
from app.data.year import get_year
from app.redis_utils import cache


@cache
async def get_all_players() -> dict[int, Player]:
    year = await get_year()
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        understat_players = await understat.get_league_players('epl', year)
    players: dict[int, Player] = {
        int(player['id']): Player(**player)
        for player in understat_players
    }
    return players


@cache
async def get_player(id: int) -> Union[Player, None]:
    try:
        player: Player = (await get_all_players())[id]
    except KeyError:
        return None
    return player


@cache
async def get_player_matches(id: int, year: Union[int, None] = None) -> Union[list[Match], None]:
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
            if str(id) in h_ids:
                match['h_a'] = 'h'
            else:
                match['h_a'] = 'a'

            # get when the player started
            player_roster_id: str = '-1'
            for key, match_data in match_players[match['h_a']].items():
                if match_data['player_id'] == str(id):
                    player_roster_id = key
            if player_roster_id == '-1':
                match['time_started'] = -1
            else:
                # get the time started by summing the minutes of every player in the chain of subsitutes preceding this player
                time_started: int = 0
                player_roster_id = match_players[match['h_a']][player_roster_id]['roster_out']
                while player_roster_id != '0':
                    time_started += int(match_players[match['h_a']][player_roster_id]['time'])
                    player_roster_id = match_players[match['h_a']][player_roster_id]['roster_out']
                match['time_started'] = time_started

    return [Match(**match) for match in matches]


@cache
async def get_player_shots(id: int, year: Union[int, None] = None) -> Union[list[Shot], None]:
    if year is None:
        year = await get_year()
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        shots = await understat.get_player_shots(id, {'season': str(year)})
    return [Shot(**shot) for shot in shots]


@cache
async def get_player_seasons(id: int) -> Union[list[Season], None]:
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        grouped_stats: Any = await understat.get_player_grouped_stats(id)
    return [Season(**season) for season in grouped_stats['season']]
