import fltk
from dataclasses import dataclass
from PIL import Image
import random
import cfg

@dataclass
class Image:
    ax: float
    ay: float
    Image: str
    speed: float

def initialisation(number, image, image2):
    liste = []
    for i in range(number+1):
        j = random.randint(1,2)
        if j == 1:
            imagechute = image
        else:
            imagechute = image2
        liste.append(
            Image(
                ax = random.randint(0, 500),
                ay = random.randint(-50, 0),
                Image = imagechute,
                speed = random.randint(4,15)
            )
        )
    return liste

def chute(liste):
    for i in liste:
        i.ay += i.speed
        i.ay = i.ay % 600

def dessiner(liste):
    for i in liste:
        fltk.afficher_image(i.ax, i.ay, i.Image, ancrage='s')
    chute(liste)

