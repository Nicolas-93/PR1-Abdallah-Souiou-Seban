import fltk
import graphiques
import gameplay
from typing import List, Iterable, Optional, Dict, Set
from dataclasses import dataclass

@dataclass
class Allumette:
    ax: float
    ay: float
    bx: float
    by: float


largeur_fenetre, hauteur_fenetre = 500, 500
nombre_allumettes = 15
largeur_allumette, hauteur_allumette = 5, 100
rayon_cercle_allumette = largeur_allumette*0.65
marge = 10
k = 5
selection = 0
joueur = 1


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


def coup_possible(liste_allumettes: List[Allumette], k_coups_possibles: list) -> bool:
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


def initialiser_allumettes() -> List[Allumette]:
    """
    Initialise une liste d'objets ``Allumette``, dont les coordonnées
    ont été adaptées à la taille de la fenêtre par leurs constantes globales
    """

    liste_allumettes = []
    marge = 10
    espacement = largeur_fenetre / nombre_allumettes - largeur_allumette

    x_max = nombre_allumettes * espacement - espacement/2
    centre = (largeur_fenetre - x_max)/2

    for i in range(0, nombre_allumettes):
        liste_allumettes.append(
            Allumette(
                ax = i * espacement + centre,
                ay = hauteur_fenetre/2,
                bx = 0,
                by = 0
            )
        )
        liste_allumettes[-1].bx = liste_allumettes[-1].ax + largeur_allumette
        liste_allumettes[-1].by = liste_allumettes[-1].ay + hauteur_allumette

    return liste_allumettes


def dessin_allumette(Allumette: Allumette, coeff: float):
    """
    Dessine une allumette

    :param Allumette: Objet ``Allumette``
    :param coeff: *Under Construction...*
    """

    fltk.rectangle(
        Allumette.ax, Allumette.ay,
        Allumette.bx, Allumette.by,
        '#D4AF37', '#D4AF37'
    )
    fltk.cercle(
        Allumette.ax+(largeur_allumette/2), Allumette.ay,
        rayon_cercle_allumette,
        'red', 'red'
    )


def dessiner_allumettes(liste_allumettes: List[Allumette]):
    """
    Dessines les allumettes de la liste.

    :param liste_allumettes: Liste d'objets ``Allumette``
    """
    for allumette in liste_allumettes:
        dessin_allumette(allumette, 1)

def fin():
    print(f"Lol ta perdu, Joueur {joueur} (t'-'t) ")
    exit(0)

if __name__ == "__main__":

    # coup_possibles = gen_set_coup_possibles(k)
    coup_possibles = [1,2,4,5]
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

            elif tev == "ClicGauche":
                if fltk.ordonnee_souris() >= 250 and fltk.ordonnee_souris() <= 350:
                    selection = gameplay.selectionCoups(selection, 1, coup_possibles)


                if 100 <= fltk.ordonnee_souris() <= 200 and 100 <= fltk.abscisse_souris() <= 400:
                    gameplay.jouer_tour(selection, liste_allumettes, coup_possibles)
                    joueur = 2 - (joueur - 1)
                    selection = 0


            elif tev == "ClicDroit":
                if fltk.ordonnee_souris() >= 250 and fltk.ordonnee_souris() <= 350:
                    selection = gameplay.selectionCoups(selection, -1, coup_possibles)
            fltk.rectangle(0,0,500,500, remplissage = "#3f3e47")


            if 132 <= fltk.ordonnee_souris() <= 167 and 172 <= fltk.abscisse_souris() <= 327:
                graphiques.beau_bouton(250,150, "black", "#898496" , 1, "Fin de tour", 30)

            else:
                graphiques.beau_bouton(250,150, "black", "#dbdbdb" , 1, "Fin de tour", 30)

            dessiner_allumettes(liste_allumettes)

            if not coup_possible(liste_allumettes, coup_possibles):
                joueur = 2 - (joueur - 1)
                fin()
            graphiques.encadre(liste_allumettes, selection, coup_possibles)

            fltk.texte(250, 100, f'Joueur {joueur}', couleur='white', ancrage='center', police='Helvetica', taille= 24)

            fltk.mise_a_jour()

        except KeyboardInterrupt:
            print("\nVous devriez pouvoir fermer la fenêtre avec la croix",
                  "théoriquement...",
                  "\nMais merci d'y avoir pris plaisir!! A bientôt!!")
            break

    #fltk.ferme_fenetre()
    #exit()
