import fltk
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
    with Image.open('allumette.png') as img1,\
         Image.open('allumette-brûée.png') as img2:
        imagechute1 = resize(img1)
        imagechute2 = resize(img2)

    for i in range(number+1):
        imagechute = (imagechute1
                      if bool(random.getrandbits(1)) else
                      imagechute2)

        liste.append(
            AluChute(
                ax=random.randint(0, cfg.largeur_fenetre),
                ay=random.randint(int(-cfg.hauteur_fenetre*2), 0),
                Alu=imagechute,
                speed=random.randint(2, 7),
                angle=random.randint(-160, 160),
                height=imagechute.height
            )
        )
        imagechute = imagechute.rotate(
            liste[-1].angle, expand=True, resample=Image.BICUBIC
        )
        liste[-1].height = imagechute.height
        liste[-1].Alu = ImageTk.PhotoImage(imagechute)

    return liste


def resize(image):
    (width, height) = (image.width // 10, image.height // 10)
    return image.resize((width, height), resample=Image.BICUBIC)


def chute(elem):
    elem.ay += elem.speed
    elem.ay = elem.ay % (cfg.hauteur_fenetre + elem.height)


def dessiner(liste):
    for elem in liste:
        fltk.afficher_image(elem.ax, elem.ay, elem.Alu, ancrage='s')
        chute(elem)
