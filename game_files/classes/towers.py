import pygame
from BlockDefence.game_files.settings import *


class Tower:

    def __init__(self, coords):
        self.coords = coords

        self.damage = 0
        self.range = 0

        self.aoe()

    def green(self):
        self.damage = 1
        self.range = t_green_aoe

    def aoe(self):
        n_edge = self.coords[1] - self.range
        s_edge = self.coords[1] + self.range
        e_edge = self.coords[0] + self.range
        w_edge = self.coords[0] - self.range
        return n_edge, s_edge, e_edge, w_edge


def set_towers(self, colors, coords):
    for i, coord in enumerate(coords):
        block = pygame.draw.rect(self.display, colors[i],
                                 (coord[0] - B_SIZE / 2,
                                  coord[1] - B_SIZE / 2,
                                  B_SIZE, B_SIZE))

        aoe = pygame.draw.rect(self.display, colors[i],
                                 (coord[0] - t_green_aoe / 2,
                                  coord[1] - t_green_aoe / 2,
                                  t_green_aoe, t_green_aoe), 1)

        self.display.blit(self.display, block, (coord[0] - B_SIZE / 2,
                                                coord[1] - B_SIZE / 2,
                                                B_SIZE, B_SIZE))

        self.display.blit(self.display, aoe, (coord[0] - t_green_aoe / 2,
                                              coord[1] - t_green_aoe / 2,
                                              t_green_aoe, t_green_aoe))
