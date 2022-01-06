import random
import os

try:
    import pygame
    pygame_available = True

except:
    pygame_available = False

def initialisation():
    global menu_bleep, menu_depart, bye_bye, change
    menu_bleep = pygame.mixer.Sound(os.path.join(os.path.curdir, 'sound/MenuBleep.wav'))
    menu_depart = pygame.mixer.Sound(os.path.join(os.path.curdir, 'sound/MenuAccept.wav'))
    change = pygame.mixer.Sound(os.path.join(os.path.curdir, 'sound/MenuWoosh.wav'))

def SoundAllu():
    if pygame_available:
        boopie = random.randint(0,5)
        boop = pygame.mixer.Sound(os.path.join(os.path.curdir, 'sound/DNATiny'+ str(boopie)+'.wav'))
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

def song(name):
    pygame.init()
    pygame.mixer.music.load(os.path.join(os.path.curdir, 'sound/song/' + name + '.mp3'))
    pygame.mixer.music.play(-1)
