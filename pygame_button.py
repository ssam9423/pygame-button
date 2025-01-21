# Button Module for Pygame

import pygame

class Button:
    def __init__(self, name, screen, bg_color, t_color, x_pos, y_pos):
        self.name = name
        self.screen = screen
        self.bg_color = bg_color
        self.t_color = t_color
        self.hover_bg_color = bg_color
        self.hover_t_color = bg_color
        self.default = 0                # Button Color Fill
        self.hover = 2                  # Button Color Fill

        self.font_name = 'yugothicuisemibold'
        self.font_size = 20

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.w_factor = 5
        self.h_factor = 10
        self.spacing_factor = 15
        self.width = self.screen.get_size()[0] / self.w_factor
        self.height = self.screen.get_size()[1] / self.h_factor
        self.w_spacing = self.width / self.spacing_factor
        self.h_spacing = self.height / self.spacing_factor
        self.b_radius = 2
        self.static_size = False
        
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.font = pygame.font.SysFont(self.font_name, self.font_size)

    def default_draw(self):
        pygame.draw.rect(self.screen, self.bg_color, self.rect, 
                         self.default, border_radius=self.b_radius)
        button_surf = self.font.render(self.name, 1, self.t_color)
        text_width, text_height = button_surf.get_size()
        x_center = self.x_pos + (self.width - text_width) / 2
        y_center = self.y_pos + (self.height - text_height) / 2
        self.screen.blit(button_surf, (x_center, y_center))

    def hover_draw(self):
        pygame.draw.rect(self.screen, self.hover_bg_color, self.rect, 
                         self.hover, border_radius=self.b_radius)
        button_surf = self.font.render(self.name, 1, self.hover_bg_color)
        text_width, text_height = button_surf.get_size()
        x_center = self.x_pos + (self.width - text_width) / 2
        y_center = self.y_pos + (self.height - text_height) / 2
        self.screen.blit(button_surf, (x_center, y_center))

    def show(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.hover_draw()
        else:
            self.default_draw()

    def update_screen(self, new_screen):
        self.screen = new_screen
        if not self.static_size:
            self.width = new_screen.get_size()[0] / self.w_factor
            self.height = new_screen.get_size()[1] / self.h_factor
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def auto_font_size(self):
        curr_size = int(self.height)
        while curr_size > 1:
            f_w, f_h = pygame.font.SysFont(self.font_name, curr_size).size(self.name)
            if ((f_w < (self.width - (2 * self.spacing_factor))) and
                (f_h < (self.height - (2 * self.spacing_factor)))):
                break
            else:
                curr_size -= 1
        self.font_size = curr_size
        self.font = pygame.font.SysFont(self.font_name, self.font_size)

    def update_spacing(self, new_spacing):
        self.spacing_factor = new_spacing
        self.w_spacing = self.width / new_spacing
        self.h_spacing = self.height / new_spacing

    def get_size_offset(self):
        return (self.width/2, self.height/2)
    
    def get_size(self):
        return (self.width, self.height)
    
    def get_font_size(self):
        return self.font.size(self.name)