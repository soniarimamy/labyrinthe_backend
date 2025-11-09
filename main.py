from api import *
from fastapi import FastAPI
from schemas import StartGameInput

app = FastAPI(version="1.0.0")


@app.get('/')
def main():
    return {"Welcome to labyrinth Project. This is Backend REST API"}


@app.post('/start')
def start_game(start_game_input: StartGameInput):
    return launch_game(start_game_input)


@app.get('/map')
def discover_map():
    return display_map()
