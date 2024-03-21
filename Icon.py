import pygame
from constants import *


class Icon:

    def __init__(self, screen: pygame.display, size: tuple[int, int], color, position, image=None):
        self.size = size
        self.color = color
        self.position = position
        self.screen = screen
        self.image = image
        self.area = pygame.Rect(position, size)

    def render_color_square(self):
        pygame.draw.rect(self.screen, self.color, self.area)

    def render_image_icon(self):
        icon_resized = pygame.transform.scale(self.image, self.size)
        icon_rect = icon_resized.get_rect(center=self.area.center)
        self.screen.blit(icon_resized, icon_rect)
