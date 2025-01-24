# Button Module for Pygame
import pygame

class Button:
    def __init__(self, screen, name='Button', x_pos=0, y_pos=0,
                 bg_color=(96, 108, 56), t_color=(40, 54, 24), 
                 hover_bg_color=(96, 108, 56), hover_t_color=(96, 108, 56), 
                 disable_bg_color=(48, 42, 42), disable_t_color=(226, 226, 226), 
                 default=0, hover=2,
                 font_name='yugothicuisemibold', font_size=25,
                 width=150, height=80, spacing_factor=10,
                 b_radius=2, static_size=False, clickable=True):
        self.name = name
        self.screen = screen
        self.bg_color = bg_color
        self.t_color = t_color
        self.hover_bg_color = hover_bg_color
        self.hover_t_color = hover_t_color
        self.disable_bg_color = disable_bg_color
        self.disable_t_color = disable_t_color
        self.default = default          # Button Color Fill
        self.hover = hover              # Button Color Fill

        self.font_name = font_name
        self.font_size = font_size

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.w_factor = self.screen.get_size()[0] / self.width
        self.h_factor = self.screen.get_size()[1] / self.height
        self.spacing_factor = spacing_factor
        self.w_spacing = self.width / self.spacing_factor
        self.h_spacing = self.height / self.spacing_factor
        self.b_radius = b_radius
        self.static_size = static_size
        
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.clickable = clickable

    def button_draw(self, button_color, text_color):
        pygame.draw.rect(self.screen, button_color, self.rect, 
                         self.default, border_radius=self.b_radius)
        self.text_blit(text_color)
    
    def text_blit(self, text_color):
        button_surf = self.font.render(self.name, 1, text_color)
        text_width, text_height = button_surf.get_size()
        x_center = self.x_pos + (self.width - text_width) / 2
        y_center = self.y_pos + (self.height - text_height) / 2
        self.screen.blit(button_surf, (x_center, y_center))

    def show(self, mouse_pos):
        if self.clickable:
            if self.rect.collidepoint(mouse_pos):
                self.button_draw(self.hover_bg_color, self.hover_t_color)
            else:
                self.button_draw(self.bg_color, self.t_color)
        else:
            self.button_draw(self.disable_bg_color, self.disable_t_color)

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
            if ((f_w < (self.width - (2 * self.w_spacing))) and
                (f_h < (self.height - (2 * self.h_spacing)))):
                break
            else:
                curr_size -= 1
        self.font_size = curr_size
        self.font = pygame.font.SysFont(self.font_name, self.font_size)

    def update_spacing(self, new_spacing):
        self.spacing_factor = new_spacing
        self.w_spacing = self.width / new_spacing
        self.h_spacing = self.height / new_spacing

    def update_position(self, new_x, new_y):
        self.x_pos = new_x
        self.y_pos = new_y
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def update_font_name(self, font_name):
        self.font_name = font_name
        self.font = pygame.font.SysFont(self.font_name, self.font_size)

    def update_font_size(self, font_size):
        self.font_size = font_size
        self.font = pygame.font.SysFont(self.font_name, self.font_size)

    def get_size_offset(self):
        return (int(self.width/2), int(self.height/2))
    
    def get_size(self):
        return (self.width, self.height)
    
    def get_font_size(self):
        return self.font.size(self.name)
    
# pygame.init()
# screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

# color = (100, 50, 50)
# button = Button('Button', screen, color, (200, 200, 200), 0, 0)

# button.x_pos = 400 - button.get_size_offset()[0]
# button.y_pos = 300 - button.get_size_offset()[1]
# button.update_screen(screen)
# game_on = True


# while game_on:
#     for event in pygame.event.get():
#         screen.fill((232, 228, 218))
#         # Check to Quit Game 
#         if event.type == pygame.QUIT:
#             game_on = False
#         # Change screen size
#         if event.type == pygame.VIDEORESIZE:
#             # There's some code to add back window content here.
#             screen = pygame.display.set_mode((event.w, event.h),
#                                               pygame.RESIZABLE)
#             button.x_pos = (screen.get_size()[0] / 2) - button.get_size_offset()[0]
#             button.y_pos = (screen.get_size()[1] / 2) - button.get_size_offset()[1]
#             button.update_screen(screen)
#             button.auto_font_size()

#     button.show(pygame.mouse.get_pos())
#     pygame.display.update()
