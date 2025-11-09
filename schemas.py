from typing import Any
from pydantic import BaseModel


class BasicResponse(BaseModel):
    status: str
    msg: str
    data: Any


class StartGameInput(BaseModel):
    player: str


class StartGameOutput(BaseModel):
    player: str
    message: str
    position_x: int
    position_y: int
    dead: bool = False
    win: bool = False
    url_move: str
    url_discover: str


class MapDiscoveringOutput(BaseModel):
    x: int
    y: int
    move: bool = False
    value = 'wall' or 'path' or 'trap' or 'home' or 'stop'
