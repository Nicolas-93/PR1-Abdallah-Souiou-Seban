import fltk
import graphiques
import gameplay
import bouton
import cfg

# Mode joueur solo
# Ajuster/Zoomer les allumettes de manière à optimiser l'espace disponible
# Animer le menu avec des allumettes se déplaçant en diagonale
# Chute d'allumettes
# Effet de disparition des allumettes: les allumer!!
# Mettre un beau message en cas de valeurs incohérentes (minimum 30 pages) :)
# README

def fin(joueur: int):
    """
    :param int joueur: Numéro du joueur
    """
    liste_boutons_fin = [
        bouton.cree_bouton_simple(
            0.1, 0.6, 0.45, 0.8,
            "Menu",
            couleur_hovered='#0b8a68'
        ),
        bouton.cree_bouton_simple(
            0.55, 0.6, 0.9, 0.8,
            "Quitter",
            couleur_hovered='#c21532'
        )  
    ]
    bouton.unifier_taille_texte(liste_boutons_fin)

    if cfg.misere:
        message = f"Quel dommage Joueur {joueur},\ntu as pris l'allumette de trop !\n:("
    else:
        message = f"Bien joué Joueur {joueur}!\nTu as chapardé la\ndernière allumette !\n:D"

    while True:
        try:
            fltk.efface_tout()
            graphiques.background("#3f3e47")

            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)

            nom_bouton = bouton.dessiner_boutons(liste_boutons_fin)
            fltk.texte(
                cfg.largeur_fenetre/2, 0.2*cfg.hauteur_fenetre,
                message, couleur= "white", ancrage='center', police='Biometric Joe', taille = 20
            )

            if tev == 'Quitte':
                fltk.ferme_fenetre()
                exit()

            elif tev == "ClicGauche":
                if nom_bouton == 'Menu':
                    menu()
                if nom_bouton == 'Quitter':
                    fltk.ferme_fenetre()
                    exit()

            fltk.mise_a_jour()

        except KeyboardInterrupt:
            gameplay.message_interruption()

def menu():

    liste_boutons_menu = [
        bouton.cree_bouton_simple(
            0.2, 0.45, 0.8, 0.55,
            'Jeu normal'
        ),
        bouton.cree_bouton_simple(
            0.2, 0.60, 0.8, 0.70,
            "Jeu de Marienbad"
        ),
        bouton.cree_bouton_simple(
            0.2, 0.75, 0.8, 0.85,
            'Options'
        )
    ]
    bouton.unifier_taille_texte(liste_boutons_menu)

    while True:
        try:
            fltk.efface_tout()
            graphiques.background("#3f3e47")

            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)

            nom_bouton = bouton.dessiner_boutons(liste_boutons_menu)

            if tev == 'Quitte':
                fltk.ferme_fenetre()
                exit()

            elif tev == "ClicGauche":
                if nom_bouton == 'Jeu normal':
                    fin(jeu())
                if nom_bouton == 'Options':
                    options()

            fltk.mise_a_jour()

        except KeyboardInterrupt:
            gameplay.message_interruption()


def jeu():
    # coup_possibles = gen_set_coup_possibles(cfg.k)
    indice_coups_possibles = -1
    joueur = 1
    coups_possibles = [1,2,4,5]
    liste_allumettes = gameplay.initialiser_allumettes(liste_marienbad=[1,3,5,7])

    liste_boutons_jeu = [
        bouton.cree_bouton_simple(
            0.3, 0.05, 0.7, 0.15,
            'Fin de tour'
        ),
        bouton.cree_bouton_factice(
            0.3, 0.85, 0.7, 0.95,
            "Joueur 1"
        )
    ] + gameplay.hitbox_marienbad(liste_allumettes)

    coeff = graphiques.calcul_taille_image(
        cfg.taille_image,
        (cfg.largeur_allumette, cfg.hauteur_allumette)
    )
    image_allumette = fltk.redimensionner_image('allumette.png', coeff)
    image_allumette_brulee = fltk.redimensionner_image('allumette-brûée.png', coeff)

    while True:
        try:
            fltk.efface_tout()
            graphiques.background("#3f3e47")
            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)

            nom_bouton = bouton.dessiner_boutons(liste_boutons_jeu)

            #fltk.ligne(cfg.largeur_fenetre/2, 0, cfg.largeur_fenetre/2, cfg.hauteur_fenetre)

            if tev == 'Quitte':
                fltk.ferme_fenetre()
                exit()

            elif tev == "ClicGauche":
                indice_coups_possibles = gameplay.appliquer_selection_allumettes(
                    indice_coups_possibles, 1, coups_possibles,
                    liste_allumettes, nom_bouton
                )

                if nom_bouton == 'Fin de tour': # et vérifier si la selection a bien été effectuée?
                    gameplay.jouer_tour(liste_allumettes, liste_boutons_jeu)
                    joueur = 2 - (joueur - 1)
                    liste_boutons_jeu[1].texte = f'Joueur {joueur}'
                    indice_coups_possibles = -1

            elif tev == "ClicDroit":
                indice_coups_possibles = gameplay.appliquer_selection_allumettes(
                    indice_coups_possibles, -1, coups_possibles,
                    liste_allumettes, nom_bouton
                )

            if not gameplay.coup_possible(liste_allumettes, coups_possibles):
                joueur = 2 - (joueur - 1)
                return joueur


            graphiques.dessiner_allumettes(liste_allumettes, image_allumette, image_allumette_brulee)
            
            fltk.mise_a_jour()

        except KeyboardInterrupt:
            gameplay.message_interruption()


def options():
    liste_boutons_options = [
        bouton.cree_bouton_booleen(
            0.2, 0.60, 0.8, 0.70,
            'Mode',
            cfg.misere,
            'Mode misère', 'Mode normal'
        ),
        bouton.cree_bouton_simple(
            0.2, 0.75, 0.8, 0.85,
            'Menu'
        )
    ]

    bouton.unifier_taille_texte(liste_boutons_options)
    while True:
        try:
            fltk.efface_tout()
            graphiques.background("#3f3e47")
            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)

            nom_bouton = bouton.dessiner_boutons(liste_boutons_options)

            if tev == 'ClicGauche':
                if nom_bouton == 'Mode':
                    cfg.misere = not cfg.misere
                    liste_boutons_options[0].etat = cfg.misere

                if nom_bouton == 'Menu':
                    break

            if tev == 'Quitte' or tev == 'Touche' and fltk.touche(ev) == 'Escape':
                break

            fltk.mise_a_jour()

        except KeyboardInterrupt:
            gameplay.message_interruption()


if __name__ == "__main__":

    fltk.cree_fenetre(cfg.largeur_fenetre, cfg.hauteur_fenetre)

    menu()
