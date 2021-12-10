import fltk
import graphiques
from typing import List, Iterable, Optional, Sequence, Dict, Set
from dataclasses import dataclass

@dataclass
class Allumette:
    x: float
    y: float

largeur_fenetre, hauteur_fenetre = 500, 500
nombre_allumettes = 21
largeur_allumette = 5
marge = 10
k = 5

# Choisir les objets (image)


def gen_set_coup_possibles(k: int) -> Set:
    """
    Initialise un ensemble de valeurs allant de 1 à ``k`` inclu, afin
    de déterminer les tirages possibles.

    :param k int: Nombre d'allumettes que pourra tirer un joueur (k > 0)
    :return set: Ensemble

    >>> gen_set_coup_possibles(8)
    {1, 2, 3, 4, 5, 6, 7, 8}
    >>> gen_set_coup_possibles(1)
    {1}
    """
    return {x for x in range(1, k+1)}



def coup_possible(liste_allumettes: List[Allumette], k_coups_possibles: Set) -> bool:
    """
    Retourne ``True`` si le prochain joueur pourra prélever une allumette.

    :param list liste_allumettes: liste d'objets allumettes
    :param dict k_coups_possibles: Dictionnaire contenant les

    >>> coup_possible([1, 1, 1, 1, 1], {1,2,3,4})
    True
    >>> coup_possible([0,0,0,0], {4})
    True
    >>> coup_possible([0,0,0,0], {5})
    False
    >>> coup_possible([], {1,2,3,4})
    False
    """

    for coup in k_coups_possibles:
        if coup <= len(liste_allumettes):
            return True
    return False

def initialiser_allumettes() -> List[Allumette]:
    """
    Initialise une liste d'objets ``Allumette``, dont les coordonnées
    ont été adaptées à la taille de la fenêtre par leurs constantes globales
    """
    
    liste_allumettes = []
    espacement = largeur_fenetre / nombre_allumettes - largeur_allumette
    # espacement += marge
    x_max = nombre_allumettes * espacement - espacement/2
    centre = (largeur_fenetre - x_max)/2
    for i in range(0, nombre_allumettes):
        liste_allumettes.append(
            Allumette(i * espacement + centre,
                      hauteur_fenetre/2
            )
        )
    
    return liste_allumettes

def dessin_allumette(Allumette: Allumette, coeff: float):

    fltk.rectangle((Allumette.x)*coeff, (Allumette.y)*coeff, (Allumette.x+largeur_allumette)*coeff, (Allumette.y+100)*coeff, '#D4AF37', '#D4AF37')
    fltk.cercle(Allumette.x+(largeur_allumette/2), Allumette.y, largeur_allumette, 'red', 'red')

def dessiner_allumettes(liste_allumettes: List[Allumette]):
    for allumette in liste_allumettes:
        dessin_allumette(allumette, 1)

if __name__ == "__main__":
    
    coup_possibles = gen_set_coup_possibles(k)
    liste_allumettes = initialiser_allumettes()


    fltk.cree_fenetre(largeur_fenetre, hauteur_fenetre)
    while True:
        try:
            fltk.efface_tout()
            # Gestion des événements
            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)
            if tev == 'Quitte':
                fltk.ferme_fenetre()
                exit()

            dessiner_allumettes(liste_allumettes)


            fltk.mise_a_jour()

        except KeyboardInterrupt:
            print("\nVous devriez pouvoir fermer la fenêtre avec la croix",
                  "théoriquement...",
                  "\nMais merci d'y avoir pris plaisir!! A bientôt!!")
            break

fltk.ferme_fenetre()
exit()
