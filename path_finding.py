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

def smallest_in_cost():
    fs = [spot.full_cost_expected for spot in openSet]
    lowestIndex = fs.index(min(fs))

    return openSet[lowestIndex]

def start_to_end(current):
    while current is not start:
        yield current
        current = current.previous

def inner_path(current):
    return list(start_to_end(current))[1:]

def handle_all_neighbors(current):
    for neighbor in current.neighbors:
        handle_one_neighbor(current, neighbor)

def never_reached(spot):
    return spot not in closedSet and spot not in openSet

def better_parent(spot, current_cost):
    return spot.previous is None or spot not in closedSet and spot in openSet and spot.cost_to_reach > current_cost

def is_best_cost_to_reach(spot, current_cost):
    return spot not in closedSet and spot not in openSet or spot.cost_to_reach > current_cost

def reparent_if_needed(current, spot, cost):
    if better_parent(spot, cost):
        spot.previous = current

def update_all_cost(spot, cost):
    if is_best_cost_to_reach(spot, cost):
        spot.cost_to_reach = cost
    spot.heuristic_cost_expected = heuristic(spot, end)
    spot.full_cost_expected = spot.cost_to_reach + spot.heuristic_cost_expected

def open_if_needed(spot):
    if never_reached(spot):
        openSet.append(spot)

def handle_one_neighbor(current, neighbor):
    tempG = current.cost_to_reach + heuristic(current, neighbor)
    reparent_if_needed(current, neighbor, tempG)
    update_all_cost(neighbor, tempG)
    open_if_needed(neighbor)


def main():
    if len(openSet) <= 0:
        return

    current = smallest_in_cost()
    
    if current == end:
        print('done', current.full_cost_expected)
        return current.full_cost_expected, inner_path(current)

    openSet.remove(current)
    closedSet.append(current)

    handle_all_neighbors(current)


while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()

    end.show(PINK, 0)
    start.show(PINK, 0)
    stopped = main()
    if stopped:
        for spot in stopped[1]:
            spot.show(BLUE, 0)
        pygame.display.update()

        windows.end_window(stopped[0])
        pygame.quit()
    if var.get():
        for spot in openSet:
            spot.show(GREEN, 0)

        for spot in closedSet:
            if spot != start:
                spot.show(RED, 0)
# END ACTUAL A*
