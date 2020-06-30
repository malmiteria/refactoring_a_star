import pygame

import windows
from settings import *
import phases.a_star
from colors import ColorAStar
from game_stages.setup_and_wall import SetupAndWall

pygame.init()
saw = SetupAndWall(row, cols)

# ACTUAL A*
a_star = phases.a_star.AStar(saw.grid)
a_star_color = ColorAStar(saw.grid, a_star)

while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
    pygame.display.update()

    saw.grid_color.color_start_and_end()

    stopped = a_star.main()
    if stopped:
        a_star_color.color_final_path(stopped[1])
        pygame.display.update()

        windows.end_window(stopped[0])

        pygame.quit()
    if saw.var.get():
        a_star_color.color_open_and_closed()
# END ACTUAL A*
