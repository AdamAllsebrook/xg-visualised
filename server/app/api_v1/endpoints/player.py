from fastapi import APIRouter
from typing import Union
from app import schemas

router = APIRouter()


@router.get('/{id}', response_model=Union[schemas.Player, None])
def get_player(id: int):
    return {'id': 1, 'name': 'Jordan Henderson', 'xG': 0.02, 'xA': 0.11}
