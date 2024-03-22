"""
Constants.py
The constants file holds the constants used in the game.
"""

import pygame

pygame.font.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (128, 128, 128)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARK_GREY = (100, 100, 100)

#
ROWS, COLS = 8, 8
SQUARE_SIZE = 85
WIDTH, HEIGHT = 1000, 1000
BUTTON_WIDTH, BUTTON_HEIGHT = 300, 50
BUTTON_SPACING = 10

# Icons
DEFAULT_ICON_SIZE = (45, 45)
KING = pygame.transform.scale(pygame.image.load('pics/king_icon.png'), (44, 25))  # for king piece
LEADERBOARD_ICON = pygame.image.load('pics/leaderboard_icon.png')
START_GAME_ICON = pygame.image.load('pics/start_icon.png')
SETTINGS_ICON = pygame.image.load('pics/settings_icon.png')
TUTORIAL_ICON = pygame.image.load('pics/tutorial_icon.png')
BOARD_ICON = pygame.image.load('pics/colorwheel_icon.png')
BACKGROUND_IMAGE = pygame.image.load("checkers.jpg")
CHECKERS_ICON = pygame.image.load('pics/checkersguy_icon.png')
MUSIC_ICON = pygame.image.load('pics/music_icon.png')

# Fonts
FONT_64 = pygame.font.Font(None, 64)
FONT_48 = pygame.font.Font(None, 48)
FONT_32 = pygame.font.Font(None, 32)
FONT_24 = pygame.font.Font(None, 24)
