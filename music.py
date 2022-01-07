import random
import os
import cfg

try:
    import pygame
    pygame_available = True
    sound = True

except:
    pygame_available = False
    sound = False
    cfg.son = False
    print("Installez pygame pour une meilleure expérience.")

def initialisation():
    if pygame_available:
        global menu_bleep, menu_depart, change
        menu_bleep = pygame.mixer.Sound(os.path.join('sound', 'MenuBleep.wav'))
        menu_depart = pygame.mixer.Sound(os.path.join('sound', 'MenuAccept.wav'))
        change = pygame.mixer.Sound(os.path.join('sound', 'MenuWoosh.wav'))

def SoundAllu():
    if pygame_available and sound:
        boopie = random.randint(0,5)
        boop = pygame.mixer.Sound(os.path.join('sound', f'DNATiny{boopie}.wav'))
        boop.play()

def BoutonAccept():
    if pygame_available and sound:
        menu_bleep.play()

def GameStart():
    if pygame_available and sound:
        menu_depart.play()

def MenuChange():
    if pygame_available and sound:
        change.play()

def toggle_sound():
    global sound
    if pygame_available:
        pygame.mixer.music.stop()
        sound = not sound
        if sound:
            pygame.mixer.music.load(os.path.join('sound', 'song', 'Neutral.mp3'))
            pygame.mixer.music.play(-1)


def song(name):
    if pygame_available and sound:
        pygame.init()
        pygame.mixer.music.load(os.path.join('sound', 'song', f'{name}.mp3'))
        pygame.mixer.music.play(-1)
