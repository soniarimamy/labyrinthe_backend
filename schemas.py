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
    dead: bool
    win: bool
    url_move: str
    url_discover: str
