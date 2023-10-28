import sys
import pygame
from setting import Setting
from ship import Ship
from game_functions import *
# def check_events(ship):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = True
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = True
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_RIGHT:
#                 ship.moving_right = False
#             elif event.key == pygame.K_LEFT:
#                 ship.moving_left = False
#
# def update_screen(ai_setting, screen ,ship):
#     screen.fill(ai_setting.bg_color)
#     ship.blitme()
#     pygame.display.flip()
def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode(ai_setting.setscreen())
    ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion")
    while True:
        check_events(ship)
        ship.update()
        update_screen(ai_setting,screen,ship)

run_game()
