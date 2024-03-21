"""
Main.py
The main file holds menu operations for the game including sound, settings, leaderboard, tutorial, and board customization.

"""
import pygame
from Button import Button
from Icon import Icon
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

# background music
tracks = [
    "music/Track1.mp3",
    "music/Track2.mp3",
    "music/Track3.mp3",
    "music/Track4.mp3",
    "music/Track5.mp3",
    "music/Track6.mp3",
    "music/Track7.mp3",
    "music/Track8.mp3"
]  # can add more or delete tracks if we do not like them
current_track = 0
SONG_END = pygame.USEREVENT + 1
second_menu = SecondMenu(tracks)

def main():
    """
    The main function is the main menu of the game. It displays the title, message, and credits, and holds user interaction with buttons. 
    If a user hovers over a button, the button will change GREY to indicate that it has been clicked. If the user clicks on a button,
    the corresponding function will be called.
    """

    running = True

    buttons = menu_buttons()

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
            elif event.type == SONG_END:
                music_loop()

        # image of the background
        background = pygame.transform.scale(BACKGROUND_IMAGE, (Width, Height))
        screen.blit(background, (0, 0))

        # display title information and credits
        display_title_and_credits()

        for button in buttons:
            button.render()
            button.on_hover(mouse)

        pygame.display.flip()

    # done! time to quit
    pygame.quit()
def music_loop():
    """
    The music loop function loops through the music tracks in the tracks list.
    """
    global current_track
    pygame.mixer.music.load(tracks[current_track])
    pygame.mixer.music.set_volume(0.1)  # 0.1-1.0
    pygame.mixer.music.play()
    current_track = (current_track + 1) % len(tracks)


music_loop()
pygame.mixer.music.set_endevent(SONG_END)  # create event for song ending/looping

def display_title_and_credits():
    # Title text
    Text(
        "Checkers+",
        screen,
        (Width // 2, 22),
        FONT_64,
        WHITE,
    )

    # Under title text
    Text(
        "Checkers with a twist! For all ages and skill levels!",
        screen,
        (Width // 2, 55),
        FONT_32,
        WHITE,
    )
    # Credits text
    Text(
        "Developed by Wander Cerda-Torres, Barry Lin,",
        screen,
        (Width // 2, 650),
        FONT_24,
        WHITE,
    )
    Text(
        "Nathan McCourt, Jonathan Stanczak, and Geonhee Yu",
        screen,
        (Width // 2, 670),
        FONT_24,
        WHITE,
    )


second_menu_instance = SecondMenu(tracks)

def menu_buttons():
    """
    The menu buttons function creates the buttons on the main menu. It returns the button rectangles for each button so that they can be used in the main function.
    """
    # Start Game Button
    start_game_button = Button(
        "Start Game",
        screen,
        (Width // 2 - 150, Height // 3),
        (300, 50),
        GREY,
        START_GAME_ICON
    )
    # Settings Button
    setting_button = Button(
        "Settings",
        screen,
        (Width // 2 - 150, Height // 3 + BUTTON_HEIGHT + BUTTON_SPACING),
        (300, 50),
        GREY,
        SETTINGS_ICON
    )
    # Tutorial button
    tutorial_button = Button(
        "Tutorial",
        screen,
        (Width // 2 - 150, Height // 3 + 135),
        (300, 50),
        GREY,
        TUTORIAL_ICON
    )
    # Leaderboard button
    leaderboard_button = Button(
        "View Rankings",
        screen,
        (Width // 2 - 150, Height // 3 + 210),
        (300, 50),
        GREY,
        LEADERBOARD_ICON
    )
    # Customize Board button
    customize_board_button = Button(
        "Customize Board",
        screen,
        (Width // 2 - 150, Height // 3 + 285),
        (300, 50),
        GREY,
        BOARD_ICON
    )
    # Used to indicate if cursor is hovering over button. If so, button will be darker

    start_game_button.set_on_click_listener(second_menu_instance.start_game_menu)
    setting_button.set_on_click_listener(settings)
    tutorial_button.set_on_click_listener(tutorial)
    leaderboard_button.set_on_click_listener(show_leaderboard)
    customize_board_button.set_on_click_listener(board_customization)

    return start_game_button, setting_button, tutorial_button, leaderboard_button, customize_board_button


def tutorial():
    """
    The tutorial function displays the tutorial screen. It displays the tutorial text and image, and allows the user to exit the tutorial after clicking the exit button.
    The tutorial informs the user on how to use the application and what features are available to them.
    """

    # load image used in tutorial
    screen.fill(GREY)

    # First message
    Text(
        "Welcome to Checkers+!",
        screen,
        (Width // 2, 50),
        FONT_64,
        WHITE,
    )
    # Second message
    Text(
        "This tutorial should provide you with instructions on how to play and use Checkers+.",
        screen,
        (Width // 2, 105),
        FONT_32,
        WHITE,
    )

    tutorial_texts = [
        "There are many features accessible from the Checkers+ menu. You can start a player versus player game, a player",
        "versus computer game, and access features like the settings, leaderboard, board customization, and this tutorial!",
        "The settings will allow you to turn music on or off. You cannot change this once this game starts."
    ]
    tutorial_texts2 = [
        "The rankings will show how many points you have as a player, so make sure the name you enter is correct!",
        "To play Checkers+, standard checkers rules are applied...with a twist!",
        "You only have 5 seconds to make a move, so act fast! If you do not make a move within 5 seconds,",
        "you will lose your turn. Clicking on a piece will display available moves for that piece.",
        "Like standard checkers, once a piece reaches the opposing player's last row, that piece will become a king.",
        "This is indicated by a crown symbol that will display on the piece. Remember, you can move this piece backwards now!",
        "When the game starts, you will be asked to enter the names of the players (or player, if playing against the computer).",
        "Doing this will allow your name(s) and score(s) to be updated on your local leaderboard. 50 points for a win, and",
        "-50 points for a loss. However, your first loss of the day will not affect your score, so don't quit if you're off to a bad start!",
        "By now, you should have a basic understanding of what Checkers+ has to offer. Go give it a try!",
        "Note - Currently there is no button to exit a checkers game early. If you would like to quit,",
        "simply close the window by clicking the X in the top right corner. This should return you to the main menu."
    ]
    y = 145
    for line in tutorial_texts:
        t = Text(
            line,
            screen,
            (Width // 2, y),
            FONT_24,
            WHITE,
        )
        y = t.position[1] + t.line_height + 5

    # Create icon
    checkers_icon = Icon(
        screen,
        DEFAULT_ICON_SIZE,
        None,
        (Width // 2, (Height // 2) - 100),
        CHECKERS_ICON
    )
    checkers_icon.render_image_icon()

    y = 365

    for line in tutorial_texts2:
        t = Text(
            line,
            screen,
            (Width // 2, y),
            FONT_24,
            WHITE,
        )
        y = t.position[1] + t.line_height + 5

    # Exit button to return back to menu
    exit_tutorial_button = Button(
        "Exit Tutorial",
        screen,
        (Width // 2 - 150, Height - 50),
        (300, 50),
        DARK_GREY,
        None,
        FONT_32
    )

    pygame.display.flip()
    while True:
        mouse = pygame.mouse.get_pos()
        exit_tutorial_button.on_hover(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_tutorial_button.area.collidepoint(event.pos):  # if exit tutorial button is clicked
                    return
            elif event.type == SONG_END:
                music_loop()


def settings():
    """
    The settings function displays the settings screen. It displays the music button that allows the user to stop and play the music. It allows the user to exit
    the settings after clicking the exit button.
    """
    music_playing = True
    # Used for buttons w/ images
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    display_title_and_credits()

    # Music Button
    music_button = Button(
        "Music (On/Off)",
        screen,
        (Width // 2 - 150, Height // 3 + BUTTON_HEIGHT + BUTTON_SPACING + BUTTON_HEIGHT // 2),
        (300, 50),
        DARK_GREY,
        MUSIC_ICON,
        FONT_32
    )

    # Exit button to return back to menu
    exit_setting_button = Button(
        "Exit Settings",
        screen,
        (Width // 2 - 150, Height - 100),
        (300, 50),
        DARK_GREY,
        None,
        FONT_32
    )

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_setting_button.area.collidepoint(event.pos):  # if exit settings button is clicked
                    return  # exit settings and return to menu
                if music_button.area.collidepoint(event.pos):  # if music button is clicked
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()  # Stop the music
                        music_playing = False
                    else:
                        music_loop()  # Start the music from next song in tracklist
                        music_playing = True
            elif event.type is SONG_END and music_playing is True:
                music_loop()


def show_leaderboard():
    """
    The show leaderboard function displays the leaderboard screen. It displays the top ten players and their scores. It allows the user to exit the leaderboard after clicking the
    exit button.
    """
    screen.fill(GREY)
    # Leaderboard header
    Text(
        "Leaderboard",
        screen,
        (500, 40),
        FONT_32,
        WHITE
    )

    score_manager = ScoreManager("user_data/user_data.json")
    # Load scores from the JSON file
    score_manager.load_scores()

    # Sort players based on their scores in descending order
    sorted_players = sorted(score_manager.user_scores.items(), key=lambda x: x[1], reverse=True)

    # Extract the top ten players or all players if less than ten
    top_ten_players = sorted_players[:10]

    leaderboard_y = 80  # Adjust the vertical position as needed

    # Display the leaderboard in the new window
    for i, (username, score) in enumerate(top_ten_players):
        Text(
            f"{i + 1}. {username}: {score} points",
            screen,
            (500, leaderboard_y + i * 30),
            FONT_48,
            WHITE
        )

    pygame.display.flip()

    # Exit button to return back to menu
    exit_leaderboard_button = Button(
        "Return to Main Menu",
        screen,
        (Width // 2 - 150, Height - 50),
        (300, 50),
        DARK_GREY,
        None,
        FONT_32
    )

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_leaderboard_button.area.collidepoint(event.pos):  # if exit tutorial button is clicked
                    return  # exit tutorial and return to menu
            elif event.type == SONG_END:
                music_loop()


def board_customization():
    """
    The board customization function displays the board customization screen. It allows the user to change the GREY of the board to red, blue, yellow, or green. 
    It allows the user to exit the board customization after clicking the exit button.
    """
    # image of the background
    screen.fill(GREY)
    display_title_and_credits()
    # Exit button to return back to menu
    exit_leaderboard_button = Button(
        "Exit Board Customization",
        screen,
        (Width // 2 - 150, Height - 150),
        (300, 50),
        DARK_GREY,
        None,
        FONT_32
    )
    # Board GREY Text
    board_GREY_font = pygame.font.Font(None, 32)
    board_GREY_text = board_GREY_font.render("Board GREY", True, WHITE)
    text_rect = board_GREY_text.get_rect(center=(Width // 2 - 200, Height // 3 + 80))
    # Enlarge the box behind the text
    box_width = text_rect.width + 40  # Increase width
    box_height = text_rect.height + 20  # Increase height
    box_rect = pygame.Rect(text_rect.left - 20, text_rect.top - 10, box_width, box_height)
    # Draw the enlarged box behind the text
    pygame.draw.rect(screen, GREY, box_rect)
    screen.blit(board_GREY_text, text_rect)

    square_side = 50  # Size of the square
    red_square_rect = pygame.Rect(text_rect.right + 50, text_rect.centery - square_side // 2, square_side, square_side)
    pygame.draw.rect(screen, RED, red_square_rect)  # Red square
    blue_square_rect = pygame.Rect(red_square_rect.right + 20, red_square_rect.top, square_side, square_side)
    pygame.draw.rect(screen, BLUE, blue_square_rect)  # Blue square
    yellow_square_rect = pygame.Rect(blue_square_rect.right + 20, blue_square_rect.top, square_side, square_side)
    pygame.draw.rect(screen, YELLOW, yellow_square_rect)  # Yellow square
    green_square_rect = pygame.Rect(yellow_square_rect.right + 20, yellow_square_rect.top, square_side, square_side)
    pygame.draw.rect(screen, GREEN, green_square_rect)  # Green square

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_leaderboard_button.area.collidepoint(event.pos):  # if exit settings button is clicked
                    return
                if red_square_rect.collidepoint(event.pos):  # make board red
                    second_menu_instance.color = RED
                if blue_square_rect.collidepoint(event.pos):  # make board blue
                    second_menu_instance.color = BLUE
                if yellow_square_rect.collidepoint(event.pos):  # make board yellow
                    second_menu_instance.color = YELLOW
                if green_square_rect.collidepoint(event.pos):  # make board green
                    second_menu_instance.color = GREEN
            elif event.type == SONG_END:
                music_loop()


main()
