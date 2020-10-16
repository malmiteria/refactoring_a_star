from settings import SCREEN_WIDTH, SCREEN_HEIGHT, ROW, COLS

class Spot:
    def __init__(self, x, y, grid):
        self.i = x
        self.j = y
        self.full_cost_expected = 0
        self.cost_to_reach = 0
        self.heuristic_cost_expected = 0
        self.grid = grid
        self.previous = None
        self.obstructed = False
        self.state = None

    def possible_neighboring(self):
        for i in range(-1,2):
            for j in range(-1,2):
                yield self.i + i, self.j + j

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
            yield self.grid.spot_at(i, j)

    @property
    def neighbors(self):
        for spot in self.in_map_neighboring():
            if spot.obstructed:
                continue
            yield spot

    # state in a_star 
    def is_opened(self):
        return self.state == 'open'

    def not_seen_yet(self):
        return self.state is None

    def better_parent(self, cost):
        return self.previous is None or \
            self.is_opened() and \
            self.cost_to_reach > cost

    def is_new_or_cost_lower(self, cost):
        return self.not_seen_yet() or \
            self.cost_to_reach > cost

    def open(self):
        self.state = 'open'

    def close(self):
        self.state = 'close'


class Grid(object):

    def __init__(self):
        self.row = ROW
        self.cols = COLS

        self.grid = [[Spot(i, j, self) for j in range(self.row)] for i in range(self.cols)]

        for spot in self.outer_ring_spots():
            spot.obstructed = True

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

    def opened(self):
        for spot in self.all_spots():
            if spot.state != 'open':
                continue
            yield spot

    def closed(self):
        for spot in self.all_spots():
            if spot.state != 'close':
                continue
            yield spot

    def smallest_opened_in_cost(self):
        opened_spots = self.opened()
        least_expensive_spot = next(opened_spots)
        for spot in opened_spots:
            if spot.full_cost_expected < least_expensive_spot.full_cost_expected:
                least_expensive_spot = spot
        return least_expensive_spot

    def set_start(self, x, y):
        self.start = self.grid[x][y]

    def set_end(self, x, y):
        self.end = self.grid[x][y]

    def spot_can_be_a_wall(self, spot):
        return spot != self.start and spot != self.end and not spot.obstructed

    def turn_spot_to_wall_if_possible(self, spot):
        if self.spot_can_be_a_wall(spot):
            spot.obstructed = True

    def spot_at(self, i, j):
        return self.grid[i][j]

    def spot_from_coordinates(self, x, y):
        g1 = x // (SCREEN_HEIGHT // COLS)
        g2 = y // (SCREEN_WIDTH // ROW)
        return self.grid[g1][g2]
