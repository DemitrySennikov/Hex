import random
import pygame as pg
from team import Team as T
from field import Field


def move(team, field, home):
    if team.value == T.player.value:
        return _player_move(field.hexes, home)
    else:
        return _opponent_move(team, field, home)


def _opponent_move(team, field, home):
    game_over = False
    is_menu = False
    is_quit = False
    if team.value == T.random.value:
        hex = _random_move(field.hexes)
    elif team.value == T.other_player.value:
        hex, game_over, is_menu, is_quit = _player_move(field.hexes, home)
    else:
        hex = _AI_move(field)
    return hex, game_over, is_menu, is_quit
    
    
def _player_move(hexes, home):
    game_over = False
    is_quit = False
    is_menu = False
    hex = None
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
            is_menu = True
            is_quit = True
        if event.type == pg.MOUSEBUTTONDOWN:
            s_x, s_y = event.pos
            if home.is_pressed((s_x, s_y)):
                hex = None
                game_over = True
                is_menu = True
            else:
                hex = _define_nearest_hex(s_x, s_y, hexes)
    return hex, game_over, is_menu, is_quit


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


def _AI_move(field: Field):
    hexes, is_attack, d = field.AI_solver()
    if is_attack and d <=4 or not is_attack and d <= 5:
        return random.choice(hexes)
    count = 0
    for hex_row in field.hexes:
        for hex in hex_row:
            if hex.owner == T.AI:
                count += 1
    if count%2 == 0:
        return random.choice(hexes)
    return _random_move(field.hexes)
