from pygame import Surface

from constants import *
import pygame

from Icon import Icon


class Button:
    def __init__(self, button_text, screen: pygame.display, position, size: tuple[int, int], color,
                 icon: Surface = None, font=pygame.font.Font(None, 32)):
        self.button_text = button_text
        self.screen = screen
        self.position = position
        self.button_size = size
        self.color = color
        self.font = font
        self.area = pygame.Rect(position, size)
        self.onclick_function = None
        self.icon = icon
        self.hover = False
        self.render()

    def render(self):
        # Draw the button background
        pygame.draw.rect(self.screen, self.color, self.area)

        # Render and position the button text
        button_text_render = self.font.render(self.button_text, True, WHITE)
        button_text_rect = button_text_render.get_rect(center=self.area.center)

        # Render the icon if it exists
        if self.icon is not None:
            Icon(
                self.screen,
                DEFAULT_ICON_SIZE,
                None,
                self.position,
                self.icon
            ).render_image_icon()

        # Blit the text onto the button
        self.screen.blit(button_text_render, button_text_rect)

        # Update only the portion of the screen where the button is located
        pygame.display.update(self.area)

    def change_state(self, new_button_color):
        self.color = new_button_color
        self.render()

    def set_on_click_listener(self, onclick_function):
        self.onclick_function = onclick_function

    def handle_click(self, event):
        if self.hover and self.onclick_function is not None:
            self.onclick_function()

    def on_hover(self, mouse):
        if self.area.collidepoint(mouse):
            self.hover = True
            self.change_state(DARK_GREY)
        else:
            self.hover = False
            self.change_state(GREY)
