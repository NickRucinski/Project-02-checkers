from ScoreManager import ScoreManager
from SecondMenu import SecondMenu
from constants import *
from Text import Text
from Button import Button
from Icon import Icon


class MainMenu:
    def __init__(self, screen, music_manager):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.music_manager = music_manager
        self.second_menu = SecondMenu(RED, screen, music_manager)

    def display_title_and_credits(self):
        # Title text
        Text(
            "Checkers+",
            self.screen,
            (self.width // 2, 22),
            FONT_64,
            WHITE,
        )

        # Under title text
        Text(
            "Checkers with a twist! For all ages and skill levels!",
            self.screen,
            (self.width // 2, 55),
            FONT_32,
            WHITE,
        )
        # Credits text
        Text(
            "Developed by Wander Cerda-Torres, Barry Lin,",
            self.screen,
            (self.width // 2, 650),
            FONT_24,
            WHITE,
        )
        Text(
            "Nathan McCourt, Jonathan Stanczak, and Geonhee Yu",
            self.screen,
            (self.width // 2, 670),
            FONT_24,
            WHITE,
        )

    def menu_buttons(self):
        """
        The menu buttons function creates the buttons on the main menu. It returns the button rectangles for each button so that they can be used in the main function.
        """
        # Start Game Button
        start_game_button = Button(
            "Start Game",
            self.screen,
            (self.width // 2 - 150, self.height // 3),
            (300, 50),
            GREY,
            START_GAME_ICON
        )
        # Settings Button
        setting_button = Button(
            "Settings",
            self.screen,
            (self.width // 2 - 150, self.height // 3 + BUTTON_HEIGHT + BUTTON_SPACING),
            (300, 50),
            GREY,
            SETTINGS_ICON
        )
        # Tutorial button
        tutorial_button = Button(
            "Tutorial",
            self.screen,
            (self.width // 2 - 150, self.height // 3 + 135),
            (300, 50),
            GREY,
            TUTORIAL_ICON
        )
        # Leaderboard button
        leaderboard_button = Button(
            "View Rankings",
            self.screen,
            (self.width // 2 - 150, self.height // 3 + 210),
            (300, 50),
            GREY,
            LEADERBOARD_ICON
        )
        # Customize Board button
        customize_board_button = Button(
            "Customize Board",
            self.screen,
            (self.width // 2 - 150, self.height // 3 + 285),
            (300, 50),
            GREY,
            BOARD_ICON
        )
        # Used to indicate if cursor is hovering over button. If so, button will be darker

        start_game_button.set_on_click_listener(self.second_menu.start_game_menu)
        setting_button.set_on_click_listener(self.settings)
        tutorial_button.set_on_click_listener(self.tutorial)
        leaderboard_button.set_on_click_listener(self.show_leaderboard)
        customize_board_button.set_on_click_listener(self.board_customization)

        return start_game_button, setting_button, tutorial_button, leaderboard_button, customize_board_button

    def tutorial(self):
        """
        The tutorial function displays the tutorial self.screen. It displays the tutorial text and image, and allows the user to exit the tutorial after clicking the exit button.
        The tutorial informs the user on how to use the application and what features are available to them.
        """

        # load image used in tutorial
        self.screen.fill(GREY)

        # First message
        Text(
            "Welcome to Checkers+!",
            self.screen,
            (self.width // 2, 50),
            FONT_64,
            WHITE,
        )
        # Second message
        Text(
            "This tutorial should provide you with instructions on how to play and use Checkers+.",
            self.screen,
            (self.width // 2, 105),
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
                self.screen,
                (self.width // 2, y),
                FONT_24,
                WHITE,
            )
            y = t.position[1] + t.line_height + 5

        # Create icon
        checkers_icon = Icon(
            self.screen,
            DEFAULT_ICON_SIZE,
            None,
            (self.width // 2, (self.height // 2) - 100),
            CHECKERS_ICON
        )
        checkers_icon.render_image_icon()

        y = 365

        for line in tutorial_texts2:
            t = Text(
                line,
                self.screen,
                (self.width // 2, y),
                FONT_24,
                WHITE,
            )
            y = t.position[1] + t.line_height + 5

        # Exit button to return back to menu
        exit_tutorial_button = Button(
            "Exit Tutorial",
            self.screen,
            (self.width // 2 - 150, self.height - 50),
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
                elif event.type == self.music_manager.SONG_END:
                    self.music_manager.music_loop()

    def settings(self):
        """
        The settings function displays the settings self.screen. It displays the music button that allows the user to stop and play the music. It allows the user to exit
        the settings after clicking the exit button.
        """
        music_playing = True
        # Used for buttons w/ images
        background = pygame.transform.scale(BACKGROUND_IMAGE, (self.screen.get_width(), self.screen.get_width()))
        self.screen.blit(background, (0, 0))
        self.display_title_and_credits()

        # Music Button
        music_button = Button(
            "Music (On/Off)",
            self.screen,
            (self.width // 2 - 150, self.height // 3 + BUTTON_HEIGHT + BUTTON_SPACING + BUTTON_HEIGHT // 2),
            (300, 50),
            DARK_GREY,
            MUSIC_ICON,
            FONT_32
        )

        # Exit button to return back to menu
        exit_setting_button = Button(
            "Exit Settings",
            self.screen,
            (self.width // 2 - 150, self.height - 100),
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
                            self.music_manager.music_loop()  # Start the music from next song in tracklist
                            music_playing = True
                elif event.type is self.music_manager.SONG_END and music_playing is True:
                    self.music_manager.music_loop()

    def show_leaderboard(self):
        """
        The show leaderboard function displays the leaderboard self.screen. It displays the top ten players and their scores. It allows the user to exit the leaderboard after clicking the
        exit button.
        """
        self.screen.fill(GREY)
        # Leaderboard header
        Text(
            "Leaderboard",
            self.screen,
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
                self.screen,
                (500, leaderboard_y + i * 30),
                FONT_48,
                WHITE
            )

        pygame.display.flip()

        # Exit button to return back to menu
        exit_leaderboard_button = Button(
            "Return to Main Menu",
            self.screen,
            (self.width // 2 - 150, self.height - 50),
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
                elif event.type == self.music_manager.SONG_END:
                    self.music_manager.music_loop()

    def board_customization(self):
        """
        The board customization function displays the board customization self.screen. It allows the user to change the GREY of the board to red, blue, yellow, or green. 
        It allows the user to exit the board customization after clicking the exit button.
        """
        # image of the background
        self.screen.fill(GREY)
        self.display_title_and_credits()
        # Exit button to return back to menu
        exit_leaderboard_button = Button(
            "Exit Board Customization",
            self.screen,
            (self.width // 2 - 150, self.height - 150),
            (300, 50),
            DARK_GREY,
            None,
            FONT_32
        )
        # Board GREY Text
        board_GREY_font = pygame.font.Font(None, 32)
        board_GREY_text = board_GREY_font.render("Board GREY", True, WHITE)
        text_rect = board_GREY_text.get_rect(center=(self.width // 2 - 200, self.height // 3 + 80))
        # Enlarge the box behind the text
        box_width = text_rect.width + 40  # Increase width
        box_height = text_rect.height + 20  # Increase height
        box_rect = pygame.Rect(text_rect.left - 20, text_rect.top - 10, box_width, box_height)
        # Draw the enlarged box behind the text
        pygame.draw.rect(self.screen, GREY, box_rect)
        self.screen.blit(board_GREY_text, text_rect)

        square_side = 50  # Size of the square
        red_square_rect = pygame.Rect(text_rect.right + 50, text_rect.centery - square_side // 2, square_side,
                                      square_side)
        pygame.draw.rect(self.screen, RED, red_square_rect)  # Red square
        blue_square_rect = pygame.Rect(red_square_rect.right + 20, red_square_rect.top, square_side, square_side)
        pygame.draw.rect(self.screen, BLUE, blue_square_rect)  # Blue square
        yellow_square_rect = pygame.Rect(blue_square_rect.right + 20, blue_square_rect.top, square_side, square_side)
        pygame.draw.rect(self.screen, YELLOW, yellow_square_rect)  # Yellow square
        green_square_rect = pygame.Rect(yellow_square_rect.right + 20, yellow_square_rect.top, square_side, square_side)
        pygame.draw.rect(self.screen, GREEN, green_square_rect)  # Green square

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
                        self.second_menu.color = RED
                    if blue_square_rect.collidepoint(event.pos):  # make board blue
                        self.second_menu.color = BLUE
                    if yellow_square_rect.collidepoint(event.pos):  # make board yellow
                        self.second_menu.color = YELLOW
                    if green_square_rect.collidepoint(event.pos):  # make board green
                        self.second_menu.color = GREEN
                elif event.type == self.music_manager.SONG_END:
                    self.music_manager.music_loop()
