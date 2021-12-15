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

    fltk.rectangle(
        liste_allumettes[-encadrement].ax - marge, liste_allumettes[-encadrement].ay - marge,
        liste_allumettes[-1].bx + marge, liste_allumettes[-1].by + marge,
        couleur = "white"
    )


def beau_bouton(x, y, color, bucket, thickness, texte, size):
    marge = 10
    longueur, hauteur = fltk.taille_texte(texte, police='Helvetica', taille='24')

    longueur = longueur // 2 + marge
    hauteur = hauteur // 2 + marge

    fltk.rectangle(
        x - longueur, y - hauteur,
        x + longueur, y + hauteur,
        couleur= color, remplissage= bucket , epaisseur= thickness
    )
    fltk.texte(x, y, texte, couleur='black', ancrage='center', police='Helvetica', taille= size, tag='')

def dessin_allumette(Allumette: Allumette):
    """
    Dessine une allumette

    :param Allumette: Objet ``Allumette``
    """

    fltk.rectangle(
        Allumette.ax, Allumette.ay,
        Allumette.bx, Allumette.by,
        '#D4AF37', '#D4AF37'
    )
    fltk.cercle(
        Allumette.ax+(cfg.largeur_allumette/2), Allumette.ay,
        cfg.rayon_cercle_allumette,
        'red', 'red'
    )

def dessiner_allumettes(liste_allumettes: List[Allumette]):
    """
    Dessines les allumettes de la liste.

    :param liste_allumettes: Liste d'objets ``Allumette``
    """
    for allumette in liste_allumettes:
        dessin_allumette(allumette)