from pydantic import BaseModel


class TeamStripped(BaseModel):
    id: int
    name: str
    prefix : str = 'team'



class Team(BaseModel):
    id: int
    name: str
    xG: float
    xGA: float
