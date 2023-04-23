from fastapi import APIRouter, HTTPException
from typing import Union, List

from app import schemas
from app.data.players import get_player, get_player_matches, get_player_seasons, get_player_shots, get_all_shots_against_teams 
from app.data.teams import get_team_fixtures
from app.data.year import get_year


router = APIRouter()


@router.get('/all_shots', response_model=dict[str, list[schemas.SimpleShot]], tags=['player'])
async def read_all_shots(year: Union[int, None] = None):
    if year is None:
        year = await get_year()
    shots = await get_all_shots_against_teams(year)
    return shots


@router.get('/{id}', response_model=schemas.Player, tags=['player'])
async def read(id: int):
    player = await get_player(id)
    if player is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return player


@router.get('/{id}/seasons', response_model=List[schemas.Season], tags=['player'])
async def read_seasons(id: int):
    seasons = await get_player_seasons(id)
    if seasons is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return seasons


@router.get('/{id}/matches', response_model=List[schemas.Match], tags=['player'])
async def read_matches(id: int, year: Union[int, None] = None):
    if year is None:
        year = await get_year()
    matches = await get_player_matches(id, year=year)
    if matches is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return matches


@router.get('/{id}/fixtures', response_model=List[schemas.Fixture], tags=['player'])
async def read_fixtures(id: int, year: Union[int, None] = None):
    if year is None:
        year = await get_year()
    player = await get_player(id)
    if player is None:
        raise HTTPException(status_code=404, detail="Item not found")
    fixtures = await get_team_fixtures(player.team_title, year)
    if fixtures is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return fixtures


@router.get('/{id}/shots', response_model=List[schemas.Shot], tags=['player'])
async def read_shots(id: int, year: Union[int, None] = None):
    if year is None:
        year = await get_year()
    shots = await get_player_shots(id, year=year)
    if shots is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return shots
