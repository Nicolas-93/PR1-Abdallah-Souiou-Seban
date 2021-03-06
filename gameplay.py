"""
PROJET 1, TP 11 GROUPE 4
Amal Abdallah, Nicolas Seban, Adam Souiou
"""

from typing import List, Tuple
from dataclasses import dataclass
import bouton
from bouton import Bouton
import cfg
import graphiques
import music
import solo


@dataclass
class Allumette:
    ax: float
    ay: float
    bx: float
    by: float
    selection = False


def appliquer_selection_allumettes(indice_coups_possibles: int,
                                   increment_clic: int,
                                   coups_possibles: list,
                                   liste_allumettes: List[List[Allumette]],
                                   rangee: str) -> int:
    """
    Sélectionne les allumettes en fonction de la valeur
    de ``indice_coups_possibles`` qui représente le curseur de
    la liste des coups possibles ``coups_possibles``.
    Ce curseur est dé/incrémenté dans les limites de
    la liste ``coups_possibles`` mais aussi dans la limite
    des allumettes restantes dans la rangée ``rangee`` demandée.

    :param int indice_coups_possibles: Curseur/indice par rapport
    à la liste ``coups_possibles``
    :param int increment_clic: Incrémentation +/- 1 du clic
    :param list coups_possibles: Liste représentant les coups possibles
    :param list liste_allumettes: Liste de rangées d'objets ``Allumette``s
    :param str rangee: Numéro de la rangée où la sélection sera réalisée

    :param return: Nouvel indice (curseur) de coups_possibles
    """

    if (rangee is not None and rangee.isnumeric()):
        rangee = int(rangee)

        if ((0 <= indice_coups_possibles + increment_clic
            <= len(coups_possibles)-1)
            and coups_possibles[indice_coups_possibles + increment_clic]
                <= len(liste_allumettes[rangee])):

            indice_coups_possibles += increment_clic
            nb_a_selectionner = coups_possibles[indice_coups_possibles]

        elif increment_clic == -1 and indice_coups_possibles == -1:
            nb_a_selectionner = 0

        else:
            nb_a_selectionner = coups_possibles[indice_coups_possibles]

        graphiques.afficher_selection_allumettes(
            nb_a_selectionner, liste_allumettes, rangee
        )

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


def jouer_tour(liste_allumettes: List[List[Allumette]],
               liste_boutons_jeu: List[Bouton]):
    """
    Supprime les allumettes selctionées dans la liste d'allumettes,
    et inverse la position des boutons 'Joueur' et 'Fin de tour'
    aux indices 0 et 1 de la liste_boutons_jeu

    :param list liste_allumettes: Liste de rangées d'objets ``Allumette``s
    :param list liste_boutons_jeu: Liste d'objets ``Boutons``s
    """

    bouton.intervertir_pos_boutons(liste_boutons_jeu[0], liste_boutons_jeu[1])
    break_rangee = False

    for rangee in range(len(liste_allumettes)-1, -1, -1):
        for allumette in range(len(liste_allumettes[rangee])-1, -1, -1):

            if liste_allumettes[rangee][allumette].selection:
                break_rangee = True
                del liste_allumettes[rangee][allumette]
            else:
                break
        if break_rangee:
            break


def hitbox_marienbad(liste_allumettes: List[List[Allumette]]) -> List[Bouton]:
    """
    Crée un bouton pour chaque rangée de la ``liste_allumettes``,
    le texte de chaque bouton est le numéro de la rangée (Débute à 0).

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
                identificateur=str(i),
                )
        )

    return hitbox_allumettes


def check_hitbox(liste_allumettes: List[List[Allumette]],
                 indice_coups_possibles: int,
                 nom_bouton: str, bouton_precedent: str,
                 tev: str) -> Tuple[int, str]:
    """
    Gère la logique liée à la selection et les appuis
    sur les boutons correspondants
    """

    retour = 0 if tev == "ClicDroit" else -1

    if nom_bouton is not None and nom_bouton.isnumeric():
        music.SoundAllu()
        if bouton_precedent is not None:
            if bouton_precedent is not nom_bouton:
                reset_selection_rangee(liste_allumettes[int(bouton_precedent)])
                return retour, nom_bouton
        return indice_coups_possibles, nom_bouton
    return indice_coups_possibles, bouton_precedent


def initialiser_allumettes(
        liste_marienbad=[cfg.nombre_allumettes]) -> List[List[Allumette]]:
    """
    Initialise une liste d'objets ``Allumette``, dont les coordonnées
    ont été adaptées à la taille de la fenêtre par leurs constantes globales
    """

    liste_allumettes = []
    nb_rangees = len(liste_marienbad)
    nombre_allumettes_max = max(liste_marienbad)
    marge = cfg.hauteur_fenetre*0.1

    espacement_x = cfg.largeur_fenetre / (nombre_allumettes_max+1)
    x_max = (nombre_allumettes_max-1) * espacement_x + cfg.largeur_allumette
    x_centre = (cfg.largeur_fenetre - x_max)/2

    espacement_y = cfg.hauteur_fenetre / (nb_rangees) - marge
    y_max = (nb_rangees-1) * espacement_y + cfg.hauteur_fenetre
    y_centre = (cfg.hauteur_fenetre - y_max)/2 +\
               (cfg.hauteur_fenetre - cfg.hauteur_allumette)/2

    for j in range(nb_rangees):
        ligne_allumettes = []
        for i in range(liste_marienbad[j]):
            ligne_allumettes.append(
                Allumette(
                    ax=i * espacement_x + x_centre,
                    ay=j * espacement_y + y_centre,
                    bx=i * espacement_x + x_centre + cfg.largeur_allumette,
                    by=j * espacement_y + y_centre + cfg.hauteur_allumette
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


def coup_possible(liste_allumettes: List[Allumette],
                  coups_possibles: list) -> bool:
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


def message_de_fin(joueur: int) -> str:
    """
    Retourne le message de fin de partie en fonction de la situation

    :param int joueur: le joueur qui a pris la dernière allumette
    :return str: message qui s'affiche à l'écran de fin
    """
    if cfg.mode_solo and cfg.mode_difficile:
        message = "Comment avez pu croire\nà avoir une chance\nface à 3X-PL0-X10N ?"
        music.song('WORST END')

    elif cfg.misere:
        message = f"Quel dommage Joueur {joueur},\ntu as pris l'allumette de trop !\n:("

    else:
        message = f"Bien joué Joueur {joueur}!\nTu as chapardé la\
        \ndernière allumette !"
    return message


def premier_tour(liste_allumettes: list, coups_gagnants: list) -> int:
    """
    Retourne le joueur qui commence en fonction de la position
    gagnante ou perdante en mode solo et difficulté difficile.

    :param list liste_allumettes: la liste des allumettes en Marienbad
    :param list coups_gagnants: la liste des coups gagnants en jeu classique
    :return int: le joueur qui commence en position gagnante
    """
    joueur = 1
    if len(liste_allumettes) == 1:
        if coups_gagnants[len(liste_allumettes[0])] is not None:
            joueur = 2
    elif int(solo.nimsomme([len(liste_allumettes[x])
             for x in range(len(liste_allumettes))])):
        joueur = 2
    return joueur


def message_interruption():
    """
    Message à l'intention de l'utilisateur qui utiliserait Ctrl+C...
    """
    print("\nVous devriez pouvoir fermer la fenêtre avec la croix",
          "théoriquement...",
          "\nMais merci d'y avoir pris plaisir!! A bientôt!!")
    # fltk.ferme_fenetre()
    exit(0)
