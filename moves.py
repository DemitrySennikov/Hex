import random
import pygame as pg
from team import Team as T


def move(team, hexes):
    if team.value == T.player.value:
        return _player_move(hexes)
    else:
        return _opponent_move(team, hexes)


def _opponent_move(team, hexes):
    game_over = False
    is_quit = False
    if team.value == T.random.value:
        hex = _random_move(hexes)
    elif team.value == T.other_player.value:
        hex, game_over, is_quit = _player_move(hexes)
    else:
        hex = _random_move(hexes)
    return hex, game_over, is_quit
    
    
def _player_move(hexes):
    game_over = False
    is_quit = False
    hex = None
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
            is_quit = True
        if event.type == pg.MOUSEBUTTONDOWN:
            s_x, s_y = event.pos
            hex = _define_nearest_hex(s_x, s_y, hexes)
    return hex, game_over, is_quit


def _define_nearest_hex(s_x, s_y, hexes):
    min_d = 1e9
    nearest = hexes[0][0]
    for x in range(len(hexes)):
        for y in range(len(hexes[0])):
            hex = hexes[x][y]
            current_d = _distance(s_x, s_y, hex)
            if current_d < min_d:
                min_d = current_d
                nearest = hex
    return nearest
    
    
def _distance(s_x, s_y, h):
    return ((s_x - h.center_x)**2 + (s_y - h.center_y)**2) ** 0.5
        

def _random_move(hexes):
    free_hexes = []
    for x in range(len(hexes)):
        for y in range(len(hexes[0])):
            hex = hexes[x][y]
            if hex.owner is None:
                free_hexes.append(hex)
    return random.choice(free_hexes)

'''
a = field.Field(5)
for _ in range(5):
    x, y = _AI_random_move(a)
    print(x, y)
'''