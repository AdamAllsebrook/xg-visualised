from fastapi import APIRouter
from typing import Union, List

from app.data.players import get_all_players
from app import schemas
from app.data.year import get_year

router = APIRouter()


@router.get('/', response_model=List[Union[schemas.PlayerSearch, schemas.TeamSearch]], tags=['items'])
async def read(year: Union[int, None] = None):
    if year is None:
        year = await get_year()
    players = await get_all_players(year)
    players = [
        schemas.PlayerSearch(
            name=player.player_name,
            **player.dict()
        )
        for player in players.values()
    ]
    # teams = await get_all_teams()
    # teams = [schemas.TeamSearch(**team.dict()) for team in teams]
    return players
