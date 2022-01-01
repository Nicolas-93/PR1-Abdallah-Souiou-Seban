from typing import List, Union
from dataclasses import dataclass
import bouton
import cfg
import graphiques

@dataclass
class Allumette:
    ax: float
    ay: float
    bx: float
    by: float
    selection = False


def appliquer_selection_allumettes(
    indice_coups_possibles: int, increment_clic: int, coups_possibles: list,
    liste_allumettes: List[List[Allumette]], rangee: Union[int, str]):

    """
    Sélectionne les allumettes en fonction de la valeur de ``indice_coups_possibles`` qui représente
    le curseur de la liste des coups possibles ``coups_possibles``. Ce curseur est dé/incrémenté dans les
    limites de la liste ``coups_possibles`` mais aussi dans la limite des allumettes restantes
    dans la rangée ``rangee`` demandée.
    ~~Permet la déselection des allumettes~~ 

    :param int indice_coups_possibles: Curseur/indice par rapport à la liste ``coups_possibles``
    :param int increment_clic: Incrémentation +/- 1
    :param list coups_possibles: Liste représentant les coups possibles
    :param list liste_allumettes: Liste de rangées d'objets ``Allumette``s
    :param Union[int, str] rangee: Numéro de la rangée où la sélection sera réalisée

    Supprimer les rangées vides de la liste_allumettes!!!!!
    """

    if (rangee != None and rangee.isnumeric()) or type(rangee) == int:
        rangee = int(rangee)

        # Déterminer si l'indice de la selection demandé peut devenir valable avec l'increment du clic (+-1)
        if ((0 <= indice_coups_possibles + increment_clic <= len(coups_possibles)-1) 
        and coups_possibles[indice_coups_possibles + increment_clic] <= len(liste_allumettes[rangee])):
            
            indice_coups_possibles += increment_clic
            nombre_allumettes_a_selectionner = coups_possibles[indice_coups_possibles]

        elif increment_clic == -1 and indice_coups_possibles == -1: # ~~in {0,-1}~~
            nombre_allumettes_a_selectionner = 0
        
        else:

            nombre_allumettes_a_selectionner = coups_possibles[indice_coups_possibles]
        
        graphiques.afficher_selection_allumettes(nombre_allumettes_a_selectionner, liste_allumettes, rangee)

    return indice_coups_possibles
    

def reset_selection_rangee(liste_rangee: list) -> None:
    """
    Déselectionne toutes les objets ``Allumettes`` de la rangée d'objets
    ``liste_rangee``s
    """
    for i in range(len(liste_rangee)-1, -1, -1):
        if liste_rangee[i].selection:
            liste_rangee[i].selection = False
        else:
            break

    return None


def jouer_tour(liste_allumettes, liste_boutons_jeu):

    bouton.intervertir_pos_boutons(liste_boutons_jeu[0], liste_boutons_jeu[1])

    for rangee in range(len(liste_allumettes)-1, -1, -1):
        for allumette in range(len(liste_allumettes[rangee])-1, -1, -1):

            if liste_allumettes[rangee][allumette].selection:
                del liste_allumettes[rangee][allumette]


def hitbox_marienbad(liste_allumettes: List[List[Allumette]]):
    """
    Crée un bouton pour chaque rangée de la ``liste_allumettes``, le texte de chaque bouton
    est le numéro de la rangée (Débute à 0).

    :param List[List[Allumette]] liste_allumettes: Liste d'objets ``Bouton``s
    :return list: Liste d'objets ``Bouton``s
    """
    hitbox_allumettes = []
    for i, rangee in enumerate(liste_allumettes):
        hitbox_allumettes.append(
            bouton.cree_bouton_invisible(
                rangee[0].ax/cfg.largeur_fenetre,
                rangee[0].ay/cfg.hauteur_fenetre,
                rangee[-1].bx/cfg.largeur_fenetre,
                rangee[-1].by/cfg.hauteur_fenetre,
                identificateur = str(i),
                )
        )
    
    return hitbox_allumettes


def initialiser_allumettes(liste_marienbad=[cfg.nombre_allumettes]) -> List[Allumette]: # Avec support du jeu de marienbad
    """
    Initialise une liste d'objets ``Allumette``, dont les coordonnées
    ont été adaptées à la taille de la fenêtre par leurs constantes globales
    """

    liste_allumettes = []
    nb_rangees = len(liste_marienbad)
    nombre_allumettes_max = max(liste_marienbad)
    marge = 40

    espacement_x = cfg.largeur_fenetre / (nombre_allumettes_max+1)
    x_max = (nombre_allumettes_max-1) * espacement_x + cfg.largeur_allumette
    x_centre = (cfg.largeur_fenetre - x_max)/2

    espacement_y = cfg.hauteur_fenetre / (nb_rangees) - marge
    y_max = (nb_rangees-1) * espacement_y + cfg.hauteur_fenetre
    y_centre = (cfg.hauteur_fenetre - y_max)/2 + (cfg.hauteur_fenetre - cfg.hauteur_allumette)/2

    for j in range(nb_rangees):
        ligne_allumettes = []
        for i in range(liste_marienbad[j]):
            ligne_allumettes.append(
                Allumette(
                    ax = i * espacement_x + x_centre,
                    ay = j * espacement_y + y_centre,
                    bx = i * espacement_x + x_centre + cfg.largeur_allumette,
                    by = j * espacement_y + y_centre + cfg.hauteur_allumette
                )
            )
        liste_allumettes.append(ligne_allumettes)

    return liste_allumettes


def gen_lst_coup_possibles(k: int) -> list:
    """
    Initialise une liste de valeurs allant de 1 à ``k`` inclu, afin
    de déterminer les coups/tirages possibles.

    :param int k: Nombre d'allumettes que pourra tirer un joueur (k > 0)
    :return set: liste de coups

    >>> gen_set_coup_possibles(8)
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> gen_set_coup_possibles(1)
    [1]
    """
    return [x for x in range(1, k+1)]


def coup_possible(liste_allumettes: List[Allumette], coups_possibles: list) -> bool:
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

    for coup in coups_possibles:
        for rangee in liste_allumettes:
            if coup <= len(rangee):
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