import pygame
from BlockDefence.game_files.settings import *


class Tower:

    def __init__(self, coords):
        self.coords = coords


def set_towers(self, colors, coords):
    for i, coord in enumerate(coords):
        aoe = colors[i]

        if aoe == green:
            aoe = t_green_aoe
        elif aoe == blue:
            aoe = t_blue_aoe
        elif aoe == yellow:
            aoe = t_yellow_aoe
        elif aoe == purple:
            aoe = t_purple_aoe

        block = pygame.draw.rect(self.display, colors[i],
                                 (coord[0] - B_SIZE / 2,
                                  coord[1] - B_SIZE / 2,
                                  B_SIZE, B_SIZE))

        aoe_block = pygame.draw.rect(self.display, colors[i],
                                     (coord[0] - aoe / 2,
                                      coord[1] - aoe / 2,
                                      aoe, aoe), 1)

        self.display.blit(self.display, block, (coord[0] - B_SIZE / 2,
                                                coord[1] - B_SIZE / 2,
                                                B_SIZE, B_SIZE))

        self.display.blit(self.display, aoe_block, (coord[0] - aoe / 2,
                                                    coord[1] - aoe / 2,
                                                    aoe, aoe))
