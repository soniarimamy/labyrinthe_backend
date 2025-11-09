import os
import requests
from typing import List
from dotenv import load_dotenv
from helpers.Player import store_player_info, get_player_info
from schemas import StartGameInput, MapDiscoveringOutput, StartGameOutput

load_dotenv()


def launch_game(start_game_input: StartGameInput):
    if not start_game_input or not start_game_input.player:
        return {"status": "failed", "msg": "payload not found", "data": None}
    else:
        base_url = os.getenv("LABYRINTHE_BACKEND_API")
        data = {"player": start_game_input.player}
        store_player_info(start_game_input.player)
        try:
            response: StartGameOutput = requests.post(f"{base_url}/start-game/", data=data, allow_redirects=False).json()
            return {"status": "success", "msg": "game started", "data": response}
        except Exception as error:
            return {"status": "failed", "msg": f"failed to start the game, error: {str(error)}", "data": None}


def display_map():
    try:
        game_player = get_player_info()
        base_url = os.getenv('LABYRINTHE_BACKEND_API')
        map_response: List[MapDiscoveringOutput] = requests.get(f"{base_url}/{game_player}/discover/", allow_redirects=False).json()
        return {"status": "success", "msg": "map shown successfully", "data": map_response}
    except Exception as error:
        return {"status": "failed", "msg": f"failed to discover map, error: {str(error)}", "data": None}
