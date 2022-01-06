import random
import os

# try:
#     import pygame
#     pygame_available = True
#
# except:
pygame_available = False

def initialisation():
    if pygame_available:
        global menu_bleep, menu_depart, bye_bye, change
        menu_bleep = pygame.mixer.Sound(os.path.join('sound', 'MenuBleep.wav'))
        menu_depart = pygame.mixer.Sound(os.path.join('sound', 'MenuAccept.wav'))
        change = pygame.mixer.Sound(os.path.join('sound', 'MenuWoosh.wav'))

def SoundAllu():
    if pygame_available:
        boopie = random.randint(0,5)
        boop = pygame.mixer.Sound(os.path.join('sound', f'DNATiny{boopie}.wav'))
        boop.play()

def BoutonAccept():
    global menu_bleep
    if pygame_available:
        menu_bleep.play()

def GameStart():
    global menu_depart
    if pygame_available:
        menu_depart.play()

def MenuChange():
    global change
    if pygame_available:
        change.play()

"""def toggle_sound():
    print(cfg.son)
    if cfg.son:
        pygame.mixer.pause()
    else:
        pygame.mixer.unpause()"""


def song(name):
    if pygame_available:
        pygame.init()
        pygame.mixer.music.load(os.path.join('sound', 'song', f'{name}.mp3'))
        pygame.mixer.music.play(-1)
