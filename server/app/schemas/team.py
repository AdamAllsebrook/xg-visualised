from pydantic import BaseModel


class TeamStripped(BaseModel):
    id: int
    name: str
    prefix : str = 'team'

    def create(fpl_team_json):
        return {
            'id': fpl_team_json['id'],
            'name': fpl_team_json['name'],
            'prefix': 'team'
        }


class Team(BaseModel):
    id: int
    name: str
    xG: float
    xGA: float
