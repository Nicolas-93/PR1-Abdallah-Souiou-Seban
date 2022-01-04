import fltk
from tkinter import *
from dataclasses import dataclass
from PIL import Image, ImageTk
import random
import cfg

@dataclass
class AluChute:
    ax: float
    ay: float
    Alu: object
    speed: float
    angle: int
    height: float

def initialisation(number):
    liste = []
    image1 = Image.open('allumette.png')
    image2 = Image.open('allumette-brûée.png')

    for i in range(number+1):
        j = random.randint(1,2)
        if j == 1:
            imagechute = image1
        else:
            imagechute = image2

        imagechute = resize(imagechute)

        liste.append(
            AluChute(
                ax = random.randint(0, 500),
                ay = random.randint(-100, 0),
                Alu = imagechute,
                speed = random.randint(2,20),
                angle = random.randint(0,35),
                height = imagechute.height
            )
        )
    liste = rotation(liste)
    return liste

def resize(image):
    (width, height) = (image.width // 10, image.height // 10)
    return image.resize((width, height))
    
def rotation(liste):
    for elem in liste:
        img = elem.Alu
        ang = elem.angle
        elem.Alu = img.rotate(ang * 10, expand = True)
        elem.height = img.height
        elem.Alu = ImageTk.PhotoImage(elem.Alu)
    return liste

def chute(elem):
    elem.ay += elem.speed
    elem.ay = elem.ay % (cfg.hauteur_fenetre + elem.height)

def dessiner(liste):
    for elem in liste:
        fltk.afficher_image(elem.ax, elem.ay, elem.Alu, ancrage='s')
        chute(elem)

