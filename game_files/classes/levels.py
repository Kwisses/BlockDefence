from BlockDefence.game_files.classes.enemies import *
from BlockDefence.game_files.functions import *
from BlockDefence.game_files.settings import *


class LevelOne(object):

    def __init__(self, app, display, enemies, clock):
        self.app = app
        self.display = display
        self.enemies = enemies
        self.clock = clock

        self.enemy_instances = []
        self.level_text = "Level 1"
        self.enemy_num = 2
        self.spawn_time = 1000
        self.spawn_range = 0
        self.count = 0

        create_enemies(self, green)


class LevelTwo(object):

    def __init__(self, app, display, enemies, clock):
        self.app = app
        self.display = display
        self.enemies = enemies
        self.clock = clock

        self.enemy_instances = []
        self.level_text = "Level 2"
        self.enemy_num = 5
        self.spawn_time = 1000
        self.spawn_range = 0
        self.count = 0

        create_enemies(self, blue)


def create_enemies(self, color):
    for enemy in range(self.enemy_num):
        cpu_enemy = Enemy(self.display, color, self.enemies)
        self.enemy_instances.append(cpu_enemy)
        # self.app.e_coords = self.enemy_instances
        self.app.e_coords.append(cpu_enemy)


def show(self):
    label(self.app, self.level_text, black, size="s",
          x_displace=ALERT2[0], y_displace=ALERT2[1])
    self.count += self.clock.tick(FPS * 2)

    if self.count >= self.spawn_time:
        self.spawn_range += 1
        self.count = 0

    for enemy in self.enemy_instances[:self.spawn_range]:
        enemy.direction()
        enemy.draw()
        enemy.update(self.app, self.app.e_coords)
