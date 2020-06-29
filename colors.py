
import pygame

from settings import *

def show(spot, color, st):
    pygame.draw.rect(screen, color, (spot.i * w, spot.j * h, w, h), st)

def color_walls(wall_spot):
    for spot in wall_spot:
        show(spot, WHITE, 0)

def color_empty_grid(GRID):
    # Default coloring
    for spot in GRID.not_obstructed_spots():
        show(spot, WHITE, 1)

    for spot in GRID.obstructed_spots():
        show(spot, GREY, 0)

def color_start_and_end(start, end):
    show(start, PINK, 0)
    show(end, PINK, 0)

def color_final_path(spots):
    for spot in spots:
        show(spot, BLUE, 0)

def color_open_and_closed(openSet, closedSet, start):
    for spot in openSet:
        show(spot, GREEN, 0)

    for spot in closedSet:
        if spot != start:
            show(spot, RED, 0)
