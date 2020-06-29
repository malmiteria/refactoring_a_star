
import pygame

from settings import *

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

    def show(self, color, st):
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


