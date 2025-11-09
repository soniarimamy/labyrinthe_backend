from api import *
from fastapi import FastAPI
from schemas import StartGameInput

app = FastAPI()


@app.post('/start')
def start_game(start_game_input: StartGameInput):
    return launch_game(start_game_input)
