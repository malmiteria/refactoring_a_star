
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
cols = 50
row = 50
openSet = []
closedSet = []
PINK = (255, 8, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (220, 220, 220)
WHITE = (255, 255, 255)
w = SCREEN_WIDTH / cols
h = SCREEN_HEIGHT / row
cameFrom = []
