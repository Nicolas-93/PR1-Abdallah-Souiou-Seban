import fltk
from typing import List, Iterable, Optional, Dict, Set
from dataclasses import dataclass
import cfg

@dataclass
class Allumette:
    ax: float
    ay: float
    bx: float
    by: float



def selectionCoups(selection, indice, coup_possibles):
    if (selection + indice) > (len(coup_possibles) - 1) or (selection + indice) < 0:
        return selection
    
    else:
        return (selection + indice)


def jouer_tour(selection, liste_allumettes, coup_possibles, boutons):
    choix = coup_possibles[selection]
    del liste_allumettes[-choix:]
    boutons[0].ay, boutons[0].by, boutons[1].ay, boutons[1].by = boutons[1].ay, boutons[1].by, boutons[0].ay, boutons[0].by


def selection_possible(liste_allumettes, selection, coups_possibles):
    """
    Détermine si la selection demandée est réalisable

    :param list liste_allumettes: Liste d'objets Allumettes
    """

    return coups_possibles[selection] < len(liste_allumettes)


def initialiser_allumettes() -> List[Allumette]:
    """
    Initialise une liste d'objets ``Allumette``, dont les coordonnées
    ont été adaptées à la taille de la fenêtre par leurs constantes globales
    """

    liste_allumettes = []
    marge = 10
    espacement = cfg.largeur_fenetre / cfg.nombre_allumettes - cfg.largeur_allumette

    x_max = cfg.nombre_allumettes * espacement - espacement/2
    centre = (cfg.largeur_fenetre - x_max)/2

    for i in range(0, cfg.nombre_allumettes):
        liste_allumettes.append(
            Allumette(
                ax = i * espacement + centre,
                ay = cfg.hauteur_fenetre/2 - cfg.hauteur_allumette/2,
                bx = i * espacement + centre + cfg.largeur_allumette,
                by = cfg.hauteur_fenetre/2 + cfg.hauteur_allumette/2
            )
        )
    
    return liste_allumettes


def gen_lst_coup_possibles(k: int) -> list:
    """
    Initialise une liste de valeurs allant de 1 à ``k`` inclu, afin
    de déterminer les coups/tirages possibles.

    :param k int: Nombre d'allumettes que pourra tirer un joueur (k > 0)
    :return set: liste de coups

    >>> gen_set_coup_possibles(8)
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> gen_set_coup_possibles(1)
    [1]
    """
    return [x for x in range(1, k+1)]


def coup_possible(liste_allumettes: List[Allumette], k_coups_possibles: list, misere=True) -> bool:
    """
    Retourne ``True`` si le prochain joueur pourra prélever une allumette.

    :param list liste_allumettes: liste d'objets allumettes
    :param dict k_coups_possibles: Dictionnaire contenant les

    >>> coup_possible([1, 1, 1, 1, 1], [1,2,3,4])
    True
    >>> coup_possible([0,0,0,0], [4])
    True
    >>> coup_possible([0,0,0,0], [5])
    False
    >>> coup_possible([], [1,2,3,4])
    False
    """

    for coup in k_coups_possibles:
        if coup <= len(liste_allumettes):
            return True
    return False


def message_interruption():
    """
    Message à l'intention de l'utilisateur qui utiliserait Ctrl+C...
    """
    print("\nVous devriez pouvoir fermer la fenêtre avec la croix",
          "théoriquement...",
          "\nMais merci d'y avoir pris plaisir!! A bientôt!!")
    # fltk.ferme_fenetre()
    exit(0)