from fastapi import APIRouter, HTTPException
from typing import Union, List

from app import schemas
from app.data.players import get_fpl_player, get_understat_player_matches, get_understat_player_seasons, get_understat_player_shots


router = APIRouter()


@router.get('/{id}', response_model=schemas.Player)
async def read_player(id: int):
    player = await get_fpl_player(id)
    if player is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return player


@router.get('/{id}/seasons', response_model=List[schemas.Season])
async def read_seasons(id: int):
    seasons = await get_understat_player_seasons(id)
    if seasons is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return seasons


@router.get('/{id}/matches', response_model=List[schemas.Match])
async def read_matches(id: int, year: Union[int, None] = None):
    matches = await get_understat_player_matches(id, year)
    if matches is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return list(reversed(matches))


@router.get('/{id}/shots', response_model=List[schemas.Shot])
async def read_shots(id: int, year: Union[int, None] = None):
    shots = await get_understat_player_shots(id, year=year)
    if shots is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return shots
