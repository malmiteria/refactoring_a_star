import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PINK = (255, 8, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (220, 220, 220)
WHITE = (255, 255, 255)
COLS = 50
ROW = 50
w = SCREEN_WIDTH / COLS
h = SCREEN_HEIGHT / ROW

def show(spot, color, st):
    pygame.draw.rect(screen, color, (spot.i * w, spot.j * h, w, h), st)
