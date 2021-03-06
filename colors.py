from settings import show, WHITE, GREY, PINK, BLUE, GREEN, RED

def color_walls(wall_spot):
    for spot in wall_spot:
        show(spot, WHITE, 0)

class ColorGrid:

    def __init__(self, grid):
        self.grid = grid

    def color_empty_grid(self):
        # Default coloring
        for spot in self.grid.not_obstructed_spots():
            show(spot, WHITE, 1)

        for spot in self.grid.obstructed_spots():
            show(spot, GREY, 0)

    def color_start_and_end(self):
        show(self.grid.start, PINK, 0)
        show(self.grid.end, PINK, 0)

class ColorAStar:

    def __init__(self, a_star):
        self.a_star = a_star

    def color_final_path(self, spots):
        for spot in spots:
            show(spot, BLUE, 0)

    def color_open_and_closed(self):
        for spot in self.a_star.grid.opened():
            if spot != self.a_star.grid.start:
                if spot != self.a_star.grid.end:
                    show(spot, GREEN, 0)

        for spot in self.a_star.grid.closed():
            if spot != self.a_star.grid.start:
                if spot != self.a_star.grid.end:
                    show(spot, RED, 0)
