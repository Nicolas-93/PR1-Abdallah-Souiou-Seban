

def coups_gagnants(nb_allumettes_max, coups_possibles):
    liste_positions, liste_coups = [], []
    for nb_allumettes in range(nb_allumettes_max + 1):
        liste_positions.append(False)
        liste_coups.append(False)
        for i in range(len(coups_possibles)):
            if nb_allumettes >= coups_possibles[i] and not liste_positions[nb_allumettes - coups_possibles[i]]:
                liste_coups[nb_allumettes] = i
                liste_positions[nb_allumettes] = True
                break
    return liste_coups
