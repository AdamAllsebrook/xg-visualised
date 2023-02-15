from pydantic import BaseModel
from typing import Literal, Union


class Search(BaseModel):
    id: int
    name: str
    prefix: Union[Literal['player'], Literal['team']]

class PlayerSearch(Search):
    first_name: str
    second_name: str
    web_name: str
    prefix: str = 'player'

class TeamSearch(Search):
    prefix: str = 'team'
