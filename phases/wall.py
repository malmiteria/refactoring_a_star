
import pygame

from settings import *

def add_walls(grid, start, end):
    # adding wall by mouse press
    def mousePress(x):
        t, w = x
        g1 = t // (SCREEN_HEIGHT // cols)
        g2 = w // (SCREEN_WIDTH // row)
        acess = grid[g1][g2]
        if acess != start and acess != end:
            if not acess.obs:
                acess.obs = True
                acess.show(WHITE, 0)

    loop = True
    while loop:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
            if pygame.mouse.get_pressed()[0]:
                try:
                    pos = pygame.mouse.get_pos()
                    mousePress(pos)
                except AttributeError:
                    pass
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    loop = False
                    break
        pygame.display.update()
    # end adding wall by mouse press
