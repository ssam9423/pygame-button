"""Button Module for Pygame"""

import pygame

class Button:
    """Class representing a Button"""

    def __init__(self, screen, name='Button', x_pos=0, y_pos=0,
                 bg_color=(96, 108, 56), t_color=(40, 54, 24),
                 hover_bg_color=(96, 108, 56), hover_t_color=(96, 108, 56),
                 disable_bg_color=(48, 42, 42), disable_t_color=(226, 226, 226),
                 default=0, hover=2,
                 font_name='yugothicuisemibold', font_size=25,
                 width=150, height=80, spacing_factor=10,
                 b_radius=2, static_size=False, clickable=True):
        """Initializes a Button onto a screen"""
        self.name = name                            # Text that appears on Button
        self.screen = screen
        self.bg_color = bg_color                    # Default Background Color
        self.t_color = t_color                      # Default Text Color
        self.hover_bg_color = hover_bg_color        # Hover Background Color
        self.hover_t_color = hover_t_color          # Hover Text Color
        self.disable_bg_color = disable_bg_color    # Disabled Background Color
        self.disable_t_color = disable_t_color      # Disabled Text Color
        self.default = default                      # Default Rect Fill-In or Outline
        self.hover = hover                          # Hover Rect Fill-In or Outline

        self.font_name = font_name
        self.font_size = font_size

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.w_factor = self.screen.get_size()[0] / self.width  # For Button
        self.h_factor = self.screen.get_size()[1] / self.height # For Button
        self.spacing_factor = spacing_factor                    # For Font
        self.w_spacing = self.width / self.spacing_factor       # For Font
        self.h_spacing = self.height / self.spacing_factor      # For Font
        self.b_radius = b_radius                                # Rounded Corners
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.static_size = static_size
        self.clickable = clickable

    def button_draw(self, button_color, text_color):
        """Draws Rect Representing the Button"""
        pygame.draw.rect(self.screen, button_color, self.rect,
                         self.default, border_radius=self.b_radius)
        self.text_blit(text_color)

    def text_blit(self, text_color):
        """Blits Text into center of Button"""
        button_surf = self.font.render(self.name, 1, text_color)
        text_width, text_height = button_surf.get_size()
        x_center = self.x_pos + (self.width - text_width) / 2
        y_center = self.y_pos + (self.height - text_height) / 2
        self.screen.blit(button_surf, (x_center, y_center))

    def show(self, mouse_pos):
        """Show Button - Hover, Default, or Disabled"""
        if self.clickable:
            if self.rect.collidepoint(mouse_pos):
                self.button_draw(self.hover_bg_color, self.hover_t_color)
            else:
                self.button_draw(self.bg_color, self.t_color)
        else:
            self.button_draw(self.disable_bg_color, self.disable_t_color)

    def update_screen(self, new_screen):
        """Takes in new screen and adjusts Button size based on screen size"""
        self.screen = new_screen
        if not self.static_size:
            self.width = new_screen.get_size()[0] / self.w_factor
            self.height = new_screen.get_size()[1] / self.h_factor
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def auto_font_size(self):
        """Finds and sets largest font size where text still fits on the Button"""
        curr_size = int(self.height)
        while curr_size > 1:
            f_w, f_h = pygame.font.SysFont(self.font_name, curr_size).size(self.name)
            if ((f_w < (self.width - (2 * self.w_spacing))) and
                (f_h < (self.height - (2 * self.h_spacing)))):
                break
            else:
                curr_size -= 1
        self.font_size = curr_size
        self.font = pygame.font.SysFont(self.font_name, self.font_size)

    def update_spacing_factor(self, new_spacing_factor):
        """Takes new spacing factor and adjusts width and height spacing"""
        self.spacing_factor = new_spacing_factor
        self.w_spacing = self.width / new_spacing_factor
        self.h_spacing = self.height / new_spacing_factor

    def update_button_size(self, new_width, new_height):
        """Takes new width and height and adjusts Rect"""
        self.width = new_width
        self.height = new_height
        self.rect = self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def update_position(self, new_x, new_y):
        """Takes new x_pos and y_pos and adjusts Rect"""
        self.x_pos = new_x
        self.y_pos = new_y
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def update_font_name(self, font_name):
        """Takes new font name and adjusts font"""
        self.font_name = font_name
        self.font = pygame.font.SysFont(self.font_name, self.font_size)

    def update_font_size(self, font_size):
        """Takes new font size and adjusts font"""
        self.font_size = font_size
        self.font = pygame.font.SysFont(self.font_name, self.font_size)

    def get_size_offset(self):
        """Returns x and y offset from middle of the Button"""
        return (int(self.width/2), int(self.height/2))

    def get_size(self):
        """Returns the Button's width and height"""
        return (self.width, self.height)

    def get_font_size(self):
        """Returns font size of text on Button"""
        return self.font.size(self.name)
