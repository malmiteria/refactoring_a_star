
import pygame

import windows
from models import Grid
import phases.wall
from colors import ColorGrid

class SetupAndWall:

    def __init__(self):
        self.grid = Grid()
        self.grid_color = ColorGrid(self.grid)

    def run(self):
        # render colored empty map before asking where to put start and stop.
        self.grid_color.color_empty_grid()
        pygame.display.update()

        # Set start and stop node using windows to ask user.
        self.color_steps = windows.first_window(self.grid)
        self.grid_color.color_start_and_end()

        # add walls
        wall = phases.wall.Wall(self.grid)
        wall.add_walls()

        # add neighbor here so it take account for walls
        self.grid.add_neighboring()

