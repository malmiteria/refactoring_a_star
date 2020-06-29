
import pygame

from settings import *

def show(spot, color, st):
    pygame.draw.rect(screen, color, (spot.i * w, spot.j * h, w, h), st)

def color_walls(wall_spot):
    for spot in wall_spot:
        show(spot, WHITE, 0)

class ColorGrid:

    def __init__(self, grid):
        self.grid = grid

    def color_empty_grid(self):
        # Default coloring
        for spot in self.grid.not_obstructed_spots():
            show(spot, WHITE, 1)

        for spot in self.grid.obstructed_spots():
            show(spot, GREY, 0)

    def color_start_and_end(self):
        show(self.grid.start, PINK, 0)
        show(self.grid.end, PINK, 0)

class ColorAStar:

    def __init__(self, grid, a_star):
        self.grid = grid
        self.a_star = a_star

    def color_final_path(self, spots):
        for spot in spots:
            show(spot, BLUE, 0)

    def color_open_and_closed(self):
        for spot in self.a_star.openSet:
            show(spot, GREEN, 0)

        for spot in self.a_star.closedSet:
            if spot != self.grid.start:
                show(spot, RED, 0)
