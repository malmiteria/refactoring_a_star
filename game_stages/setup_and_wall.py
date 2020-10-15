
import pygame

import windows
from models import Grid
import phases.wall
from colors import ColorGrid

class SetupAndWall:

    def __init__(self):
        # construct game grid
        self.init_grid()
        # Set start and end node
        self.choose_start_and_end()
        # add walls
        self.add_walls()
        # add neighbor here so it take account for walls
        self.grid.add_neighboring()

    def init_grid(self):
        self.grid = Grid()
        self.grid_color = ColorGrid(self.grid)
        pygame.display.update()

    def choose_start_and_end(self):
        self.color_steps = windows.first_window(self.grid)
        self.grid_color.color_start_and_end()

    def add_walls(self):
        wall = phases.wall.Wall(self.grid)
        wall.add_walls()

