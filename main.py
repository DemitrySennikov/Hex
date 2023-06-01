from game_logic import game
from team import Team as T


def main():
    n = 5
    op = T.random
    game(n, op)
    op = T.other_player
    game(n, op)
    
    
if __name__ == '__main__':
    main()
