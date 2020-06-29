import pygame

import windows
from settings import *
from models import Grid
import phases.wall
import phases.a_star
from colors import color_empty_grid, color_start_and_end, color_final_path, color_open_and_closed

# SETUP GRID
pygame.init()

# construct game grid
GRID = Grid(row, cols)
grid = GRID.grid

color_empty_grid(GRID)

pygame.display.update()

# Set start and end node
var, st, ed = windows.first_window()
start = grid[st[0]][st[1]]
end = grid[ed[0]][ed[1]]

color_start_and_end(start, end)

# add walls
wall = phases.wall.Wall(grid, start, end)
wall.add_walls()

# add neighbor here so it take account for walls
GRID.add_neighboring()
# END SETUP GRID

# ACTUAL A*
a_star = phases.a_star.AStar(start, end)
a_star.update_all_cost(start, 0)
a_star.openSet.append(start)

while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()

    color_start_and_end(start, end)

    stopped = a_star.main()
    if stopped:
        color_final_path(stopped[1])
        pygame.display.update()

        windows.end_window(stopped[0])

        pygame.quit()
    if var.get():
        color_open_and_closed(a_star.openSet, a_star.closedSet, start)
# END ACTUAL A*
