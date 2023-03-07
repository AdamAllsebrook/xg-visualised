from fastapi import APIRouter, HTTPException
from typing import Union

from app import schemas
from app.data.teams import get_all_teams
from app.data.year import get_year

router = APIRouter()


@router.get('/all', response_model=list[schemas.Team], tags=['team'])
async def read_all(year: Union[int, None] = None):
    if year is None:
        year = await get_year()
    teams = await get_all_teams(year=year)
    return teams


# @router.get('/{id}', response_model=schemas.Team, tags=['team'])
# async def read(id: int):
#     team = await get_team(id)
#     if team is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return team


# @router.get('/{id}/results', response_model=list[schemas.Result], tags=['team'])
# async def read_results(id: int):
#     matches = await get_fpl_team_matches(id)
#     if matches is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return matches.results


# @router.get('/{id}/fixtures', response_model=list[schemas.Fixture], tags=['team'])
# async def read_fixtures(id: int):
#     matches = await get_fpl_team_matches(id)
#     if matches is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return matches.fixtures
