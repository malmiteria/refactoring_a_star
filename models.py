
import pygame

from settings import h, w, screen

class Spot:
    def __init__(self, x, y, grid_model):
        self.i = x
        self.j = y
        self.full_cost_expected = 0
        self.cost_to_reach = 0
        self.heuristic_cost_expected = 0
        self.neighbors = []
        self.grid = grid_model.grid
        self.cols = grid_model.cols
        self.row = grid_model.row
        self.previous = None
        self.obs = False

    def addNeighbors(self):
        for i, j in self.accessible_neighboring():
            self.add_neighbor(i, j)

    def add_neighbor(self, i, j):
        self.neighbors.append(self.grid[i][j])

    def possible_neighboring(self):
        for i in [self.i-1, self.i, self.i +1]:
            for j in [self.j-1, self.j, self.j +1]:
                yield i, j

    def in_map_neighboring(self):
        for i, j in self.possible_neighboring():
            if i == self.i and j == self.j:
                continue
            if i >= self.cols-1:
                continue
            if i <= 0:
                continue
            if j >= self.row-1:
                continue
            if j <= 0:
                continue
            yield i, j

    def accessible_neighboring(self):
        for i, j in self.in_map_neighboring():
            if self.grid[i][j].obs:
                continue
            yield i, j


class Grid:

    def __init__(self, row, cols):
        self.row = row
        self.cols = cols

        self.grid = [None] * cols
        # create 2d array
        for i in range(cols):
            self.grid[i] = [None] * row

        # Create Spots
        for i in range(cols):
            for j in range(row):
                self.grid[i][j] = Spot(i, j, self)

        for i in range(0,row):
            self.grid[0][i].obs = True
            self.grid[cols-1][i].obs = True
            self.grid[i][0].obs = True
            self.grid[i][row-1].obs = True

    def all_spots(self):
        for column in self.grid:
            for spot in column:
                yield spot

    def obstructed_spots(self):
        for spot in self.all_spots():
            if not spot.obs:
                continue
            yield spot

    def not_obstructed_spots(self):
        for spot in self.all_spots():
            if spot.obs:
                continue
            yield spot

    def add_neighboring(self):
        # Add neighboring
        for spot in self.all_spots():
            spot.addNeighbors()

    def set_start(self, x, y):
        self.start = self.grid[x][y]

    def set_end(self, x, y):
        self.end = self.grid[x][y]
