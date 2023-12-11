import pygame as pg
from pygame.font import SysFont
from settings import game_settings
from button import Button

WIDTH = 960
HEIGHT = 640
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
def_font = pg.font.get_default_font()


def menu(screen):
    screen.fill(WHITE)
    title = SysFont(def_font, 240, True, True).render("HEX", True, BLACK)
    title_rect = title.get_rect()
    title_rect.center = (WIDTH//2, HEIGHT//3)
    screen.blit(title, title_rect)
    records = Button("Records", 50, WHITE, WHITE, BLUE,
                     150, 150, (WIDTH//4, 2*HEIGHT//3), screen)
    continue_play = Button("Continue", 40, WHITE, WHITE, GREEN,
                  150, 150, (WIDTH//2, 2*HEIGHT//3), screen)
    play = Button("Play", 70, WHITE, WHITE, RED,
                  150, 150, (3*WIDTH//4, 2*HEIGHT//3), screen)
    pg.display.update()
    is_quit = False
    while not is_quit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_quit = True
            if event.type == pg.MOUSEBUTTONDOWN:
                p = event.pos
                if play.is_pressed(p):
                    game_settings(screen)
                    is_quit = True
