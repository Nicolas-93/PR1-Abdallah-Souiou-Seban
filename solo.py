

def coups_gagnants(nb_allumettes_max, coups_possibles, mode_misere):
    liste_positions, liste_coups = [mode_misere], [mode_misere]
    for nb_allumettes in range(1, nb_allumettes_max + 1):
        liste_positions.append(False)
        liste_coups.append(False)
        for i in range(len(coups_possibles)):
            if nb_allumettes >= coups_possibles[i] and not liste_positions[nb_allumettes - coups_possibles[i]]:
                liste_coups[nb_allumettes] = i
                liste_positions[nb_allumettes] = True
                break
    return liste_coups
