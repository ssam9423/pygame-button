# Pygame Button Class
## Description
This is a class to create buttons in Pygame.

## Initializing a Button - Parameters & Varaibles
To initialyze a Button, the following parameters are required:
- `name`: (string) text desplayed on the Button
- `screen`: (`pygame.surface.Surface` object) surface on which the Button is displayed
- `bg_color`: (tuple) background color of the Button
- `t_color`: (tuple) text color of the Button
- `x_pos`: (int) x-position of the Button
- `y_pos`: (int) y-position of the Button

The other parameters are optional:
- `hover_bg_color`: (tuple) background color of the Button when user's cursor is on the Button
- `hover_t_color`: (tuple) text color of the Button when the user's cursor is on the Button
- `default`: (int) integer determining if the `pygame.Rect` object is filled in or not
- `hover`: (int) integer determining if the `pygame.Rect` object is filled in or not when the user's cursor is on the Button
- `font_name`: (string) name of font for Button text
- `font_size`: (int) size of font for Button text
- `width`: (int) width of Button
- `height`: (int) height of Button
- `spacing_factor`: (int) factor determining the spacing size between the text on the Button and the Button
- `b_radius`: (int) radius of Button corners - for rounded corners
- `static_size`: (Boolean) determines if the size of the button adjusts with a change in screen size

## Functions
The Button class has multiple functions:
- `show(mouse_position)`: this function takes in a mouse position `pygame.mouse.get_pos()` and draws the appropriate Button depending on if the user's cursor is on the Button (default vs hover).
- `update_screen(screen)`: this funtion takes in a `pygame.surface.Surface` object and updates screen on which the Button is displayed on. If `static_size` is `False`, the Button's `width` and `height` are updated as well.
- `auto_font_size()`: this function updates the font size so that the text on the button fits within the button according to the Button's `w_spacing` and `h_spacing`
- `update_spacing(new_spacing)`: this function takes in an integer as the new `spacing_factor` and updates the `w_spacing` and `h_spacing`
- `get_size_offset()`: this function returns a pair of integers representing the offset from the Button's center
- `get_size()`: this function returns a pair of integers representing the `width` and `height` of the Button
- `get_font_size()`: this function returns a pair or integers representing the width and height of the text on the Button

## Example Code
Initialize the Button and make sure to use the `show()` function in the game loop to display the Button. 
If the `screen` is ever changed, make sure to use the `update_screen()` function and (optionally) `auto_font_size()`

```
# Initialize Pygame & Screen
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

# Initializing Button and displaying it in the center of the screen
bg_color = (100, 50, 50)
text_color = (200, 200, 200)
button = Button('Button', screen, color, text_color, 0, 0)
button.x_pos = 400 - button.get_size_offset()[0]
button.y_pos = 300 - button.get_size_offset()[1]

# Game Loop
game_on = True
while game_on:
    for event in pygame.event.get():
        screen.fill((232, 228, 218))
        # Check to Quit Game 
        if event.type == pygame.QUIT:
            game_on = False
        # Change Screen Size
        if event.type == pygame.VIDEORESIZE:
            # Update Screen Size
            screen = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
            # Update Button Position to remain in center of the screen
            button.x_pos = (screen.get_size()[0] / 2) - button.get_size_offset()[0]
            button.y_pos = (screen.get_size()[1] / 2) - button.get_size_offset()[1]
            # Update Screen & Font Size
            button.update_screen(screen)
            button.auto_font_size()
    # Show Button - either default or hover
    button.show(pygame.mouse.get_pos())
    pygame.display.update()
```
