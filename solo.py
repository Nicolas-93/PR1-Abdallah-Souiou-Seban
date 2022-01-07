import cfg
import math
import random


def coups_gagnants(nb_allumettes_max, coups_possibles, mode_misere):
    liste_positions, liste_coups = [mode_misere], [mode_misere]
    for nb_allumettes in range(1, nb_allumettes_max + 1):
        liste_positions.append(False)
        liste_coups.append(None)
        for i in range(0, len(coups_possibles)):
            if nb_allumettes >= coups_possibles[i] and not liste_positions[nb_allumettes - coups_possibles[i]]:
                liste_coups[nb_allumettes] = i
                liste_positions[nb_allumettes] = True
    return liste_coups


def nimsomme(liste_allumettes):
    table_binaire, xor, bilan = [], 0, '0'
    if max(liste_allumettes):
        for nb_allumettes in liste_allumettes:
            table_binaire.append(format(nb_allumettes, 'b').zfill(int(math.log(max(liste_allumettes), 2)) + 1))
        for i in range(int(math.log(max(liste_allumettes), 2)) + 1):
            for x in [int(row[i]) for row in table_binaire]: xor = xor ^ x
            bilan += str(xor)
    return bilan


def coups_gagnants_marienbad(liste_allumettes):
    for rangee in range(len(liste_allumettes)):
        for coup in range(liste_allumettes[rangee] + 1):
            liste_arrivee = liste_allumettes[::]
            liste_arrivee[rangee] -= coup
            if not (cfg.misere ^ int(nimsomme(liste_arrivee))):
                return rangee, coup - 1
    return None, None


def coup_bot(liste_allumettes, coups_gagnants, coups_possibles):
    rangee_coup, coup = 0, 0
    if not cfg.mode_difficile:
        rangee_coup = random.randint(0, len(liste_allumettes) - 1)
        while not liste_allumettes[rangee_coup] and any(liste_allumettes):
            rangee_coup = random.randint(0, len(liste_allumettes) - 1)
    if cfg.mode_difficile and len(liste_allumettes) == 1 and coups_gagnants[len(liste_allumettes[0])] != None:
        coup = coups_gagnants[len(liste_allumettes[0])]
    elif len(liste_allumettes[rangee_coup]) > 0:
        coup = random.randint(0, min(len(coups_possibles), len(liste_allumettes[rangee_coup])) - 1)
    return rangee_coup, coup
