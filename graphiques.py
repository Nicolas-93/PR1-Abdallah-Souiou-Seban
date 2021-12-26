import fltk
from typing import List, Iterable, Optional
from gameplay import Allumette
import gameplay
import cfg


def encadre(liste_allumettes: List[Allumette], selection: int, coup_possibles: List[int]):
    """
    Dessine un encadré autour des allumettes sélectionées
    """
    
    marge = 5

    if gameplay.selection_possible(liste_allumettes, selection, coup_possibles):
        encadrement = coup_possibles[selection]
    else:
        encadrement = 0

    '''fltk.rectangle(
        liste_allumettes[-encadrement].ax - marge, liste_allumettes[-encadrement].ay - marge,
        liste_allumettes[-1].bx + marge, liste_allumettes[-1].by + marge,
        couleur = "white"
    )'''

    for i in range(len(liste_allumettes)):
        if i <= encadrement:
            liste_allumettes[-i].selection = True
        else:
            liste_allumettes[-i].selection = False

        if encadrement:
            liste_allumettes[0].selection = False
        else:
            liste_allumettes[-i].selection = True


def dessiner_allumettes(liste_allumettes: List[Allumette], image_allumette, image_allumette_brulee):
    """
    Dessines les allumettes de la liste.

    :param liste_allumettes: Liste d'objets ``Allumette``
    """

    for allumette in liste_allumettes:
        image = image_allumette_brulee if allumette.selection else image_allumette
        fltk.afficher_image(
            allumette.ax,
            allumette.ay,
            image, ancrage='nw'
        )


def calcul_taille_image(taille_image: tuple, taille_box: tuple):
    """
    Calcule le coefficient d'agrandissement ou de réduction (afin de préserver le ratio)
    à appliquer à l'image, afin d'optimiser l'espace de la box.
    """

    largeur_image, hauteur_image = taille_image
    largeur_box, hauteur_box = taille_box

    return min(largeur_box/largeur_image, hauteur_box/hauteur_image)


def background(couleur: str) -> None:
    
    fltk.rectangle(
        0, 0,
        cfg.largeur_fenetre, cfg.hauteur_fenetre,
        remplissage=couleur
    )

    return None