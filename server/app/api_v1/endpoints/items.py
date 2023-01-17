from fastapi import APIRouter
from typing import Union, List
from app import schemas

router = APIRouter()


@router.get('/', response_model=List[Union[schemas.PlayerStripped, schemas.TeamStripped]])
def read_items():
    return [{'id': 1, 'name': 'Kevin De Bruyne', 'prefix': 'player'}]
