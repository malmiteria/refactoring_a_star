
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
        for i, j in possible_neighboring():
            if i >= cols-1:
                continue
            if i <= 0:
                continue
            if j >= row-1:
                continue
            if j <= 0:
                continue
            if self.grid[i][j].obs:
                continue
            if i == self.i and j == self.j:
                continue
            self.add_neighbor(i, j)

    def add_neighbor(self, i, j):
        self.neighbors.append(self.grid[i][j])

    def possible_neighboring(self):
        for i in [self.i-1, self.i, self.i +1]:
            for j in [self.j-1, self.j, self.j +1]:
                yield i, j

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


