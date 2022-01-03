import fltk
from typing import List
from gameplay import Allumette
import gameplay
import cfg


def afficher_selection_allumettes(nombre_allumettes_a_selectionner: int, liste_allumettes: List[Allumette], rangee: int):
    """
    
    """

    gameplay.reset_selection_rangee(liste_allumettes[rangee])
    if len(liste_allumettes[rangee]) > 0:
        for i in range(len(liste_allumettes[rangee])-1, len(liste_allumettes[rangee])-nombre_allumettes_a_selectionner-1, -1):
            liste_allumettes[rangee][i].selection = True

def dessiner_allumettes(liste_allumettes: List[Allumette], image_allumette, image_allumette_brulee):
    """
    Dessines les allumettes de la liste.

    :param liste_allumettes: Liste d'objets ``Allumette``
    """

    for rangee in liste_allumettes:
        for allumette in rangee:
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