import pygame
import sys
import math
import os

import windows
from settings import *
from models import Grid
import phases.wall

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
phases.wall.add_walls(grid, start, end)

# add neighbor here so it take account for walls
GRID.add_neighboring()
# END SETUP GRID

# ACTUAL A*
def heuristic(n, e):
    return math.sqrt((n.i - e.i)**2 + (n.j - e.j)**2)

start.full_cost_expected = heuristic(start, end)
start.heuristic_cost_expected = heuristic(start, end)
openSet.append(start)

def main():
    end.show(PINK, 0)
    start.show(PINK, 0)
    if len(openSet) > 0:
        fs = [spot.full_cost_expected for spot in openSet]
        lowestIndex = fs.index(min(fs))

        current = openSet[lowestIndex]
        if current == end:
            print('done', current.full_cost_expected)
            start.show(PINK, 0)
            temp = current.full_cost_expected
            for i in range(round(current.full_cost_expected)):
                current.closed = False
                current.show(BLUE, 0)
                current = current.previous
            end.show(PINK, 0)
            pygame.display.update()

            windows.end_window(temp)
            pygame.quit()

        openSet.pop(lowestIndex)
        closedSet.append(current)

        for neighbor in current.neighbors:
            if neighbor not in closedSet:
                tempG = current.cost_to_reach + heuristic(current, neighbor)
                if neighbor in openSet: # node reached
                    if neighbor.cost_to_reach > tempG: # current way is shorter
                        neighbor.cost_to_reach = tempG
                        neighbor.previous = current # update parent, but don't reopen
                else:
                    neighbor.cost_to_reach = tempG
                    openSet.append(neighbor)

            neighbor.heuristic_cost_expected = heuristic(neighbor, end)
            neighbor.full_cost_expected = neighbor.cost_to_reach + neighbor.heuristic_cost_expected

            if neighbor.previous == None:
                neighbor.previous = current
    if var.get():
        for i in range(len(openSet)):
            openSet[i].show(GREEN, 0)

        for i in range(len(closedSet)):
            if closedSet[i] != start:
                closedSet[i].show(RED, 0)
        
    current.closed = True


while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()
    main()

# END ACTUAL A*
