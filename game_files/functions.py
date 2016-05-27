import pygame
from BlockDefence.game_files.settings import *
from BlockDefence.game_files.classes.towers import *


def text_objects(self, text, color, size):
    # Parameters for Render are: (text, antialias, color)
    text_surface = self.xs_font.render(text, True, color)
    if size == "xs":
        text_surface = self.xs_font.render(text, True, color)
    elif size == "s":
        text_surface = self.s_font.render(text, True, color)
    elif size == "m":
        text_surface = self.m_font.render(text, True, color)
    elif size == "l":
        text_surface = self.l_font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def label(self, text, color, size="s", x_displace=0, y_displace=0):
    text_surf, text_rect = text_objects(self, text, color, size)
    text_rect = (x_displace, y_displace)
    self.display.blit(text_surf, text_rect)


def button(self, text="", x=0, y=0, width=0, height=0,
           inactive_color=l_green, active_color=green, action=None):

    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(self.display, active_color, (x, y, width, height))
        if click[0] == 1:
            if action == "s":
                self.intro = False
            if action == "t":
                self.tutorial = True
                self.game_tutorial()
            if action == "b":
                self.tutorial = False
                self.game_intro()
            if action == "twr":
                self.b_color = inactive_color
                self.cur_change = True

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            tower = Tower(cur)
                            self.towers.append(tower)

                # self.purchase = True  # Need to find a better spot for this
    else:
        pygame.draw.rect(self.display, inactive_color, (x, y, width, height))

    text_to_button(self, self.display, text, black, x, y, width, height)


def text_to_button(self, display, text, color,
                   button_x, button_y, button_width, button_height, size="s"):
    """Writes text over an already created button via button().

    Args:
        self (game_loop.App): Game loop class App.
        display (pygame.Surface): Pygame game surface.
        text (str): Text that is placed onto the button
        color (tuple): Color to text; colors are defined as (R, G, B)
        button_x (float): x coordinate for button in game_display
        button_y (float): y coordinate for button in game_display
        button_width (int): Length of button
        button_height (int): Height of button
        size (str): Text (font) size as a string
    """
    text_surf, text_rect = text_objects(self, text, color, size)
    text_rect.center = ((button_x + button_width / 2),
                        button_y + button_height / 2)
    display.blit(text_surf, text_rect)


def block_mouse(self, color, cur):
    block = pygame.draw.rect(self.display, color,
                             (cur[0] - B_SIZE / 2,
                              cur[1] - B_SIZE / 2,
                              B_SIZE, B_SIZE))
    self.display.blit(self.display, block, (cur[0] - B_SIZE / 2,
                                            cur[1] - B_SIZE / 2,
                                            B_SIZE, B_SIZE))


def enough_money(self):
    if self.b_color == green and self.money >= t_cost_green:
        return True
    elif self.b_color == blue and self.money >= t_cost_blue:
        return True
    elif self.b_color == yellow and self.money >= t_cost_yellow:
        return True
    elif self.b_color == purple and self.money >= t_cost_purple:
        return True
    else:
        return False


def not_enough_money(self):
    if self.no_money_count == 30:
        self.no_money_count = 0
        self.cur_change = False
    else:
        label(self, "Not enough money!", black, size="s",
              x_displace=ALERT1[0], y_displace=ALERT1[1])
        self.no_money_count += 1


def sub_money(self, color):
    if color == green:
        self.money -= t_cost_green
    elif color == blue:
        self.money -= t_cost_blue
    elif color == yellow:
        self.money -= t_cost_yellow
    elif color == purple:
        self.money -= t_cost_purple
    self.purchase = False
