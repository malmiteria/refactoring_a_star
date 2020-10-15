
from contextlib import suppress

import pygame

from colors import color_walls

class Wall:

    def __init__(self, grid_model):
        self.grid = grid_model

    def key_space(self, event):
        return event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE

    def handle_all_event(self, ev):
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                self.mousePress(*pos)
            elif self.key_space(event):
                return False
        return True

    def mousePress(self, x, y):
        spot = self.grid.spot_from_coordinates(x, y)
        self.grid.turn_spot_to_wall_if_possible(spot)

    def add_walls(self):
        # adding wall by mouse press
        while True:
            ev = pygame.event.get()

            if not self.handle_all_event(ev):
                break
            color_walls(self.grid.obstructed_spots())
            pygame.display.update()
        # end adding wall by mouse press
