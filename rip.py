
def gen_dico_coups_possibles(k):
    """
    Initialise un dictionnaire associant les coups
    possibles à un booléen indiquant True, (qui sera
    modifié afin d'indiquer si le coup associé pourra être
    utilisé)

    :param k int: Nombre d'allumettes que pourra tirer un joueur
    """
    return {coup: True for coup in range(1, k)}


def coup_possible(liste_allumettes: List[Allumette], k_coups_possibles: Dict) -> bool:
    """
    Retourne ``True`` si le prochain joueur pourra prélever une allumette.

    :param list liste_allumettes: liste d'objets allumettes
    :param dict k_coups_possibles: Dictionnaire contenant les
    """

    nombre_allumettes_actuel = len(liste_allumettes)
    
    for key, value in k_coups_possibles:
        if value:
            if key <= nombre_allumettes_actuel:
                return True
    return False


k_coups_possibles = gen_dico_coups_possibles(k)



