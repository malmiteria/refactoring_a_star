
import pygame

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, ROW, COLS, h, w, screen

class Spot:
    def __init__(self, x, y, grid_model):
        self.i = x
        self.j = y
        self.full_cost_expected = 0
        self.cost_to_reach = 0
        self.heuristic_cost_expected = 0
        self.neighbors = []
        self.grid = grid_model
        self.previous = None
        self.obstructed = False

    def addNeighbors(self):
        for i, j in self.accessible_neighboring():
            self.add_neighbor(i, j)

    def add_neighbor(self, i, j):
        self.neighbors.append(self.grid.spot_at(i, j))

    def possible_neighboring(self):
        for i in [self.i-1, self.i, self.i +1]:
            for j in [self.j-1, self.j, self.j +1]:
                yield i, j

    def in_map_neighboring(self):
        for i, j in self.possible_neighboring():
            if i == self.i and j == self.j:
                continue
            if i >= self.grid.cols-1:
                continue
            if i <= 0:
                continue
            if j >= self.grid.row-1:
                continue
            if j <= 0:
                continue
            yield i, j

    def accessible_neighboring(self):
        for i, j in self.in_map_neighboring():
            if self.grid.spot_at(i, j).obstructed:
                continue
            yield i, j


class Grid(object):

    def __init__(self):
        self.row = ROW
        self.cols = COLS

        self.grid = [[Spot(i, j, self) for j in range(self.row)] for i in range(self.cols)]

        for spot in self.outer_ring_spots():
            spot.obstructed = True

    def spot_at(self, i, j):
        return self.grid[i][j]

    def outer_ring_spots(self):
        for spot in self.grid[0]:
            yield spot
        for row in self.grid[1:-1]:
            yield row[0]
            yield row[-1]
        for spot in self.grid[-1]:
            yield spot

    def all_spots(self):
        for column in self.grid:
            for spot in column:
                yield spot

    def obstructed_spots(self):
        for spot in self.all_spots():
            if not spot.obstructed:
                continue
            yield spot

    def not_obstructed_spots(self):
        for spot in self.all_spots():
            if spot.obstructed:
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

    def spot_from_coordinates(self, x, y):
        g1 = x // (SCREEN_HEIGHT // COLS)
        g2 = y // (SCREEN_WIDTH // ROW)
        return self.grid[g1][g2]

    def spot_can_be_a_wall(self, spot):
        return spot != self.start and spot != self.end and not spot.obstructed

    def turn_spot_to_wall_if_possible(self, spot):
        if self.spot_can_be_a_wall(spot):
            spot.obstructed = True
