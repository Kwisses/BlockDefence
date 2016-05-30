import pygame
from BlockDefence.game_files.settings import *


class Enemy(pygame.sprite.Sprite):

    def __init__(self, display, color, enemies):
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.color = color
        self.enemies = enemies

        self.image = pygame.Surface([B_SIZE, B_SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = 710
        self.rect.y = 0

        self.up = False
        self.down = True
        self.left = False
        self.right = False

        self.health = 0
        self.speed = 0

        self.enemies.add(self)

    def green(self):
        self.health = 5
        self.speed = 1

    def draw(self):
        self.enemies.draw(self.display)
        return self.rect.x, self.rect.y

    def direction(self):
        if self.rect.x == 710 and self.rect.y == 206:
            self.down = False
            self.left = True
        elif self.rect.x == 590 and self.rect.y == 206:
            self.left = False
            self.up = True
        elif self.rect.x == 590 and self.rect.y == 60:
            self.up = False
            self.left = True
        elif self.rect.x == 470 and self.rect.y == 60:
            self.left = False
            self.down = True
        elif self.rect.x == 470 and self.rect.y == 206:
            self.down = False
            self.left = True
        elif self.rect.x == 350 and self.rect.y == 206:
            self.left = False
            self.up = True
        elif self.rect.x == 350 and self.rect.y == 60:
            self.up = False
            self.left = True
        elif self.rect.x == 246 and self.rect.y == 60:
            self.left = False
            self.down = True
        elif self.rect.x == 246 and self.rect.y == 326:
            self.down = False
            self.right = True
        elif self.rect.x == 722 and self.rect.y == 326:
            self.right = False
            self.down = True
        elif self.rect.x == 722 and self.rect.y == 524:
            self.down = False
            self.left = True
        elif self.rect.x == 200 and self.rect.y == 524:
            self.left = False
        return [self.rect.x, self.rect.y]

    def update(self):
        if self.up:
            self.rect.y -= 1
        elif self.down:
            self.rect.y += 1
        elif self.left:
            self.rect.x -= 1
        elif self.right:
            self.rect.x += 1