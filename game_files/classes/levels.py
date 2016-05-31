from pygame import time
from BlockDefence.game_files.classes.enemies import *
from BlockDefence.game_files.functions import *
from BlockDefence.game_files.settings import *


class LevelOne:

    def __init__(self, app, display, enemies, clock):
        self.app = app
        self.display = display
        self.enemies = enemies
        self.clock = clock

        self.enemy_instances = []
        self.enemy_num = 5
        self.spawn_time = 1000
        self.spawn_range = 0
        self.count = 0

        self.create_enemies()

    def create_enemies(self):
        for enemy in range(self.enemy_num):
            cpu_enemy = Enemy(self.display, green, self.enemies)
            self.enemy_instances.append(cpu_enemy)

    def show(self):
        label(self.app, "Level 1", black, size="s",
              x_displace=ALERT2[0], y_displace=ALERT2[1])
        self.count += self.clock.tick(FPS * 2)

        if self.count >= self.spawn_time:
            self.spawn_range += 1
            self.count = 0

        for enemy in self.enemy_instances[:self.spawn_range]:
            enemy.direction(self.app.lives)
            enemy.draw()
            enemy.update()


def level_switch(level=1):
    if level == 1:
        pass
