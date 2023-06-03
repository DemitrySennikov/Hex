from game_logic import game
from team import Team as T


def main():
    n = 5
    player_name = "Player1"
    op_name = "Random"
    op = T.random
    game(n, player_name, op, op_name)
    op = T.other_player
    op_name = "Player2"
    game(n, player_name, op, op_name)
    
    
if __name__ == '__main__':
    main()
