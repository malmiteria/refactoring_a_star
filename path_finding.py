import pygame
import sys
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

import windows

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

class Spot:
    def __init__(self, x, y, grid):
        self.i = x
        self.j = y
        self.full_cost_expected = 0
        self.cost_to_reach = 0
        self.heuristic_cost_expected = 0
        self.neighbors = []
        self.grid = grid
        self.previous = None
        self.obs = False
        self.closed = False

    def show(self, color, st):
        if not self.closed:
            pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)

    def addNeighbors(self):
        if self.i < cols-1 and not self.grid[self.i + 1][self.j].obs:
            self.add_neighbor_coo(self.i + 1)
        self.add_neighbor_coo(self.i)
        if self.i > 0 and not self.grid[self.i - 1][self.j].obs:
            self.add_neighbor_coo(self.i - 1)

    def add_neighbor_coo(self, i):
        if self.j < row-1 and not self.grid[i][self.j + 1].obs:
            self.neighbors.append(self.grid[i][self.j + 1])
        if i != self.i:
            self.neighbors.append(self.grid[i][self.j])
        if self.j > 0 and not self.grid[i][self.j - 1].obs:
            self.neighbors.append(self.grid[i][self.j - 1])

class Grid:

    def __init__(self, row, cols):
        self.grid = [None] * cols
        # create 2d array
        for i in range(cols):
            self.grid[i] = [None] * row

        # Create Spots
        for i in range(cols):
            for j in range(row):
                self.grid[i][j] = Spot(i, j, self.grid)

        # Default coloring
        for i in range(cols):
            for j in range(row):
                self.grid[i][j].show(WHITE, 1)

        for i in range(0,row):
            self.grid[0][i].show(GREY, 0)
            self.grid[0][i].obs = True
            self.grid[cols-1][i].obs = True
            self.grid[cols-1][i].show(GREY, 0)
            self.grid[i][row-1].show(GREY, 0)
            self.grid[i][0].show(GREY, 0)
            self.grid[i][0].obs = True
            self.grid[i][row-1].obs = True

    def add_neighboring(self):
        # Add neighboring
        for i in range(cols):
            for j in range(row):
                self.grid[i][j].addNeighbors()


GRID = Grid(row, cols)
grid = GRID.grid

pygame.display.update()

# Set start and end node
st = [2, 2] # default start
ed = [45, 45] # default end
var, st, ed = windows.first_window()
start = grid[st[0]][st[1]]
end = grid[ed[0]][ed[1]]

pygame.init()

end.show(PINK, 0)
start.show(PINK, 0)

# adding wall by mouse press
def mousePress(x):
    t, w = x
    g1 = t // (SCREEN_HEIGHT // cols)
    g2 = w // (SCREEN_WIDTH // row)
    acess = grid[g1][g2]
    if acess != start and acess != end:
        if not acess.obs:
            acess.obs = True
            acess.show(WHITE, 0)

loop = True
while loop:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                mousePress(pos)
            except AttributeError:
                pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                loop = False
                break
    pygame.display.update()
# end adding wall by mouse press
# add neighbor here so it take account for walls
GRID.add_neighboring()


def heurisitic(n, e):
    d = math.sqrt((n.i - e.i)**2 + (n.j - e.j)**2)
    #d = abs(n.i - e.i) + abs(n.j - e.j)
    return d

start.full_cost_expected = heurisitic(start, end)
start.heuristic_cost_expected = heurisitic(start, end)
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
                tempG = current.cost_to_reach + heurisitic(current, neighbor)
                if neighbor in openSet:
                    if neighbor.cost_to_reach > tempG:
                        neighbor.cost_to_reach = tempG
                else:
                    neighbor.cost_to_reach = tempG
                    openSet.append(neighbor)

            neighbor.heuristic_cost_expected = heurisitic(neighbor, end)
            neighbor.full_cost_expected = neighbor.cost_to_reach + neighbor.heuristic_cost_expected

            if neighbor.previous == None:
                neighbor.previous = current
    if var.get():
        for i in range(len(openSet)):
            openSet[i].show(GREEN, 0)

        for i in range(len(closedSet)):
            if closedSet[i] != start:
                closedSet[i].show(RED, 0)
        pygame.display.update()
        
    current.closed = True


while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()
    main()

