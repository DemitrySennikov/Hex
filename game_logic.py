import pygame as pg
import team as t
import hex as h
import field as f
from math import sin, pi
from AI import AI_move


WIDTH = 960
HEIGHT = 640
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)


def game(n):
    field = f.Field(n)
    screen = _init_game()
    hexes = _init_hexes(n, screen)
    game_over = False
    is_quit = False 
    current_team = t.Team.player
    while not game_over:
        if current_team.value == t.Team.player.value:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_over = True
                    is_quit = True
                if event.type == pg.MOUSEBUTTONUP:
                    s_x, s_y = event.pos
                    #print(s_x, s_y)
                    nearest = _define_nearest_hex(s_x, s_y, hexes)
                    correct = field.try_move(current_team, 
                                             nearest.x, nearest.y)
                    if correct:
                        nearest.assign(current_team, screen)
                        if field.is_team_win(current_team):
                            game_over = True
                            screen.fill(BLUE)
                            pg.display.update()
                        else:
                            current_team = t.Team.AI
        else:
            hex = AI_move(current_team, hexes)
            hex.assign(current_team, screen)
            field.try_move(current_team, hex.x, hex.y)
            if field.is_team_win(current_team):
                game_over = True
                screen.fill(RED)
                pg.display.update()
            else:
                 current_team = t.Team.player
    while not is_quit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_quit = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    is_quit = True
    pg.quit()
    quit()      


def _init_game():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    pg.display.set_caption("Hex")
    pg.display.update()
    return screen
            

def _init_hexes(n, screen):
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
                hex.assign(t.Team.player, screen)
            elif y == 0 or y == n+1:
                hex.assign(t.Team.AI, screen)
            hexes.append(hex)
    return hexes


def _define_nearest_hex(s_x, s_y, hexes):
    min_d = 1e9
    nearest = hexes[0]
    for hex in hexes:
        current_d = _distance(s_x, s_y, hex)
        if current_d < min_d:
            min_d = current_d
            nearest = hex
    return nearest
    
    
def _distance(s_x, s_y, h):
    return ((s_x - h.center_x)**2 + (s_y - h.center_y)**2) ** 0.5
