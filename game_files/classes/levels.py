from BlockDefence.game_files.classes.enemies import *
from BlockDefence.game_files.functions import *
from BlockDefence.game_files.settings import *


class LevelOne(object):

    def __init__(self, app, display, enemies, clock):
        self.app = app
        self.display = display
        self.enemies = enemies
        self.clock = clock

        self.level_text = "Level 1"
        self.enemy_instances = []

        # Enemy Parameters
        self.group_enemies = 5
        self.single_enemies = 0
        self.total_enemies = self.group_enemies + self.single_enemies

        self.spawn_time = 1000
        self.spawn_range = 0
        self.count = 0

        create_enemies(self, green)


class LevelTwo(LevelOne):

    def __init__(self, app, display, enemies, clock):
        super().__init__(app, display, enemies, clock)

        self.level_text = "Level 2"
        self.enemy_instances = []

        # Enemy Parameters
        self.group_enemies = 5
        self.single_enemies = 2
        self.total_enemies = self.group_enemies + self.single_enemies

        self.spawn_time = 950
        self.spawn_range = 0
        self.count = 0

        create_enemies(self, green)
        create_enemy(self, blue)
        create_enemy(self, blue)


class LevelThree(LevelOne):

    def __init__(self, app, display, enemies, clock):
        super().__init__(app, display, enemies, clock)

        self.level_text = "Level 3"
        self.enemy_instances = []

        # Enemy Parameters
        self.group_enemies = 3
        self.single_enemies = 1
        self.total_enemies = (self.group_enemies * 2) + self.single_enemies

        self.spawn_time = 900
        self.spawn_range = 0
        self.count = 0

        create_enemies(self, green)
        create_enemies(self, blue)
        create_enemy(self, yellow)


class LevelFour(LevelOne):

    def __init__(self, app, display, enemies, clock):
        super().__init__(app, display, enemies, clock)

        self.level_text = "Level 4"
        self.enemy_instances = []

        # Enemy Parameters
        self.group_enemies = 3
        self.single_enemies = 1
        self.total_enemies = (self.group_enemies * 2) + self.single_enemies

        self.spawn_time = 850
        self.spawn_range = 0
        self.count = 0

        create_enemy(self, green)
        create_enemies(self, blue)
        create_enemies(self, yellow)


class LevelFive(LevelOne):

    def __init__(self, app, display, enemies, clock):
        super().__init__(app, display, enemies, clock)

        self.level_text = "Level 5"
        self.enemy_instances = []

        # Enemy Parameters
        self.group_enemies = 2
        self.single_enemies = 1
        self.total_enemies = (self.group_enemies * 4) + self.single_enemies

        self.spawn_time = 800
        self.spawn_range = 0
        self.count = 0

        create_enemies(self, green)
        create_enemies(self, blue)
        create_enemies(self, blue)
        create_enemies(self, yellow)
        create_enemy(self, purple)


class LevelSix(LevelOne):

    def __init__(self, app, display, enemies, clock):
        super().__init__(app, display, enemies, clock)

        self.level_text = "Level 6"
        self.enemy_instances = []

        # Enemy Parameters
        self.group_enemies = 4
        self.single_enemies = 2
        self.total_enemies = (self.group_enemies * 3) + self.single_enemies

        self.spawn_time = 750
        self.spawn_range = 0
        self.count = 0

        create_enemies(self, green)
        create_enemies(self, blue)
        create_enemies(self, yellow)
        create_enemy(self, purple)
        create_enemy(self, purple)


class LevelSeven(LevelOne):

    def __init__(self, app, display, enemies, clock):
        super().__init__(app, display, enemies, clock)

        self.level_text = "Level 7"
        self.enemy_instances = []

        # Enemy Parameters
        self.group_enemies = 4
        self.single_enemies = 0
        self.total_enemies = (self.group_enemies * 5) + self.single_enemies

        self.spawn_time = 700
        self.spawn_range = 0
        self.count = 0

        create_enemies(self, green)
        create_enemies(self, green)
        create_enemies(self, blue)
        create_enemies(self, yellow)
        create_enemies(self, purple)


class LevelEight(LevelOne):

    def __init__(self, app, display, enemies, clock):
        super().__init__(app, display, enemies, clock)

        self.level_text = "Level 8"
        self.enemy_instances = []

        # Enemy Parameters
        self.group_enemies = 5
        self.single_enemies = 1
        self.total_enemies = (self.group_enemies * 4) + self.single_enemies

        self.spawn_time = 650
        self.spawn_range = 0
        self.count = 0

        create_enemies(self, green)
        create_enemy(self, yellow)
        create_enemies(self, blue)
        create_enemies(self, yellow)
        create_enemies(self, purple)


class LevelNine(LevelOne):

    def __init__(self, app, display, enemies, clock):
        super().__init__(app, display, enemies, clock)

        self.level_text = "Level 9"
        self.enemy_instances = []

        # Enemy Parameters
        self.group_enemies = 6
        self.single_enemies = 2
        self.total_enemies = (self.group_enemies * 5) + self.single_enemies

        self.spawn_time = 600
        self.spawn_range = 0
        self.count = 0

        create_enemies(self, green)
        create_enemies(self, blue)
        create_enemies(self, yellow)
        create_enemies(self, blue)
        create_enemy(self, yellow)
        create_enemies(self, purple)
        create_enemy(self, purple)


class LevelTen(LevelOne):

    def __init__(self, app, display, enemies, clock):
        super().__init__(app, display, enemies, clock)

        self.level_text = "Level 10"
        self.enemy_instances = []

        # Enemy Parameters
        self.group_enemies = 5
        self.single_enemies = 0
        self.total_enemies = (self.group_enemies * 10) + self.single_enemies

        self.spawn_time = 500
        self.spawn_range = 0
        self.count = 0

        create_enemies(self, green)
        create_enemies(self, blue)
        create_enemies(self, yellow)
        create_enemies(self, green)
        create_enemies(self, purple)
        create_enemies(self, blue)
        create_enemies(self, yellow)
        create_enemies(self, purple)
        create_enemies(self, yellow)
        create_enemies(self, purple)


def create_enemies(self, color):
    for enemy in range(self.group_enemies):
        cpu_enemy = Enemy(self.display, color, self.enemies)
        self.enemy_instances.append(cpu_enemy)
        self.app.e_coords.append(cpu_enemy)


def create_enemy(self, color):
    cpu_enemy = Enemy(self.display, color, self.enemies)
    self.enemy_instances.append(cpu_enemy)
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
