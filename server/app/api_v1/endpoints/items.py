from fastapi import APIRouter
from typing import Union, List

from app.data.players import get_all_players
from app.data.teams import get_all_teams
from app import schemas

router = APIRouter()


@router.get('/', response_model=List[Union[schemas.PlayerSearch, schemas.TeamSearch]], tags=['items'])
async def read():
    players = await get_all_players()
    players = [schemas.PlayerSearch(**player.dict()) for player in players]
    teams = await get_all_teams()
    teams = [schemas.TeamSearch(**team.dict()) for team in teams]
    return players + teams
