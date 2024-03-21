"""
MusicClass.py
The MusicClass file is used to create a BackgroundMusic class that can be used to play background music.
"""


import pygame
import pygame.mixer

pygame.mixer.init()
class BackgroundMusic:
    """
        The BackgroundMusic class is used to play background music, and consists of the functions play music, start music loop, and handle event.
    """
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

    def __init__(self):
        """
        The init function is used to initialize the BackgroundMusic class, and consists of the variables tracks, current_track, and SONG_END.
        """
        self.current_track = 0
        self.SONG_END = pygame.USEREVENT + 1

        pygame.mixer.music.set_endevent(self.SONG_END)

    def play_music(self):
        """
        The play music function is used to play music, and consists of the functions load, set volume, play, and current track.
        """
        pygame.mixer.music.load(self.tracks[self.current_track])
        pygame.mixer.music.set_volume(0.1)  # Adjust volume between 0.1 and 1.0
        pygame.mixer.music.play()
        self.current_track = (self.current_track + 1) % len(self.tracks)

    def start_music_loop(self):
        """
        The start music loop function is used to start the music loop, and consists of the function play music.
        """
        self.play_music()

    def handle_event(self, event):
        """
        The handle event function is used to handle events, and consists of the function play music.
        """
        if event.type == self.SONG_END:
            self.play_music()

    def music_loop(self):
        """
        The music loop function loops through the music tracks in the tracks list.
        """
        pygame.mixer.music.load(self.tracks[self.current_track])
        pygame.mixer.music.set_volume(0.1)  # 0.1-1.0
        pygame.mixer.music.play()
        self.current_track = (self.current_track + 1) % len(self.tracks)

