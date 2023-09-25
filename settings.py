import pygame as pg
from button import Button
from pygame.font import SysFont, Font
from game_logic import game
from team import Team as T


WIDTH = 960
HEIGHT = 640
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
def_font = pg.font.get_default_font()


def game_settings(screen):
    screen.fill(WHITE)
    title = SysFont(def_font, 72, False, True).render("VS", True, BLACK)
    title_rect = title.get_rect()
    title_rect.center = (WIDTH//2, HEIGHT//2)
    screen.blit(title, title_rect)
    size_text = Font(def_font, 20).render("Size", True, BLACK)
    size_rect = size_text.get_rect()
    size_rect.center = (WIDTH//4, HEIGHT//3 - 50)
    screen.blit(size_text, size_rect)
    first_text = Font(def_font, 20).render("First move", True, BLACK)
    first_rect = first_text.get_rect()
    first_rect.center = (3*WIDTH//4, HEIGHT//3 - 50)
    screen.blit(first_text, first_rect)
    player_name = Button("Player1", 32, BLACK, WHITE, BLUE, 150, 50,
                         (WIDTH//2, HEIGHT//3), screen)
    op_player_name = Button("Player2", 32, BLACK, WHITE, RED, 150, 50,
                            (WIDTH//2, 2*HEIGHT//3), screen)
    RANDOM = Button("Easy", 40, WHITE, WHITE, RED, 150, 50,
                    (WIDTH//4, 3*HEIGHT//4), screen)
    PVP = Button("PvP", 40, WHITE, WHITE, RED, 150, 50,
                 (WIDTH//2, 3*HEIGHT//4), screen)
    AI = Button("Hard", 40, WHITE, WHITE, RED, 150, 50,
                (3*WIDTH//4, 3*HEIGHT//4), screen)
    size = Button("11", 32, BLACK, WHITE, GREEN, 50, 50,
                  (WIDTH//4, HEIGHT//3), screen)
    first = Button("Blue", 32, BLUE, RED, WHITE, 100, 50,
                   (3*WIDTH//4, HEIGHT//3), screen)
    pg.display.update()
    is_quit = False
    while not is_quit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_quit = True
            if event.type == pg.MOUSEBUTTONDOWN:
                p = event.pos
                if player_name.is_pressed(p) != player_name.active:
                    player_name.change()
                if op_player_name.is_pressed(p) != op_player_name.active:
                    op_player_name.change()
                if size.is_pressed(p) != size.active:
                    size.change()
                if first.is_pressed(p):
                    if first.text == "Blue":
                        first.text = "Red"
                    else:
                        first.text = "Blue"
                    first.change()
                if RANDOM.is_pressed(p):
                    game(int(size.text), player_name.text, T.random,
                         "Random", first.text, screen)
                    is_quit = True
                if PVP.is_pressed(p):
                    game(int(size.text), player_name.text, T.other_player,
                         op_player_name.text, first.text, screen)
                    is_quit = True
                if AI.is_pressed(p):
                    game(int(size.text), player_name.text, T.AI,
                         "AI", first.text, screen)
                    is_quit = True
            if event.type == pg.KEYDOWN:
                s = event.unicode
                if player_name.active:
                    if event.key == pg.K_BACKSPACE:
                        player_name.text = player_name.text[:-1]
                    else:
                        player_name.text = (player_name.text + s)[:10]
                    player_name.draw()
                if op_player_name.active:
                    if event.key == pg.K_BACKSPACE:
                        op_player_name.text = op_player_name.text[:-1]
                    else:
                        op_player_name.text = (op_player_name.text + s)[:10]
                    op_player_name.draw()
                if size.active:
                    if event.key == pg.K_BACKSPACE:
                        size.text = size.text[:-1]
                        if size.text == "":
                            size.text = "0"
                    elif pg.key.name(event.key).isdigit():
                        if size.text == "0":
                            size.text = s
                        else:
                            size.text = (size.text + s)
                        if int(size.text) > 30:
                            size.text = "30"
                    size.draw()
