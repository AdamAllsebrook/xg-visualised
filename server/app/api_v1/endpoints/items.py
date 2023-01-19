from fastapi import APIRouter
from typing import Union, List

from app.data.players import get_all_players
from app.data.teams import get_all_teams
from app import schemas

router = APIRouter()


@router.get('/', response_model=List[Union[schemas.PlayerStripped, schemas.TeamStripped]])
async def read_items():
    players = await get_all_players()
    players = list(map(schemas.PlayerStripped.create, players))
    teams = await get_all_teams()
    teams = list(map(schemas.TeamStripped.create, teams))
    return players + teams
