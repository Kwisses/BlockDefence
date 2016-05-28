from BlockDefence.game_files.functions import *
# from BlockDefence.game_files.settings import *
from BlockDefence.game_files.classes.enemies import *
from BlockDefence.game_files.classes.towers import *


class App:
    def __init__(self):
        pygame.init()

        # Display
        self.display = pygame.display.set_mode((main_width, main_height))
        self.icon = pygame.image.load(icon_path)
        self.icon_bg = pygame.image.load(icon_bg_path).convert()
        self.caption = pygame.display.set_caption(caption_path)

        self.MAP1 = pygame.image.load(map1_path).convert()
        self.CLOCK = pygame.time.Clock()

        # Game Logic
        self.intro = True
        self.tutorial = False
        self.start = True
        self.pause = False
        self.game_over = False
        self.game_exit = False

        self.purchase = False
        self.no_money_count = 0

        self.cur_change = False
        self.t_place = False

        # - Font size
        self.xs_font = pygame.font.SysFont("comicsansms", 15)
        self.s_font = pygame.font.SysFont("comicsansms", 25)
        self.m_font = pygame.font.SysFont("comicsansms", 50)
        self.l_font = pygame.font.SysFont("comicsansms", 75)

        # Objects
        self.b_color = green
        self.b_colors = []
        self.t_coords = []
        self.towers = []
        self.enemies = []

        # In-game settings
        self.money = 1000
        self.lives = 10

    def game_intro(self):
        self.CLOCK.tick(MENU_FPS)
        self.display.fill(black, [0, 0, menu_width, menu_height])
        self.display.blit(self.icon_bg, (main_width / 8, 15))

        label(self, "Block Defense", white, size="l",
              x_displace=main_width / 8 + 50,
              y_displace=-20)

        while self.intro:

            button(self, text="Play", x=main_width / 8 + 75,
                   y=main_height - 100,
                   width=125, height=50,
                   inactive_color=green, active_color=l_green, action="s")

            button(self, text="Tutorial", x=main_width / 8 + 395,
                   y=main_height - 100, width=125, height=50,
                   inactive_color=green, active_color=l_green, action="t")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()

    def game_tutorial(self):
        self.CLOCK.tick(MENU_FPS)
        self.display.fill(black)

        label(self, "Tutorial", white, size="l",
              x_displace=main_width / 4 + 60,
              y_displace=0)

        label(self, "Destroy all blocks before they reach you", white,
              size="s", x_displace=100, y_displace=200)
        label(self, "Use the Menu on the left to build turrets", white,
              size="s", x_displace=100, y_displace=250)

        label(self, "You have 10 lives and 10 levels to beat; P to pause",
              white, size="s", x_displace=100, y_displace=300)

        while self.tutorial:

            button(self, text="Back", x=main_width / 2 - 63,
                   y=main_height - 100,
                   width=125, height=50,
                   inactive_color=red, active_color=l_red, action="b")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()

    def game_pause(self):
        self.CLOCK.tick(MENU_FPS)

        label(self, "Paused", black, size="m",
              x_displace=main_width / 2 - 50,
              y_displace=main_height / 3 - 25)

        label(self, "Press P to continue", black, size="m",
              x_displace=main_width / 2 - 150,
              y_displace=main_height / 2)

        pygame.display.update()

        while self.pause:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause = False

    def game_loop(self):
        self.game_intro()

        while not self.game_exit:
            self.CLOCK.tick(FPS)

            self.display.fill(black, [0, 0, menu_width, menu_height])
            self.display.blit(self.MAP1, (menu_width, 0))

            cursor = list(pygame.mouse.get_pos())
            pix_color = self.display.get_at(pygame.mouse.get_pos())

            # Menu Labels (text)
            label(self, "Menu", red, size="s",
                  x_displace=menu_width / 4 + 20,
                  y_displace=0)
            label(self, "Block", white, size="xs",
                  x_displace=menu_width / 8,
                  y_displace=menu_height / 8 - 30)
            label(self, "Price", white, size="xs",
                  x_displace=menu_width / 8 + 100,
                  y_displace=menu_height / 8 - 30)
            label(self, "Money: $%s" % self.money, white, size="s",
                  x_displace=menu_width / 20,
                  y_displace=menu_height - 50)
            label(self, "Lives: %s" % self.lives, white, size="s",
                  x_displace=menu_width / 8 + 25,
                  y_displace=menu_height - 215)
            label(self, "$5", white, size="xs",
                  x_displace=menu_width / 8 + 100,
                  y_displace=menu_height / 8)
            label(self, "$10", white, size="xs",
                  x_displace=menu_width / 8 + 100,
                  y_displace=menu_height / 4)
            label(self, "$25", white, size="xs",
                  x_displace=menu_width / 8 + 100,
                  y_displace=menu_height / 2 - menu_height / 8)
            label(self, "$100", white, size="xs",
                  x_displace=menu_width / 8 + 100,
                  y_displace=menu_height / 2)

            # Menu Buttons
            button(self, text="Start", x=menu_width / 8 + 10, y=475,
                   width=125, height=50, inactive_color=red,
                   active_color=l_red, action="s")
            button(self, x=menu_width / 8, y=menu_height / 8,
                   width=B_SIZE, height=B_SIZE, inactive_color=green,
                   active_color=l_green, action="twr")
            button(self, x=menu_width / 8, y=menu_height / 4,
                   width=B_SIZE, height=B_SIZE, inactive_color=blue,
                   active_color=l_blue, action="twr")
            button(self, x=menu_width / 8, y=menu_height / 2 - menu_height / 8,
                    width=B_SIZE, height=B_SIZE, inactive_color=yellow,
                   active_color=l_yellow, action="twr")
            button(self, x=menu_width / 8, y=menu_height / 2,
                   width=B_SIZE, height=B_SIZE, inactive_color=purple,
                   active_color=l_purple, action="twr")

            # Function calls
            set_towers(self, self.b_colors, self.t_coords)

            # Testing this function...
            Enemy(self.display, green).update()

            # Conditionals
            if self.purchase:
                sub_money(self, self.b_color)

            if self.cur_change:
                if enough_money(self):
                    block_mouse(self, self.b_color, cursor)
                else:
                    not_enough_money(self)

            if pix_color == l_red:
                self.t_place = True
            else:
                self.t_place = False

            # Event Handler
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause = True
                        self.game_pause()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.cur_change and self.t_place:
                            self.t_coords.append(cursor)
                            self.b_colors.append(self.b_color)
                            self.cur_change = False
                            self.purchase = True  # -- So far, best spot

            pygame.display.update()

        pygame.quit()
        quit()
