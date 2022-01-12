"""
PROJET 1, TP 11 GROUPE 4
Amal Abdallah, Nicolas Seban, Adam Souiou
"""

import cfg
import math
import random
from typing import List, Tuple


def coups_gagnants(
   nb_allumettes_depart: int, coups_possibles: List[int]) -> List[int]:
    """
    Retourne la liste des indices des coups gagnants de la liste
    des coups possibles en fonction du nombre d'allumettes de départ
    et de la liste des coups possibles pour le jeu classique et None
    pour les situations où le joueur est en position perdante.

    :param int nb_allumettes_depart: nombre d'allumettes au début du jeu
    :param list coups_possibles: liste des coups possibles
    :return list: liste de coups gagnants pour le jeu classique
    """
    liste_positions, liste_coups = [cfg.misere], [cfg.misere]
    for nb_allumettes in range(1, nb_allumettes_depart + 1):
        liste_positions.append(False)
        liste_coups.append(None)
        for i in range(0, len(coups_possibles)):
            if (nb_allumettes >= coups_possibles[i]
               and not liste_positions[nb_allumettes - coups_possibles[i]]):
                liste_coups[nb_allumettes] = i
                liste_positions[nb_allumettes] = True
    return liste_coups


def nimsomme(liste_allumettes: List[int]) -> str:
    """
    Retourne la nimsomme de la liste des allumettes par rangée
    passée en paramètre convertie en binaire pour le jeu Marienbad.

    :param list liste_allumettes: liste du nombre d'allumettes par rangée
    :return str: nimsomme de la liste des allumettes en Marienbad
    """
    table_binaire, xor, nimsomme = [], 0, ''
    if max(liste_allumettes):
        for nb_allumettes in liste_allumettes:
            digits = int(math.log(max(liste_allumettes), 2)) + 1
            table_binaire.append(format(nb_allumettes, 'b').zfill(digits))
        for i in range(int(math.log(max(liste_allumettes), 2)) + 1):
            for x in [int(row[i]) for row in table_binaire]:
                xor = xor ^ x
            nimsomme += str(xor)
    if len(nimsomme) == nimsomme.count('0'):
        return 0
    if len(nimsomme) == nimsomme.count('1'):
        return 1
    return nimsomme


def coups_gagnants_marienbad(liste_allumettes: List[int]) -> Tuple[int, int]:
    """
    Retourne le nombre d'allumettes à prendre et la rangée correspondante
    le plus simple en fonction du nombre d'allumettes dans chaque rangée.
    Retourne None si la position est perdante pour le joueur.

    :param list liste_allumettes: liste du nombre d'allumettes par rangée
    :return tuple: nombre d'allumettes à prendre et leur rangée
    """

    new_allumettes = [len(liste_allumettes[x]) for x in range(len(liste_allumettes))]

    for rangee in range(len(new_allumettes)):
        for coup in range(1, new_allumettes[rangee] + 1):
            liste_arrivee = new_allumettes[::]
            liste_arrivee[rangee] -= coup
            if not cfg.misere and nimsomme(liste_arrivee) == 0:
                return rangee, coup - 1
            if cfg.misere and int(nimsomme(liste_arrivee)) == 1:
                return rangee, coup - 1
    return None, None


def coup_bot(liste_allumettes: List[int],
             coups_gagnants: List[int],
             coups_possibles: List[int]) -> Tuple[int, int]:
    """
    Retourne le nombre d'allumettes à prendre et la rangée correspondante
    pour le bot en fonction du mode normal ou misère, de la difficulté
    facile ou difficile et du jeu de Nim ou de Marienbad.
    En mode facile, retoune des nombres aléatoires.
    En mode difficile, retourne le coup gagnant en fonction des modes de jeu.

    :param list liste_allumettes: liste du nombre d'allumettes par rangée
    :param list coups_gagnants: liste des coups gagnants en jeu classique
    :param list coups_possibles: liste des coups possibles en jeu classique
    :return tuple: nombre d'allumettes à prendre et leur rangée
    """
    rangee_coup, coup = 0, 0
    if not cfg.mode_difficile:
        rangee_coup = random.randint(0, len(liste_allumettes) - 1)
        while not liste_allumettes[rangee_coup] and any(liste_allumettes):
            rangee_coup = random.randint(0, len(liste_allumettes) - 1)
    if (cfg.mode_difficile and len(liste_allumettes) == 1
       and coups_gagnants[len(liste_allumettes[0])] is not None):
        coup = coups_gagnants[len(liste_allumettes[0])]
    elif len(liste_allumettes[rangee_coup]) > 0:
        coup = random.randint(0, min(len(coups_possibles),
                                     len(liste_allumettes[rangee_coup])) - 1)
    return rangee_coup, coup
