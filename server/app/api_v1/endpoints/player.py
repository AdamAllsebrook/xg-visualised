from fastapi import APIRouter, HTTPException
from typing import Union

from app import schemas
from app.data.players import get_fpl_player, get_understat_player_matches, get_understat_player_seasons

router = APIRouter()


@router.get('/{id}')#, response_model=Union[schemas.Player, None])
async def read_player(id: int):
    try:
        player = await get_fpl_player(id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Item not found")
        
    return player


@router.get('/{id}/seasons')
async def read_seasons(id: int):
    seasons = await get_understat_player_seasons(id)
    return seasons


@router.get('/{id}/matches')
async def read_matches(id: int, year: Union[str, None] = None):
    matches = await get_understat_player_matches(id, year)
    return list(reversed(matches))
