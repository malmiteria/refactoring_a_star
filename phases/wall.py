
from contextlib import suppress

import pygame

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, cols, row
from colors import color_walls

class Wall:

    def __init__(self, grid_model):
        self.grid = grid_model.grid
        self.start = grid_model.start
        self.end = grid_model.end
        self.wall_spots = []

    def key_space(self, event):
        return event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE

    def handle_all_event(self, ev):
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
            if pygame.mouse.get_pressed()[0]:
                with suppress(AttributeError):
                    pos = pygame.mouse.get_pos()
                    self.mousePress(pos)
            elif self.key_space(event):
                return False
        return True

    def mousePress(self, x):
        t, w = x
        g1 = t // (SCREEN_HEIGHT // cols)
        g2 = w // (SCREEN_WIDTH // row)
        acess = self.grid[g1][g2]
        if acess != self.start and acess != self.end:
            if not acess.obs:
                acess.obs = True
                self.wall_spots.append(acess)

    def add_walls(self):
        # adding wall by mouse press

        while True:
            ev = pygame.event.get()

            if not self.handle_all_event(ev):
                break
            color_walls(self.wall_spots)
            pygame.display.update()
        # end adding wall by mouse press
