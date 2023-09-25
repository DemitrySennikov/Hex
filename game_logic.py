import pygame as pg
import json
import field as f
from team import Team as T
from moves import move
from pygame.font import Font
from button import Button


WIDTH = 960
HEIGHT = 640
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
def_font = pg.font.get_default_font()


def game(n, player_name, op, op_name, first_color, screen):
    screen.fill(WHITE)
    field = f.Field(n, op, screen)
    game_over = False
    is_quit = False
    player_text = Font(def_font, 32).render(player_name, True, BLUE)
    op_text = Font(def_font, 32).render(op_name, True, RED)
    player_rect = player_text.get_rect()
    player_rect.left = 60
    player_rect.top = 60
    op_rect = op_text.get_rect()
    op_rect.left = 60
    op_rect.top = 100
    screen.blit(player_text, player_rect)
    screen.blit(op_text, op_rect)
    if first_color == "Blue":
        current_team = T.player
        pg.draw.polygon(screen, BLUE, 
                        [(0, 0), (0, HEIGHT),
                         (WIDTH, HEIGHT), (WIDTH, 0)], 25)
    else:
        current_team = op
        pg.draw.polygon(screen, RED, 
                        [(0, 0), (0, HEIGHT),
                         (WIDTH, HEIGHT), (WIDTH, 0)], 25)
    moves = 0
    pg.display.update()
    while not game_over:
        hex, game_over, is_quit = move(current_team, field.hexes)
        if hex is None:
            continue
        if field.try_move(current_team, hex.x, hex.y):
            moves += 1
            hex.assign(current_team, screen)
            if field.is_team_win(current_team):
                game_over = True
                if current_team.value == T.player.value:
                    pg.draw.polygon(screen, BLUE, 
                                    [(0, 0), (0, HEIGHT),
                                     (WIDTH, HEIGHT), (WIDTH, 0)], 100)
                    winner = player_name
                    loser = op_name
                else:
                    pg.draw.polygon(screen, RED, 
                                    [(0, 0), (0, HEIGHT),
                                     (WIDTH, HEIGHT), (WIDTH, 0)], 100)
                    winner = op_name
                    loser = player_name
                write_records(winner, loser, moves)
            else:
                if current_team.value == T.player.value:
                    current_team = op
                    pg.draw.polygon(screen, RED, 
                                    [(0, 0), (0, HEIGHT),
                                     (WIDTH, HEIGHT), (WIDTH, 0)], 25)
                else:
                    current_team = T.player
                    pg.draw.polygon(screen, BLUE, 
                                    [(0, 0), (0, HEIGHT),
                                     (WIDTH, HEIGHT), (WIDTH, 0)], 25)
        pg.display.update()
    while not is_quit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_quit = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    is_quit = True


def write_records(winner, loser, moves):
    with open('records.json', 'r') as r:
        D = json.load(r)
    if winner not in D:
        D[winner] = {}
        D[winner]['Games'] = {}
        D[winner]['Games']['Played'] = 1
        D[winner]['Games']['Won'] = 1
        D[winner]['Max Win Points'] = (moves+1)//2
    else:
        D[winner]['Games']['Played'] += 1
        D[winner]['Games']['Won'] += 1
        D[winner]['Max Win Points'] = max((moves+1)//2, 
                                          D[winner]['Max Win Points'])
    if loser not in D:
        D[loser] = {}
        D[loser]['Games'] = {}
        D[loser]['Games']['Played'] = 1
        D[loser]['Games']['Won'] = 0
        D[loser]['Max Win Points'] = 0
    else:
        D[loser]['Games']['Played'] += 1
    with open('records.json', 'w') as r:
        json.dump(D, r, indent=4)
