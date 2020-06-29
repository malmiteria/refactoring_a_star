import pygame

import windows
from settings import *
from models import Grid
import phases.wall
import phases.a_star

# SETUP GRID
pygame.init()

# construct game grid
GRID = Grid(row, cols)
grid = GRID.grid

pygame.display.update()

# Set start and end node
var, st, ed = windows.first_window()
start = grid[st[0]][st[1]]
end = grid[ed[0]][ed[1]]

start.show(PINK, 0)
end.show(PINK, 0)

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

    end.show(PINK, 0)
    start.show(PINK, 0)
    stopped = a_star.main()
    if stopped:
        for spot in stopped[1]:
            spot.show(BLUE, 0)
        pygame.display.update()

        windows.end_window(stopped[0])
        pygame.quit()
    if var.get():
        for spot in a_star.openSet:
            spot.show(GREEN, 0)

        for spot in a_star.closedSet:
            if spot != start:
                spot.show(RED, 0)
# END ACTUAL A*
