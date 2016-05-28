import pygame
from BlockDefence.game_files.settings import *


class Enemy:

    def __init__(self, display, color):
        self.display = display
        self.color = color

        self.x = 710
        self.y = 0

        self.health = 0
        self.speed = 0

        self.up = False
        self.down = True
        self.left = False
        self.right = False

    def green(self):
        self.health = 5
        self.speed = 1

    def move(self):
        if self.up:
            self.y -= 1
        elif self.down:
            self.y += 1
        elif self.left:
            self.x -= 1
        elif self.right:
            self.x += 1

    def direction(self):
        if self.x == 710 and self.y == 206:
            self.down = False
            self.left = True
        elif self.x == 590 and self.y == 206:
            self.left = False
            self.up = True
        elif self.x == 590 and self.y == 60:
            self.up = False
            self.left = True
        elif self.x == 470 and self.y == 60:
            self.left = False
            self.down = True
        elif self.x == 470 and self.y == 206:
            self.down = False
            self.left = True
        elif self.x == 350 and self.y == 206:
            self.left = False
            self.up = True
        elif self.x == 350 and self.y == 60:
            self.up = False
            self.left = True
        elif self.x == 246 and self.y == 60:
            self.left = False
            self.down = True
        elif self.x == 246 and self.y == 326:
            self.down = False
            self.right = True
        elif self.x == 722 and self.y == 326:
            self.right = False
            self.down = True
        elif self.x == 722 and self.y == 524:
            self.down = False
            self.left = True
        elif self.x == 200 and self.y == 524:
            self.left = False

    def update(self):
        self.move()
        self.direction()
        create_enemy(self.display, self.color, self.x, self.y)
        return self.x, self.y


def create_enemy(display, color, x, y):
    block = pygame.draw.rect(display, color, (x, y, B_SIZE, B_SIZE))
    display.blit(display, block, (x, y, B_SIZE, B_SIZE))
