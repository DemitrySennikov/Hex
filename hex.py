import pygame as pg
from team import Team as T
from math import sin, cos, pi


BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)


class Hex():
    def __init__(self, x, y, center_x, center_y, screen, s):
        self.x = x
        self.y = y
        self.center_x = center_x
        self.center_y = center_y
        self.owner = 0
        self.side = s
        pg.draw.polygon(screen, BLACK,
                        [(center_x+s*cos(pi*i/3), center_y+s*sin(pi*i/3)) for i in range(6)],
                        int(s)//5)
        pg.display.update()
    
    
    def assign(self, team, screen):
        self.owner = team.value
        if team.value == T.player.value:
            color = BLUE
        else:
            color = RED
        pg.draw.polygon(screen, color, 
                [(self.center_x+self.side*cos(pi*i/3),
                  self.center_y+self.side*sin(pi*i/3)) for i in range(6)])
        pg.draw.polygon(screen, BLACK, 
                [(self.center_x+self.side*cos(pi*i/3),
                  self.center_y+self.side*sin(pi*i/3)) for i in range(6)], 
                  int(self.side)//5)
        pg.display.update()
