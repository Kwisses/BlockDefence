import pygame
from BlockDefence.game_files.settings import *


class Bullet:
    def __init__(self, display):
        self.display = display
        self.damage = 1

    def in_range(self, t_coords, e_coords, aoe):
        for tower in t_coords:
            # count = 0
            t_x, t_y = tower
            for e in e_coords:
                e_x = e.rect.x
                e_y = e.rect.y
                if abs(e_x - (t_x - B_SIZE / 2)) <= aoe / 2:
                    if abs(e_y - (t_y - B_SIZE / 2)) <= aoe / 2:
                        pygame.draw.rect(self.display, red,
                                    (e_x + B_SIZE / 2 - BULLET_SIZE / 2,
                                        e_y + B_SIZE / 2 - BULLET_SIZE / 2,
                                        BULLET_SIZE, BULLET_SIZE))
                        e.health -= 1


def set_bullets(self, t_coords, e_coords):
    bullet = Bullet(self.display)
    bullet.in_range(t_coords, e_coords, t_green_aoe)
