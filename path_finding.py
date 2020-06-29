import pygame

import windows
from settings import *
from models import Grid
import phases.wall
import phases.a_star
from colors import ColorAStar, ColorGrid


def init_grid():
    GRID = Grid(row, cols)

    grid_color = ColorGrid(GRID)
    grid_color.color_empty_grid()

    pygame.display.update()
    return GRID, grid_color

def choose_start_and_end():
    var, st, ed = windows.first_window()
    GRID.set_start(*st)
    GRID.set_end(*ed)

    grid_color.color_start_and_end()
    return var

def add_walls(GRID):
    wall = phases.wall.Wall(GRID)
    wall.add_walls()

# SETUP GRID
pygame.init()
# construct game grid
GRID, grid_color = init_grid()
# Set start and end node
var = choose_start_and_end()
# add walls
add_walls(GRID)
# add neighbor here so it take account for walls
GRID.add_neighboring()
# END SETUP GRID

# ACTUAL A*
a_star = phases.a_star.AStar(GRID)
a_star_color = ColorAStar(GRID, a_star)

while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()

    grid_color.color_start_and_end()

    stopped = a_star.main()
    if stopped:
        a_star_color.color_final_path(stopped[1])
        pygame.display.update()

        windows.end_window(stopped[0])

        pygame.quit()
    if var.get():
        a_star_color.color_open_and_closed()
# END ACTUAL A*
