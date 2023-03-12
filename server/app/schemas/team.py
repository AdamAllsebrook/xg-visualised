from pydantic import BaseModel
from datetime import datetime
from typing import Union, Literal


class Team(BaseModel):
    id: int
    title: str
    xG: float
    xGA: float
    games: int


class FixtureTeam(BaseModel):
    id: int
    title: str
    short_title: str


class Fixture(BaseModel):
    id: int
    side: Union[Literal['h'], Literal['a']]
    h: FixtureTeam
    a: FixtureTeam
    datetime: datetime


# class Result(BaseModel):
#     id: int
#     event: Union[int, None]
#     kickoff_time: Union[datetime, None]
#     team_h: int
#     team_a: int
#     team_h_score: int
#     team_a_score: int
#     finished: bool


# class Fixture(BaseModel):
#     id: int
#     event: Union[int, None]
#     kickoff_time: Union[datetime, None]
#     team_h: int
#     team_a: int


# class TeamMatches(BaseModel):
#     results: list[Result]
#     fixtures: list[Fixture]
