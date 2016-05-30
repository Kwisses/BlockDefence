from BlockDefence.game_files.classes.enemies import *


class LevelOne:

    def __init__(self, display, enemies):
        self.display = display
        self.enemies = enemies

        self.e = []
        self.enemy_num = 2
        self.count = 0

        self.create_enemies()

    def create_enemies(self):
        for enemy in range(self.enemy_num):
            cpu_enemy = Enemy(self.display, green, self.enemies)
            self.e.append(cpu_enemy)

    def show(self):
        for x in self.e:
            x.direction()
            x.draw()
            x.update()
