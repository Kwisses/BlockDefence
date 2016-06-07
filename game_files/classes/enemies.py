from BlockDefence.game_files.functions import *
from BlockDefence.game_files.settings import *


class Enemy(pygame.sprite.Sprite):
    """Enemy instance inherits from pygame.sprite.Sprite."""

    def __init__(self, display, color, enemies):
        """Set init for enemy instance.

        Args:
            display (pygame.Surface): Display to blit enemy to.
            color (tuple): Color of enemy.
            enemies (pygame.sprite.Group): Contains all enemy sprites.
        """
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.color = color
        self.enemies = enemies

        self.image = pygame.Surface([B_SIZE, B_SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = B_SPAWN_X
        self.rect.y = B_SPAWN_Y

        self.up = False
        self.down = True
        self.left = False
        self.right = False

        self.health = 0
        self.speed = 1

        if self.color == green:
            self.green()
        elif self.color == blue:
            self.blue()
        elif self.color == yellow:
            self.yellow()
        elif self.color == purple:
            self.purple()

        self.enemies.add(self)

    def green(self):
        """Define enemy parameters for a green enemy block."""
        self.health = green_health
        self.speed = green_speed

    def blue(self):
        """Define enemy parameters for a blue enemy block."""
        self.health = blue_health
        self.speed = blue_speed

    def yellow(self):
        """Define enemy parameters for a yellow enemy block."""
        self.health = yellow_health
        self.speed = yellow_speed

    def purple(self):
        """Define enemy parameters for a purple enemy block."""
        self.health = purple_health
        self.speed = purple_speed

    def draw(self):
        """Draw enemies to game screen."""
        self.enemies.draw(self.display)

    def direction(self):
        """Control enemy block movement around the map.

        Note that there are very specific coordinates that the blocks must
        reach. Because of this, the enemy speed can only be 1 or 2. If it is
        higher, the blocks will not reach these coordinates and continue on
        their path south.

        Once an enemy block reaches the last elif coordinates, a life is
        subtracted and the block (sprite) is removed from the sprite group."""
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
            self.enemies.remove(self)
        return [self.rect.x, self.rect.y]

    def update(self, app, e_coords):
        """Update the enemy health and enemy movement.

        Args:
            app (class App): Main game class.
            e_coords (list): Contains all enemy Sprites.
        """
        if self.health <= 0:
            if self in e_coords:
                e_coords.remove(self)
                self.enemies.remove(self)
                add_money(app, self.color)

        if self.up:
            self.rect.y -= self.speed
        elif self.down:
            self.rect.y += self.speed
        elif self.left:
            self.rect.x -= self.speed
        elif self.right:
            self.rect.x += self.speed
