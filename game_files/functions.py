import pygame
from BlockDefence.game_files.settings import *


def text_objects(self, text, color, size):
    # Parameters for Render are: (text, antialias, color)
    text_surface = self.xs_font.render(text, True, color)
    if size == "xs":
        text_surface = self.xs_font.render(text, False, color)
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
                self.start = True
            if action == "p":
                self.intro = False
            if action == "t":
                self.tutorial = True
            if action == "b":
                pass
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
