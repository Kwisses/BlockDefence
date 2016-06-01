import pygame
from BlockDefence.game_files.settings import *


class Bullet:

    def __init__(self, display):
        self.display = display
        self.damage = 1

    def range(self, t_coords, e_coords, aoe):
        for tower in t_coords:
            tower_x, tower_y = tower
            for enemy in e_coords:
                enemy = enemy[0]
                enemy_x = enemy.rect.x
                enemy_y = enemy.rect.y
                if abs(enemy_x - (tower_x - B_SIZE / 2)) <= aoe / 2:
                    if abs(enemy_y - (tower_y - B_SIZE / 2)) <= aoe / 2:
                        return True
                    else:
                        return "False!"

    def update(self, e_coords):
        for enemy in e_coords:
            enemy = enemy[0]
            enemy_x = enemy.rect.x
            enemy_y = enemy.rect.y
            pygame.draw.rect(self.display, red,
                                      (enemy_x + B_SIZE / 2 - BULLET_SIZE / 2,
                                       enemy_y + B_SIZE / 2 - BULLET_SIZE / 2,
                                       BULLET_SIZE, BULLET_SIZE))


def set_bullets(self, t_coords, e_coords):
        for _ in t_coords:
            bullet = Bullet(self.display)
            in_range = bullet.range(t_coords, e_coords, t_green_aoe)
            if in_range:
                bullet.update(e_coords)
