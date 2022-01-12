"""
PROJET 1, TP 11 GROUPE 4
Amal Abdallah, Nicolas Seban, Adam Souiou
"""

import fltk
from typing import List
from gameplay import Allumette
from PIL import Image
import gameplay
import cfg


def afficher_selection_allumettes(nb_a_selectionner: int,
                                  liste_allumettes: List[Allumette],
                                  rangee: int):
    """
    Met à jour la selection des allumettes
    """

    gameplay.reset_selection_rangee(liste_allumettes[rangee])
    if len(liste_allumettes[rangee]) > 0:
        for i in range(len(liste_allumettes[rangee])-1,
                       len(liste_allumettes[rangee])-nb_a_selectionner-1,
                       -1):
            liste_allumettes[rangee][i].selection = True


def dessiner_allumettes(liste_allumettes: List[Allumette],
                        image_allumette: Image,
                        image_allumette_brulee):
    """
    Dessines les allumettes de la liste.

    :param liste_allumettes: Liste d'objets ``Allumette``
    """

    for rangee in liste_allumettes:
        for allumette in rangee:
            image = (image_allumette_brulee
                     if allumette.selection else
                     image_allumette)
            fltk.afficher_image(
                allumette.ax,
                allumette.ay,
                image, ancrage='n'
            )


def calcul_taille_image(taille_image: tuple, taille_box: tuple, marge: float):
    """
    Calcule le coefficient d'agrandissement ou de réduction
    afin de préserver le ratio à appliquer à l'image,
    afin d'optimiser l'espace de la box.
    
    :param tuple taille_image: Tuple représentant la largeur et
    la hauteur de l'image
    :param tuple taille_box: Tuple représentant la largeur et
    la hauteur de la box qui contiendra l'image
    :param float marge: Marge à appliquer au minimum sur les bords
    
    """

    largeur_image, hauteur_image = taille_image
    marge /= 2
    largeur_box, hauteur_box = taille_box[0] - marge, taille_box[1] - marge

    return min(largeur_box/largeur_image, hauteur_box/hauteur_image)


def background(couleur: str) -> None:
    """
    Crée un arrière plan uni

    :param str couleur: Couleur du fond
    """

    fltk.rectangle(
        0, 0,
        cfg.largeur_fenetre, cfg.hauteur_fenetre,
        remplissage=couleur
    )

    return None
