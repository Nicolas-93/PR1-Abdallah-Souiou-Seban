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
        imagechute = image if bool(random.getrandbits(1)) else image2
        liste.append(
            Image(
                ax = random.randint(0, cfg.largeur_fenetre),
                ay = random.randint(int(-cfg.hauteur_fenetre*cfg.hauteur_allumette), 0),
                Image = imagechute,
                speed = random.randint(4,15)
            )
        )
    return liste

def chute(liste):
    for img in liste:
        img.ay += img.speed
        img.ay = img.ay % 600

def dessiner(liste):
    for img in liste:
        fltk.afficher_image(img.ax, img.ay, img.Image, ancrage='s')
    chute(liste)

