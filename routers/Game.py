from fastapi import *
from ressources.Game import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Labyrinth API",
    description="API for managing motion of player on a labyrinth field",
    version="1.0.0",
    contact={
        "name": "Rochel SONIARIMAMY",
        "email": "rochel.soniarimamy@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    })
app.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_headers=['*'],
    allow_origins=['*']
)


@app.get('/')
async def main():
    return {
        "msg": "Welcome to labyrinth Project",
        "info": [
            {"rest api": "Backend (REST API) started on http://localhost:8000/"},
            {"swagger (docs)": "http://localhost:8000/docs"},
            {"swagger (redoc)": "http://localhost:8000/redoc"}
        ]
    }


@app.post('/start')
async def start_game(start_game_input: StartGameInput):
    return await launch_game(start_game_input)


@app.get('/map')
async def discover_map():
    return await display_map()


@app.post('/move')
async def move_player(move_player_input: MovePlayerInput):
    return await move_gamer(move_player_input)
