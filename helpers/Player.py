

def store_player_info(game_player: str):
    with open('player.txt', 'w') as player:
        player.write(game_player)


def get_player_info():
    with open('player.txt', 'r') as player:
        return player.read()
