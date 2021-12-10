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
        liste_allumettes[-1].bx + marge, liste_allumettes[-1].ay + longueur_allumette + marge
    )

