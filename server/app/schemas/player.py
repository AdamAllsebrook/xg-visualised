from pydantic import BaseModel


class PlayerStripped(BaseModel):
    id: int
    name: str
    prefix : str = 'player'


class Player(BaseModel):
    id: int
    name: str
    xG: float
    xA: float
