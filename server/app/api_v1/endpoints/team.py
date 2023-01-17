from fastapi import APIRouter
from typing import Union
from app import schemas

router = APIRouter()


@router.get('/{id}', response_model=Union[schemas.Team, None])
def get_player(id: int):
    return {'id': 1, 'name': 'Crystal Palace', 'xG': 2.1, 'xGA': 0.96}
