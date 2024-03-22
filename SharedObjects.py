"""
SharedObjects.py
The SharedObjects file is used to create a shared instance of the BackgroundMusic class.
"""

from MusicClass import BackgroundMusic
import pygame

# Initialize Pygame
pygame.init()

# Initialize the mixer
pygame.mixer.init()

# Initial tracks
initial_tracks = ["music/Track1.mp3", "music/Track2.mp3", "music/Track3.mp3", "music/Track4.mp3", "music/Track5.mp3", "music/Track6.mp3", "music/Track7.mp3", "music/Track8.mp3"]

# Create a shared instance of BackgroundMusic with the initial tracks
background_music = BackgroundMusic()
background_music.start_music_loop()
