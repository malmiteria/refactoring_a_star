import math

class AStar:

    def __init__(self, grid):
        self.start = grid.start
        self.end = grid.end
        self.openSet = []
        self.closedSet = []
        self.update_all_cost(self.start, 0)
        self.openSet.append(self.start)

    def heuristic(self, n, e): # Estimated cost between 2 nodes (accurate when they're neighbor)
        return math.sqrt((n.i - e.i)**2 + (n.j - e.j)**2)

    def smallest_in_cost(self): # used to determine next node to pick
        fs = [spot.full_cost_expected for spot in self.openSet]
        lowestIndex = fs.index(min(fs))
        return self.openSet[lowestIndex]

    def start_to_end(self, current):
        while current is not self.start:
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
        if self.better_parent(spot, cost):
            spot.previous = current

    def update_all_cost(self, spot, cost):
        if self.is_new_or_cost_lower(spot, cost):
            spot.cost_to_reach = cost
        spot.heuristic_cost_expected = self.heuristic(spot, self.end)
        spot.full_cost_expected = spot.cost_to_reach + spot.heuristic_cost_expected

    def open_if_needed(self, spot):
        if self.not_seen_yet(spot):
            self.openSet.append(spot)

    def is_opened(self, spot):
        return spot not in self.closedSet and \
            spot in self.openSet

    def not_seen_yet(self, spot):
        return spot not in self.closedSet and \
            spot not in self.openSet

    def better_parent(self, spot, cost):
        return spot.previous is None or \
            self.is_opened(spot) and \
            spot.cost_to_reach > cost

    def is_new_or_cost_lower(self, spot, cost):
        return self.not_seen_yet(spot) or \
            spot.cost_to_reach > cost
    # END HANDLE ONE NEIGHBOR

    def main(self):
        if len(self.openSet) <= 0:
            return

        current = self.smallest_in_cost()
        
        if current == self.end:
            print('done', current.full_cost_expected)
            return current.full_cost_expected, self.inner_path(current)

        self.openSet.remove(current)
        self.closedSet.append(current)

        self.handle_all_neighbors(current)

