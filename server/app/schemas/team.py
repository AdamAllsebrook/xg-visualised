from pydantic import BaseModel
from datetime import datetime
from typing import Union


class TeamSearch(BaseModel):
    id: int
    name: str
    prefix : str = 'team'


class Team(BaseModel):
    id: int
    name: str


class Result(BaseModel):
    id: int
    event: Union[int, None]
    kickoff_time: Union[datetime, None]
    team_h: int
    team_a: int
    team_h_score: int
    team_a_score: int
    finished: bool


class Fixture(BaseModel):
    id: int
    event: Union[int, None]
    kickoff_time: Union[datetime, None]
    team_h: int
    team_a: int


class TeamMatches(BaseModel):
    results: list[Result]
    fixtures: list[Fixture]
