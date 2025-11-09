import pytest
from routers import Game
from fastapi.testclient import TestClient


client = TestClient(Game.app)


@pytest.mark.asyncio
async def test_main_root():
    response = client.get("/")
    assert response.status_code == 200
    json_data = response.json()
    assert "msg" in json_data
    assert json_data["msg"] == "Welcome to labyrinth Project"


@pytest.mark.asyncio
async def test_start_game_success(monkeypatch):
    async def fake_launch_game(start_game_input):
        return {"status": "success", "msg": "game started", "data": {"player": start_game_input.player}}
    monkeypatch.setattr("routers.Game.launch_game", fake_launch_game)
    response = client.post("/start", json={"player": "Rochel"})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "success"
    assert json_data["data"]["player"] == "Rochel"


@pytest.mark.asyncio
async def test_start_game_failure(monkeypatch):
    async def fake_launch_game(start_game_input):
        return {"status": "failed", "msg": "body request not found", "data": None}
    monkeypatch.setattr("routers.Game.launch_game", fake_launch_game)
    response = client.post("/start", json={"player": ""})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "failed"


@pytest.mark.asyncio
async def test_start_game_invalid_body():
    response = client.post("/start", json={})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_discover_map(monkeypatch):
    async def fake_display_map():
        return {"status": "success", "msg": "map shown successfully", "data": [{"x": 0, "y": 0, "value": "path"}]}

    monkeypatch.setattr("routers.Game.display_map", fake_display_map)

    response = client.get("/map")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "success"
    assert isinstance(json_data["data"], list)


@pytest.mark.asyncio
async def test_move_player(monkeypatch):
    async def fake_move_gamer(move_player_input):
        return {
            "status": "success",
            "msg": "player is moved successfully",
            "data": {
                "new_position": [move_player_input.position_x, move_player_input.position_y],
                "message": "Player moved!"
            }
        }

    monkeypatch.setattr("routers.Game.move_gamer", fake_move_gamer)

    response = client.post("/move", json={"position_x": 2, "position_y": 3})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "success"
    assert json_data["data"]["new_position"] == [2, 3]
