from fastapi import APIRouter
from typing import Union

from app import schemas
from app.data.teams import get_team, get_fpl_team_matches

router = APIRouter()


@router.get('/{id}')#, response_model=Union[schemas.Team, None])
async def read_team(id: int):
    team = await get_team(id)
    return team


@router.get('/{id}/results')
async def read_results(id: int):
    matches = await get_fpl_team_matches(id)
    return matches['results']


@router.get('/{id}/fixtures')
async def read_fixtures(id: int):
    matches = await get_fpl_team_matches(id)
    return matches['fixtures']
