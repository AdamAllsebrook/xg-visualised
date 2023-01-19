from pydantic import BaseModel


class PlayerStripped(BaseModel):
    id: int
    name: str
    prefix: str = 'player'

    def create(fpl_player_json):
        return {
            'id': fpl_player_json['id'],
            'name': fpl_player_json['first_name'] + ' ' + fpl_player_json['second_name'],
            'prefix': 'player'
        }


class Player(BaseModel):
    id: int
    name: str
    xG: float
    xA: float
