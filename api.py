import os
import requests
from dotenv import load_dotenv
from schemas import StartGameInput

load_dotenv()


def launch_game(start_game_input: StartGameInput):
    if not start_game_input or not start_game_input.player:
        return {"status": "failed", "msg": "payload not found", "data": None}
    else:
        base_url = os.getenv("LABYRINTHE_API")
        data = {"player": start_game_input.player}
        try:
            response = requests.post(f"{base_url}/start-game/", data=data, allow_redirects=False)
            return {"status": "success", "msg": "game started", "data": response.json()}
        except Exception as error:
            return {"status": "failed", "msg": f"failed to start the game, error: {error}", "data": None}
