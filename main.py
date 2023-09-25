import pygame as pg
from menu import menu


WIDTH = 960
HEIGHT = 640
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Hex")
    pg.display.update()
    menu(screen)
    pg.quit()


if __name__ == '__main__':
    main()
