from pydantic import BaseModel
from typing import Union, Literal
from datetime import date, datetime


class Player(BaseModel):
    id: int
    first_name: str
    second_name: str
    web_name: str
    team: int


class Season(BaseModel):
    games: int
    goals: int
    shots: int
    time: int
    assists: int
    xG: float
    xA: float
    season: int
    team: str


class Match(BaseModel):
    id: int
    goals: int
    shots: int
    time: int
    time_started: int
    assists: int
    xG: float
    xA: float
    h_team: str
    a_team: str
    h_goals: int
    a_goals: int
    h_a: Union[Literal['h'], Literal['a']]
    date: date


class Shot(BaseModel):
    id: int
    match_id: int
    minute: int
    xG: float
    player: str
    player_assisted: Union[str, None]
    season: int
    situation: str # TODO enum
    shotType: str # TODO enum
    result: str # TODO enum
    X: float
    Y: float
    h_team: str
    a_team: str
    h_goals: int
    a_goals: int
    h_a: Union[Literal['h'], Literal['a']]
    date: datetime

