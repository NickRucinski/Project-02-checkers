"""
SecondMenu.py
The SecondMenu file and class powers the second menu of the game, which allows the user to choose between playing against another player or against the computer.
The class also creates an object of the game class to create the game the users plays.
"""
from Button import Button
from Player import Player
from Text import Text
from ScoreManager import ScoreManager
from game import Game
from computer import minimax
from MusicClass import BackgroundMusic
from SharedObjects import background_music
from constants import *


player1 = Player("Player 1", 0, RED)
player2 = Player("Player 2", 0, BLACK)
score_manager = ScoreManager("user_data/user_data.json")


def get_row_col_from_mouse(pos):
    """
    This function gets the row and column of the mouse position. This is necessary for selecting pieces in the class.
    """
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


class SecondMenu:
    """
    The SecondMenu class consists of a String color, which represents the color of the board chosen by the user.
    The class also has three functions, start_game_menu, start_game_vs_player, and start_game_vs_computer.
    """

    def __init__(self, color, screen, music_manager: BackgroundMusic):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.selected_music_track = music_manager.current_track
        self.background_music = music_manager
        self.board_color = color

    def start_game_menu(self):
        """
        The start game menu function displays the second menu of the game, which allows the user to choose between playing against another player or against the computer.
        """

        global player1, player2
        # image of the background
        background_image = pygame.transform.scale(BACKGROUND_IMAGE, (self.width, self.height))
        self.screen.blit(background_image, (0, 0))

        # Title
        Text(
            "Select Game Mode",
            self.screen,
            (self.width // 2, 38),
            FONT_64,
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

        # PvP Button
        start_pvp_button = Button(
            "Start Game VS Player",
            self.screen,
            (self.width // 2 - 150, self.height // 3 - 25),
            (300, 50),
            GREY
        )
        start_pvp_button.set_on_click_listener(lambda: (
            player1.get_player_name(),
            score_manager.add_user(player1.username),
            player2.get_player_name(),
            score_manager.add_user(player2.username),
            self.start_game_vs_player(),
            score_manager.save_scores()
        ))

        # PvC Button
        start_pvc_button = Button(
            "Start Game VS Computer",
            self.screen,
            (self.width // 2 - 150, self.height // 3 + BUTTON_HEIGHT + BUTTON_SPACING),
            (300, 50),
            GREY,
        )

        # Exit Second Menu Button
        exit_button = Button(
            "Back to Main Menu",
            self.screen,
            (self.width // 2 - 150, self.height // 3 + 135),
            (300, 50),
            GREY
        )

        pygame.display.flip()

        while True:
            mouse = pygame.mouse.get_pos()
            start_pvp_button.on_hover(mouse)
            start_pvc_button.on_hover(mouse)
            exit_button.on_hover(mouse)

            for event in pygame.event.get():
                score_manager.load_scores()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button.area.collidepoint(event.pos):  # if exit button is clicked
                        return  # exit start game menu and return to menu
                    elif start_pvp_button.area.collidepoint(event.pos):  # Start Game VS Player button clicked
                        start_pvp_button.onclick_function()
                        return
                    elif start_pvc_button.area.collidepoint(event.pos):  # Start Game VS Computer button clicked
                        player1.get_player_name()
                        score_manager.add_user(player1)
                        self.start_game_vs_computer()
                        score_manager.save_scores()
                        return
                    # score_manager.save_scores() # now inside elif so scores are updated before returning to main
                    elif event.type == self.background_music.SONG_END:
                        self.background_music.handle_event(event)

    def start_game_vs_player(self):
        """
        The start game vs player function starts the game against another player by creating an object of the game class and passing the self.screen, color, and player names.
        """
        run = True
        clock = pygame.time.Clock()
        game = Game(self.screen, self.board_color, player1.username, player2.username)
        global score_manager, user_scores

        # Exit Button
        game_exit_button = Button(
            "Exit Game",
            self.screen,
            (self.width // 2 - 150, self.height // 3 + 135),
            (300, 50),
            GREY
        )
        game_exit_button.set_on_click_listener(lambda: ())

        pygame.display.flip()

        while run:
            clock.tick(60)
            if game.winner() is not None:
                print(game.winner())
                run = False
                if game.winner() == RED:
                    player1.update_win()
                    score_manager.update_scores(player1)
                    player2.update_loss()
                    score_manager.update_scores(player2)
                elif game.winner() == WHITE:
                    player2.update_win()
                    score_manager.update_scores(player2)
                    player1.update_loss()
                    score_manager.update_scores(player1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)
                    # Check for background music event
                if event.type == background_music.SONG_END:
                    background_music.handle_event(event)

            game.update()

    def start_game_vs_computer(self):
        """
        The start game vs computer function starts the game against the computer by creating an object of the game class and passing the self.screen, color, and player name.
        """
        run = True
        clock = pygame.time.Clock()
        game = Game(self.screen, self.board_color, player1.username, "Computer")
        global score_manager, user_scores

        # Exit Button
        game_exit_button = Button(
            "Exit Game",
            self.screen,
            (self.width // 2 - 150, self.height // 3 + 135),
            (300, 50),
            GREY
        )
        game_exit_button.set_on_click_listener(lambda: ())

        pygame.display.flip()

        while run:
            clock.tick(60)
            if game.turn == player2.color:
                value, new_board = minimax(game.get_board(), 4, WHITE, game)
                game.ai_move(new_board)

            if game.winner() != None:
                print(game.winner())
                run = False
                if game.winner() == player1.color:
                    player1.update_win()
                    score_manager.update_scores(player1)
                else:
                    player1.update_loss()
                    score_manager.update_scores(player1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

                if event.type == background_music.SONG_END:
                    background_music.handle_event(event)

            game.update()
