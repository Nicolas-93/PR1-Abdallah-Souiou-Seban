import fltk
from typing import List, Iterable, Optional, Dict, Set

def selectionCoups(selection, indice, coup_possibles):
    if (selection + indice) > (len(coup_possibles) - 1) or (selection + indice) < 0:
        return selection
    
    else:
        return (selection + indice)

def jouer_tour(selection, liste_allumettes, coup_possibles):
    choix = coup_possibles[selection]
    del liste_allumettes[-choix:]