import cfg
import math


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


def strategie_marienbad(liste_allumettes):
    table_binaire, xor, bilan = [], 0, ''
    for i, nb_allumettes in enumerate(liste_allumettes):
        table_binaire.append(format(nb_allumettes, 'b').zfill(int(math.log(max(liste_allumettes), 2)) + 1))
    for i in range(int(math.log(max(liste_allumettes), 2)) + 1):
        [xor := xor ^ x for x in [int(row[i]) for row in table_binaire]]
        bilan += str(xor)
    return bilan
