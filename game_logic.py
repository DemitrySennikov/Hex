import pygame as pg
import hex as h
import field as f
from team import Team as T
from math import sin, pi
from moves import opponent_move, player_move


WIDTH = 960
HEIGHT = 640
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)


def game(n, op):
    field = f.Field(n, op)
    screen = _init_game()
    hexes = _init_hexes(n, screen, op)
    game_over = False
    is_quit = False
    current_team = T.player
    while not game_over:
        if current_team.value == T.player.value:
            hex, game_over, is_quit = player_move(hexes)
        else:
            hex, game_over, is_quit = opponent_move(current_team, hexes)
        if hex is None:
            continue
        correct = field.try_move(current_team, hex.x, hex.y)
        if correct:
            hex.assign(current_team, screen)
            if field.is_team_win(current_team):
                game_over = True
                if current_team.value == T.player.value:
                    screen.fill(BLUE)
                else:
                    screen.fill(RED)
                pg.display.update()
            else:
                if current_team.value == T.player.value:
                    current_team = op
                else:
                    current_team = T.player
    while not is_quit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_quit = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    is_quit = True
    pg.quit()


def _init_game():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    pg.display.set_caption("Hex")
    pg.display.update()
    return screen
            

def _init_hexes(n, screen, op):
    hexes = []
    side = min(25, 200/n)
    Y = 320-((n+2)//2)*side*sin(pi/3)
    X = 480-((n+2)//2)*side*3/2
    for x in range(n+2):
        for y in range(n+2):
            center_x = X + x*side*3/2
            center_y = Y + y*2*side*sin(pi/3)-x*side*sin(pi/3)
            hex = h.Hex(x, y, center_x, center_y, screen, side)
            if x == 0 or x == n+1:
                hex.assign(T.player, screen)
            elif y == 0 or y == n+1:
                hex.assign(op, screen)
            hexes.append(hex)
    return hexes
