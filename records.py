import json 
import pygame as pg
from pygame.font import Font
from button import Button


WIDTH = 960
HEIGHT = 640
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
def_font = pg.font.get_default_font()


def records(screen):
    screen.fill(WHITE)
    games = Button("Games", 32, WHITE, BLACK, RED, 100, 50,
                   (WIDTH//4, HEIGHT//3), screen)
    wins = Button("Wins", 32, WHITE, BLACK, GREEN, 100, 50,
                  (WIDTH//2, HEIGHT//3), screen)
    awppl = Button("AWPPL", 32, WHITE, BLACK, BLUE, 100, 50,
                   (3*WIDTH//4, HEIGHT//3), screen)
    home = Button("Home", 20, WHITE, WHITE, BLACK, 80, 50,
                  (WIDTH-100, 100), screen)
    games.change()
    ranking = return_top_5_games_played()


def _records_format(ranking):
    pass


def return_top_5_games_played():
    with open('records.json', 'r') as r:
        D = json.load(r)
    games = []
    for name in D:
        games.append([D[name]["Games"]["Played"], name])
    games.sort(reverse=True)
    return games[:5]


def return_top_5_games_won():
    with open('records.json', 'r') as r:
        D = json.load(r)
    wins = []
    for name in D:
        wins.append([D[name]["Games"]["Won"], name])
        wins.sort(reverse=True)
        return wins[:5]


def return_top_5_AWPPL():
    with open('records.json', 'r') as r:
        D = json.load(r)
    win_points = []
    for name in D:
        if D[name]["Games"]["Won"] > 0:
            win_points.append([round(D[name]["WPPL"]/D[name]["Games"]["Won"], 3), name])
        win_points.sort()
        return win_points[:5]


def update_records(winner, loser, moves, size):
    with open('records.json', 'r') as r:
        D = json.load(r)
    if winner not in D:
        D[winner] = {}
        D[winner]['Games'] = {}
        D[winner]['Games']['Played'] = 1
        D[winner]['Games']['Won'] = 1
        D[winner]['WPPL'] = ((moves+1)//2)/size
    else:
        D[winner]['Games']['Played'] += 1
        D[winner]['Games']['Won'] += 1
        D[winner]['WPPL'] += ((moves+1)//2)/size
    if loser not in D:
        D[loser] = {}
        D[loser]['Games'] = {}
        D[loser]['Games']['Played'] = 1
        D[loser]['Games']['Won'] = 0
        D[loser]['WPPL'] = 0
    else:
        D[loser]['Games']['Played'] += 1
    with open('records.json', 'w') as r:
        json.dump(D, r, indent = 4)
