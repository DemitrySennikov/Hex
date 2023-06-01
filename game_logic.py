import pygame as pg
import field as f
from team import Team as T
from moves import move


WIDTH = 960
HEIGHT = 640
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)


def game(n, op):
    screen = _init_game()
    field = f.Field(n, op, screen)
    game_over = False
    is_quit = False
    current_team = T.player
    while not game_over:
        hex, game_over, is_quit = move(current_team, field.hexes)
        if hex is None:
            continue
        correct = field.try_move(current_team, hex.x, hex.y)
        if correct:
            hex.assign(current_team, screen)
            if field.is_team_win(current_team):
                game_over = True
                if current_team.value == T.player.value:
                    pg.draw.polygon(screen, BLUE, 
                                    [(0, 0), (0, 640),
                                     (960, 640), (960, 0)], 100)
                else:
                    pg.draw.polygon(screen, RED, 
                                    [(0, 0), (0, 640),
                                     (960, 640), (960, 0)], 100)
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
