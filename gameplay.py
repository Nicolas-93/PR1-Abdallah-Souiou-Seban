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
    selection = False


def selectionCoups(selection, indice, coup_possibles):
    if (selection + indice) > (len(coup_possibles) - 1) or (selection + indice) < 0:
        return selection

    else:
        return (selection + indice)


def jouer_tour(selection, liste_allumettes, coup_possibles):
    choix = coup_possibles[selection]
    del liste_allumettes[-choix:]


def selection_possible(liste_allumettes, selection, coups_possibles):
    """
    Détermine si la selection demandée est réalisable

    :param list liste_allumettes: Liste d'objets Allumettes
    """

    return coups_possibles[selection] < len(liste_allumettes)


def initialiser_allumettes(liste_marienbad=[cfg.nombre_allumettes]) -> List[Allumette]: # Avec support du jeu de marienbad
    """
    Initialise une liste d'objets ``Allumette``, dont les coordonnées
    ont été adaptées à la taille de la fenêtre par leurs constantes globales
    """

    liste_allumettes = []
    nb_rangees = len(liste_marienbad)
    nombre_allumettes_max = max(liste_marienbad)
    marge = 0

    espacement_x = cfg.largeur_fenetre / (nombre_allumettes_max+1) - marge
    x_max = (nombre_allumettes_max-1) * espacement_x + cfg.largeur_allumette
    x_centre = (cfg.largeur_fenetre - x_max)/2

    espacement_y = cfg.hauteur_fenetre / (nb_rangees) - marge
    y_max = (nb_rangees-1) * espacement_y + cfg.hauteur_fenetre
    y_centre = (cfg.hauteur_fenetre - y_max)/2 + (cfg.hauteur_fenetre - cfg.hauteur_allumette)/2

    for j in range(0, nb_rangees):
        ligne_allumettes = []
        for i in range(0, liste_marienbad[j]):
            ligne_allumettes.append(
                Allumette(
                    ax = i * espacement_x + x_centre,
                    ay = j * espacement_y + y_centre,
                    bx = i * espacement_x + x_centre + cfg.largeur_allumette,
                    by = j * espacement_y + y_centre + cfg.hauteur_allumette
                )
            )
        liste_allumettes.append(ligne_allumettes)

    return liste_allumettes[0] # Pour libérer la puissance de cette ligne, rendez le jeu compatible Marienbad!


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
