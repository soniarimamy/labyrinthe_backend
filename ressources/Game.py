import os
import requests
from typing import List
from dotenv import load_dotenv
from helpers.Game import store_player_info, get_player_info
from schemas.Game import StartGameInput, MapDiscoveringOutput, StartGameOutput, MovePlayerInput, MovePlayerOutput

load_dotenv()


async def launch_game(start_game_input: StartGameInput):
    if not start_game_input or not start_game_input.player:
        return {"status": "failed", "msg": "body request not found", "data": None}
    else:
        base_url = os.getenv("LABYRINTHE_BACKEND_API")
        store_player_info(start_game_input.player)
        try:
            data = {"player": start_game_input.player}
            headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
            response: StartGameOutput = requests.post(url=f"{base_url}/start-game/", data=data, headers=headers).json()
            return {"status": "success", "msg": "game started", "data": response}
        except Exception as error:
            return {"status": "failed", "msg": f"failed to start the game, error: {str(error)}", "data": None}


async def display_map():
    try:
        game_player = get_player_info()
        base_url = os.getenv('LABYRINTHE_BACKEND_API')
        headers = {"Accept": "application/json"}
        map_response: List[MapDiscoveringOutput] = requests.get(url=f"{base_url}/{game_player}/discover/", headers=headers).json()
        return {"status": "success", "msg": "map shown successfully", "data": map_response}
    except Exception as error:
        return {"status": "failed", "msg": f"failed to discover map, error: {str(error)}", "data": None}


async def move_gamer(move_player_input: MovePlayerInput):
    if not move_player_input or not move_player_input.position_x or not move_player_input.position_y:
        return {"status": "failed", "msg": "body request not found", "data": None}
    else:
        try:
            game_player = get_player_info()
            base_url = os.getenv('LABYRINTHE_BACKEND_API', '')
            headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
            data = {"position_x": move_player_input.position_x, "position_y": move_player_input.position_y}
            move_response: MovePlayerOutput = requests.post(url=f"{base_url}/{game_player}/move/", data=data, headers=headers).json()
            return {"status": "success", "msg": "player is moved successfully", "data": move_response}
        except Exception as error:
            return {"status": "failed", "msg": f"failed to move, error: {str(error)}", "data": None}
