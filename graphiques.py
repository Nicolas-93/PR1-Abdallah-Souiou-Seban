import fltk
from typing import List, Iterable, Optional, Dict, Set
from main import Allumette

def encadre(liste_allumettes: List[Allumette], selection: int, coup_possibles: List[int]):
    """
    Dessine un encadré autour des allumettes sélectionées
    """
    marge = 5
    longueur_allumette = liste_allumettes[-1].by - liste_allumettes[-1].ay
    encadrement = coup_possibles[selection]
    
    fltk.rectangle(
        liste_allumettes[-encadrement].ax - marge, liste_allumettes[-encadrement].ay - marge,
        liste_allumettes[-1].bx + marge, liste_allumettes[-1].ay + longueur_allumette + marge, couleur = "white"
    )

def beau_bouton(x, y, color, bucket, thickness, texte, size):
    marge = 10
    longueur, hauteur = fltk.taille_texte(texte, police='Helvetica', taille='24')
    fltk.rectangle(x - (longueur // 2) - marge, y - (hauteur//2) - marge, x + (longueur//2) + marge, y + (hauteur//2) + marge, couleur= color, remplissage= bucket , epaisseur= thickness, tag= '')
    fltk.texte(x, y, texte, couleur='black', ancrage='center', police='Helvetica', taille= size, tag='')