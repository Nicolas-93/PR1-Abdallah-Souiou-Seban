import fltk
from typing import List, Iterable, Optional, Sequence, Dict, Set
from dataclasses import dataclass

def encadre(liste_allumettes, selection, coup_possibles):
    encadrement = coup_possibles[selection]
    fltk.rectangle(liste_allumettes[-encadrement].x - 5, 240, liste_allumettes[-1].x + 10, 360)