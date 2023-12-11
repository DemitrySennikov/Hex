import pygame as pg
from field import Field
from team import Team as T
from moves import move
from pygame.font import Font
from records import update_records
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
    home = Button("Home", 20, WHITE, WHITE, BLACK, 80, 50,
                  (WIDTH-100, 100), screen)
    field = Field(n, op)
    field.draw(screen)
    game_over = False
    is_quit = False
    is_menu = False
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
        hex, game_over, is_menu, is_quit = move(current_team, field.hexes,
                                                home)
        if hex is None:
            continue
        if field.try_move(current_team, hex.x, hex.y):
            moves += 1
            hex.assign(current_team)
            hex.draw(screen)
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
                update_records(winner, loser, moves, n)
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
    while not is_menu:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_menu = True
                is_quit = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if home.is_pressed(event.pos):
                    is_menu = True
    return is_quit
