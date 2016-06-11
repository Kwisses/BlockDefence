from BlockDefence.game_files.classes.bullets import *
from BlockDefence.game_files.classes.levels import *
from BlockDefence.game_files.classes.towers import *


class App:
    """Contains the main game screens and the main game loop."""

    def __init__(self):
        """Set game display settings, game logic, fonts, and levels."""
        pygame.init()

        # In-game Settings
        self.money = money
        self.lives = lives

        # Display
        self.display = pygame.display.set_mode((main_width, main_height))
        self.icon = pygame.image.load(icon_path)
        self.icon_bg = pygame.image.load(icon_bg_path).convert()
        self.set_caption = pygame.display.set_caption(caption_path)
        self.set_icon = pygame.display.set_icon(self.icon)
        self.MAP1 = pygame.image.load(map1_path).convert()
        self.CLOCK = pygame.time.Clock()

        # Game Logic
        self.intro = True
        self.tutorial = False
        self.start = True
        self.pause = False
        self.over = False
        self.win = False
        self.game_exit = False

        self.purchase = False
        self.no_money_count = 0

        self.cur_change = False
        self.t_place = False

        self.start_level = False

        # - Font size
        self.xs_font = pygame.font.SysFont("comicsansms", 15)
        self.s_font = pygame.font.SysFont("comicsansms", 25)
        self.m_font = pygame.font.SysFont("comicsansms", 50)
        self.l_font = pygame.font.SysFont("comicsansms", 75)

        # Objects
        self.b_color = green
        self.b_colors = []
        self.t_coords = []
        self.e_coords = []
        self.towers = []
        self.enemies = pygame.sprite.Group()

        # Levels (contains enemy init)
        self.current_level = 1

        self.level_1 = LevelOne(self, self.display, self.enemies, self.CLOCK)
        self.level_2 = LevelTwo(self, self.display, self.enemies, self.CLOCK)
        self.level_3 = LevelThree(self, self.display, self.enemies, self.CLOCK)
        self.level_4 = LevelFour(self, self.display, self.enemies, self.CLOCK)
        self.level_5 = LevelFive(self, self.display, self.enemies, self.CLOCK)
        self.level_6 = LevelSix(self, self.display, self.enemies, self.CLOCK)
        self.level_7 = LevelSeven(self, self.display, self.enemies, self.CLOCK)
        self.level_8 = LevelEight(self, self.display, self.enemies, self.CLOCK)
        self.level_9 = LevelNine(self, self.display, self.enemies, self.CLOCK)
        self.level_10 = LevelTen(self, self.display, self.enemies, self.CLOCK)

        self.total_enemies = len(self.enemies)

    def game_intro(self):
        """Display the main menu for the game."""
        self.CLOCK.tick(MENU_FPS)
        self.display.fill(black)
        self.display.blit(self.icon_bg, (main_width / 8, 15))

        label(self, "Block Defence", white, size="l",
              x_displace=main_width / 8 + 50,
              y_displace=-20)

        label(self, "v.1.0.0", white, size="xs",
              x_displace=10,
              y_displace=575)

        label(self, "© 2016 Kwistech", white, size="xs",
              x_displace=main_width - 125,
              y_displace=575)

        while self.intro:

            button(self, text="Play", x=main_width / 8 + 75,
                   y=main_height - 100,
                   width=125, height=50,
                   inactive_color=green, active_color=l_green, action="p")
            button(self, text="Tutorial", x=main_width / 8 + 395,
                   y=main_height - 100, width=125, height=50,
                   inactive_color=green, active_color=l_green, action="t")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()

    def game_tutorial(self):
        """Display the tutorial screen for the game."""
        self.CLOCK.tick(MENU_FPS)
        self.display.fill(black)

        label(self, "Tutorial", white, size="l",
              x_displace=main_width / 4 + 60,
              y_displace=0)
        label(self, "- Destroy all blocks before they reach the end", white,
              size="s", x_displace=100, y_displace=200)
        label(self, "- Use the Menu on the left to build towers", white,
              size="s", x_displace=100, y_displace=250)
        label(self, "- You have 3 lives and 10 levels to beat",
              white, size="s", x_displace=100, y_displace=300)
        label(self, "- Press P to pause the game",
              white, size="s", x_displace=100, y_displace=350)

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
        """Display the pause screen in game_loop()."""
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

    def game_over(self):
        """Display the game-over screen in game_loop()."""
        self.CLOCK.tick(MENU_FPS)

        label(self, "GAME OVER", black, size="m",
              x_displace=main_width / 2 - 40,
              y_displace=main_height / 3 - 25)
        label(self, "Press Enter for main menu", black, size="s",
              x_displace=main_width / 2 - 50,
              y_displace=main_height / 2 + 25)

        while self.over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Resets the game parameters
                        self.__init__()
                        self.display.fill(black)
                        self.current_level = 1
                        self.game_exit = True
                        self.over = False
                        self.intro = True
                        self.game_intro()

            pygame.display.update()

    def game_win(self):
        """Display the win screen in game_loop()."""
        self.CLOCK.tick(MENU_FPS)

        label(self, "You Win!", black, size="m",
              x_displace=main_width / 2 - 75,
              y_displace=main_height / 3 - 25)
        label(self, "Press Enter for main menu", black, size="s",
              x_displace=main_width / 2 - 50,
              y_displace=main_height / 2 + 25)

        while self.win:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Resets the game parameters
                        self.__init__()
                        self.display.fill(black)
                        self.current_level = 1
                        self.game_exit = True
                        self.over = False
                        self.intro = True
                        self.game_intro()

            pygame.display.update()

    def game_loop(self):
        """Display the game loop and handle game_over and game_win methods."""
        self.game_intro()

        while not self.game_exit:
            self.CLOCK.tick(FPS)

            self.display.blit(self.MAP1, (menu_width, 0))

            # Sets Purchased Towers - placed here to avoid aoe bleed into menu.
            set_towers(self, self.b_colors, self.t_coords)

            self.display.fill(black, [0, 0, menu_width, menu_height])

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

            # Game Over
            if not self.lives:
                self.over = True
                self.game_over()

            if self.current_level == 11:
                self.win = True
                self.game_win()

            # Life Handler
            for enemy in self.enemies:
                if enemy.rect.x == 200 and enemy.rect.y == 524:
                    self.lives -= 1

            # Tower Purchase
            if self.purchase:
                sub_money(self, self.b_color)

            # Cursor Change
            if self.cur_change:
                if enough_money(self):
                    block_mouse(self, self.b_color, cursor)
                else:
                    not_enough_money(self)

            # Tower Placement (only on red)
            if pix_color == l_red:
                self.t_place = True
            else:
                self.t_place = False

            # Level Handler
            if self.start_level:
                if self.current_level == 1:
                    show(self.level_1)
                    end_level(self, self.level_1.total_enemies)
                elif self.current_level == 2:
                    show(self.level_2)
                    end_level(self, self.level_2.total_enemies)
                elif self.current_level == 3:
                    show(self.level_3)
                    end_level(self, self.level_3.total_enemies)
                elif self.current_level == 4:
                    show(self.level_4)
                    end_level(self, self.level_4.total_enemies)
                elif self.current_level == 5:
                    show(self.level_5)
                    end_level(self, self.level_5.total_enemies)
                elif self.current_level == 6:
                    show(self.level_6)
                    end_level(self, self.level_6.total_enemies)
                elif self.current_level == 7:
                    show(self.level_7)
                    end_level(self, self.level_7.total_enemies)
                elif self.current_level == 8:
                    show(self.level_8)
                    end_level(self, self.level_8.total_enemies)
                elif self.current_level == 9:
                    show(self.level_9)
                    end_level(self, self.level_9.total_enemies)
                elif self.current_level == 10:
                    show(self.level_10)
                    end_level(self, self.level_10.total_enemies)

            # Bullet Handler
            if self.e_coords:
                set_bullets(self, self.t_coords, self.e_coords, self.b_colors)

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
                    if event.button == 3:
                        self.cur_change = False

            pygame.display.update()

        pygame.quit()
        quit()
