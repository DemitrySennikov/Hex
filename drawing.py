# Pygame шаблон - скелет для нового проекта Pygame
import pygame as pg

WIDTH = 360  # ширина игрового окна
HEIGHT = 480 # высота игрового окна
FPS = 30 # частота кадров в секунду
# создаем игру и окно
pg.init()
pg.mixer.init()  # для звука
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Hex")
clock = pg.time.Clock()