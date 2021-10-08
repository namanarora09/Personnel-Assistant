import sys,os
import pygame
from pygame import *
from pathlib import *
from pygame.locals import *
from pygame import mixer_music

def musicplayer2():
    print("")
    pygame.init()
    pygame.mixer.init()

    lists_of_songs = os.listdir("D:/Songs")

    for song in lists_of_songs:
        if song.endswith(".mp3"):
            file_path = "D:/Songs"
            pygame.mixer.music.load(str(file_path))
            pygame.mixer.music.play()
            print("Playing::::: " + song)
            while pygame.mixer.music.get_busy() == True:
                continue

