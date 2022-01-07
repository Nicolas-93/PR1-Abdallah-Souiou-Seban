"""
PROJET 1, TP 11 GROUPE 4
Amal Abdallah, Nicolas Seban, Adam Souiou
"""

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


def initialisation() -> None:
    """
    Initialise tous les effets sonores ainsi que leurs volumes.
    """
    if pygame_available:
        global menu_bleep, menu_depart, change
        menu_bleep = pygame.mixer.Sound(os.path.join('sound', 'MenuBleep.wav'))
        menu_depart = pygame.mixer.Sound(os.path.join('sound', 'MenuAccept.wav'))
        change = pygame.mixer.Sound(os.path.join('sound', 'MenuWoosh.wav'))
        pygame.mixer.Sound.set_volume(menu_bleep, 0.5)
        pygame.mixer.Sound.set_volume(menu_depart, 0.4)
        pygame.mixer.Sound.set_volume(change, 0.5)


def SoundAllu() -> None:
    """
    Fais un bruitage sonore aléatoire.
    """
    if pygame_available and sound:
        boopie = random.randint(0,5)
        boop = pygame.mixer.Sound(os.path.join('sound', f'DNATiny{boopie}.wav'))
        pygame.mixer.Sound.set_volume(boop, 0.8)
        boop.play()


def BoutonAccept() -> None:
    """
    Joue un son spécifique si pygame est disponible et si le son est activé.
    """
    global menu_bleep
    if pygame_available and sound:
        menu_bleep.play()


def GameStart() -> None:
    """
    Joue un son spécifique si pygame est disponible et si le son est activé.
    """
    global menu_depart
    if pygame_available and sound:
        menu_depart.play()


def MenuChange() -> None:
    """
    Joue un son spécifique si pygame est disponible et si le son est activé.
    """
    global change
    if pygame_available and sound:
        change.play()


def toggle_sound() -> None:
    """
    Désactive la musique et les sons ou les réactive en changeant l'état de "sound"
    """
    global sound
    if pygame_available:
        pygame.mixer.music.stop()
        sound = not sound
        if sound:
            pygame.mixer.music.load(os.path.join('sound', 'song', 'Neutral.mp3'))
            pygame.mixer.music.play(-1)


def song(name: str) -> None:
    """
    Prends en entrée le nom du fichier mp3 pour le jouer.

    :param str: nom du fichier à jouer.
    """
    if pygame_available and sound:
        pygame.init()
        pygame.mixer.music.load(os.path.join('sound', 'song', f'{name}.mp3'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
