import pygame as pg
from pygame.font import Font


class Button():
    def __init__(self, text, size, color_t_0, color_t_1, color_bg, 
                 width, height, center, screen):
        self.text = text
        self.size = size
        self.active = False
        self.color_t_0 = color_t_0
        self.color_t_1 = color_t_1
        self.color_bg = color_bg
        self.rect = pg.Rect(0, 0, width, height)
        self.rect.center = center
        self.screen = screen
        self.draw()

    def _color(self):
        if self.active:
            return self.color_t_1
        return self.color_t_0

    def draw(self):
        text = Font(None, self.size).render(self.text, True, self._color())
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        pg.draw.rect(self.screen, self.color_bg, self.rect)
        self.screen.blit(text, text_rect)
        pg.display.update()

    def is_pressed(self, point):
        return self.rect.collidepoint(point)
    
    def text_input(self, event):
        if self.active:
            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text = (self.text + event.unicode)[:15]
            self.draw()

    def change(self):
        self.active = not self.active
        self.draw()
