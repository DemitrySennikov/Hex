import pygame as pg
from team import Team as T
from math import sin, cos, pi


BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)


class Hex():
    def __init__(self, x, y, center_x, center_y, s):
        self.x = x
        self.y = y
        self.center_x = center_x
        self.center_y = center_y
        self.owner = None
        self.side = s
    
    
    def assign(self, team):
        self.owner = team

    
    def draw(self, screen):
        if self.owner == T.player:
            pg.draw.polygon(screen, BLUE, 
                    [(self.center_x+self.side*cos(pi*i/3),
                    self.center_y+self.side*sin(pi*i/3)) for i in range(6)])
        elif self.owner is not None:
            pg.draw.polygon(screen, RED, 
                    [(self.center_x+self.side*cos(pi*i/3),
                    self.center_y+self.side*sin(pi*i/3)) for i in range(6)])
        pg.draw.polygon(screen, BLACK, 
                [(self.center_x+self.side*cos(pi*i/3),
                  self.center_y+self.side*sin(pi*i/3)) for i in range(6)], 
                  int(self.side)//5)
        pg.display.update()
