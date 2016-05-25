from BlockDefence.game_files.functions import *
from BlockDefence.game_files.settings import *


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
        self.pause = False
        self.game_over = False
        self.game_exit = False

        # - Font size
        self.xs_font = pygame.font.SysFont("comicsansms", 15)
        self.s_font = pygame.font.SysFont("comicsansms", 25)
        self.m_font = pygame.font.SysFont("comicsansms", 50)
        self.l_font = pygame.font.SysFont("comicsansms", 75)

    def game_intro(self):
        self.display.fill(black, [0, 0, menu_width, menu_height])
        self.display.blit(self.icon_bg, (main_width / 8, 15))

        label(self, "Block Defense", white, size="l",
              x_displace=main_width / 8 + 50,
              y_displace=-20)

        while self.intro:
            self.CLOCK.tick(MENU_FPS)

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
            self.CLOCK.tick(MENU_FPS)

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
        label(self, "Paused", black, size="m",
              x_displace=main_width / 2 - 50,
              y_displace=main_height / 3 - 25)

        label(self, "Press P to continue", black, size="m",
              x_displace=main_width / 2 - 150,
              y_displace=main_height / 2)

        while self.pause:
            self.CLOCK.tick(MENU_FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause = False

            pygame.display.update()

    def game_loop(self):
        self.game_intro()

        while not self.game_exit:

            self.CLOCK.tick(FPS)

            self.display.fill(black, [0, 0, menu_width, menu_height])
            self.display.blit(self.MAP1, (menu_width, 0))

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
            label(self, "Money: $%s" % money, white, size="s",
                  x_displace=menu_width / 20,
                  y_displace=menu_height - 50)
            label(self, "Lives: %s" % lives, white, size="s",
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
                   width=125, height=50,
                   inactive_color=red, active_color=l_red, action="s")
            button(self, x=menu_width / 8, y=menu_height / 8,
                   width=B_SIZE, height=B_SIZE,
                   inactive_color=green, active_color=l_green)
            button(self, x=menu_width / 8, y=menu_height / 4,
                   width=B_SIZE, height=B_SIZE,
                   inactive_color=blue, active_color=l_blue)
            button(self, x=menu_width / 8, y=menu_height / 2 - menu_height / 8,
                    width=B_SIZE, height=B_SIZE,
                    inactive_color=yellow, active_color=l_yellow)
            button(self, x=menu_width / 8, y=menu_height / 2,
                   width=B_SIZE, height=B_SIZE,
                   inactive_color=purple, active_color=l_purple)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.game_exit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause = True
                        self.game_pause()

            pygame.display.update()

        pygame.quit()
        quit()
