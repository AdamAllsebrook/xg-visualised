from pydantic import BaseModel
from typing import Literal, Union


class Search(BaseModel):
    id: int
    name: str
    prefix: Union[Literal['player'], Literal['team']]

class PlayerSearch(Search):
    prefix: str = 'player'

class TeamSearch(Search):
    prefix: str = 'team'
