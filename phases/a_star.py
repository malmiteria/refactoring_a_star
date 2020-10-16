import math

class AStar:

    def __init__(self, grid):
        self.grid = grid
        self.update_all_cost(self.grid.start, 0)
        self.grid.start.open()

    def heuristic(self, n, e): # Estimated cost between 2 nodes (accurate when they're neighbor)
        return math.sqrt((n.i - e.i)**2 + (n.j - e.j)**2)

    def start_to_end(self, current):
        while current is not self.grid.start:
            yield current
            current = current.previous

    def inner_path(self, current): # build path between current and start, excluding start
        return list(self.start_to_end(current))[1:]

    def handle_all_neighbors(self, current):
        for neighbor in current.neighbors:
            self.handle_one_neighbor(current, neighbor)

    # HANDLE ONE NEIGHBOR
    def handle_one_neighbor(self, current, neighbor):
        tempG = current.cost_to_reach + self.heuristic(current, neighbor)
        self.reparent_if_needed(current, neighbor, tempG)
        self.update_all_cost(neighbor, tempG)
        self.open_if_needed(neighbor)

    def reparent_if_needed(self, current, spot, cost):
        if spot.better_parent(cost):
            spot.previous = current

    def update_all_cost(self, spot, cost):
        if spot.is_new_or_cost_lower(cost):
            spot.cost_to_reach = cost
        spot.heuristic_cost_expected = self.heuristic(spot, self.grid.end)
        spot.full_cost_expected = spot.cost_to_reach + spot.heuristic_cost_expected

    def open_if_needed(self, spot):
        if spot.not_seen_yet():
            spot.open()
    # END HANDLE ONE NEIGHBOR

    def step(self):
        if len(list(self.grid.opened())) <= 0:
            return

        current = self.grid.smallest_opened_in_cost()
        
        if current == self.grid.end:
            print('done', current.full_cost_expected)
            return current.full_cost_expected, self.inner_path(current)

        current.close()

        self.handle_all_neighbors(current)

