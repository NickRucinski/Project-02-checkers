"""
Main.py
The main file holds menu operations for the game including sound, settings, leaderboard, tutorial, and board customization.

"""
import pygame
from Button import Button
from Icon import Icon
from MainMenu import MainMenu
from MusicClass import BackgroundMusic
from Text import Text
from constants import *
from ScoreManager import ScoreManager
from SecondMenu import SecondMenu

pygame.init()
pygame.mixer.init()  # initialize pygame mixer for music

# set up the drawing window
Width, Height = 1000, 700  # updated size
screen = pygame.display.set_mode([Width, Height], pygame.RESIZABLE)
# title of the game for screen
pygame.display.set_caption("Checkers+")

music_manager = BackgroundMusic()
main_menu = MainMenu(screen, music_manager)


def main():
    """
    The main function is the main menu of the game. It displays the title, message, and credits, and holds user interaction with buttons. 
    If a user hovers over a button, the button will change GREY to indicate that it has been clicked. If the user clicks on a button,
    the corresponding function will be called.
    """

    running = True

    buttons = main_menu.menu_buttons()

    while running:
        global Width, Height
        Width = screen.get_width()
        Height = screen.get_height()
        mouse = pygame.mouse.get_pos()
        # did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.handle_click(event)
                # Check if the current song has finished, loop to next song
            elif event.type == music_manager.SONG_END:
                music_manager.music_loop()

        # image of the background
        background = pygame.transform.scale(BACKGROUND_IMAGE, (Width, Height))
        screen.blit(background, (0, 0))

        # display title information and credits
        main_menu.display_title_and_credits()

        for button in buttons:
            button.render()
            button.on_hover(mouse)

        pygame.display.flip()

    # done! time to quit
    pygame.quit()


music_manager.music_loop()
pygame.mixer.music.set_endevent(music_manager.SONG_END)  # create event for song ending/looping

main()
