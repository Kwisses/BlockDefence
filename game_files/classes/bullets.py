import pygame
from BlockDefence.game_files.settings import *


class Bullet:
    def __init__(self, display, color):
        self.display = display
        self.color = color

        self.dmg = 0
        self.fire = False

        if self.color == green:
            self.dmg = t_green_dmg
        elif self.color == blue:
            self.dmg = t_blue_dmg
        elif self.color == yellow:
            self.dmg = t_yellow_dmg
        elif self.color == purple:
            self.dmg = t_purple_dmg

    def in_range(self, t_x, t_y, e_coords, aoe):
        for e in e_coords:
            e_x, e_y = e.rect.x, e.rect.y
            if abs(e_x - (t_x - B_SIZE / 2)) <= aoe / 2:
                if abs(e_y - (t_y - B_SIZE / 2)) <= aoe / 2:
                    if not self.fire:
                        pygame.draw.rect(self.display, red,
                                         (e_x + B_SIZE / 2 - BULLET_SIZE / 2,
                                          e_y + B_SIZE / 2 - BULLET_SIZE / 2,
                                          BULLET_SIZE, BULLET_SIZE))
                        e.health -= self.dmg
                    self.fire = True


def set_bullets(self, t_coords, e_coords, colors):
    for i, tower in enumerate(t_coords):
        t_x, t_y = tower
        aoe = colors[i]

        if aoe == green:
            aoe = t_green_aoe
        elif aoe == blue:
            aoe = t_blue_aoe
        elif aoe == yellow:
            aoe = t_yellow_aoe
        elif aoe == purple:
            aoe = t_purple_aoe

        bullet = Bullet(self.display, colors[i])
        bullet.in_range(t_x, t_y, e_coords, aoe)
