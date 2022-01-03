import fltk
import graphiques
import gameplay
import bouton
import cfg
import animation

# README
# Mode joueur solo
# Agrémenter le menu
# Changer le mode de selection des allumettes
# Support des champs de texte
# Supporter les textes sur plusieurs lignes dans bouton.py
# Ajuster/Zoomer les allumettes de manière à optimiser l'espace disponible

# Animer le menu avec des allumettes se déplaçant en diagonale
# Effet de disparition des allumettes: les allumer!!

def menu():
    global image_allumette, image_allumette_brulee, liste_chute

    image_allumette = fltk.redimensionner_image('allumette.png', 0.05)
    image_allumette_brulee = fltk.redimensionner_image('allumette-brûée.png', 0.05)

    liste_chute = animation.initialisation(20, image_allumette, image_allumette_brulee)
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
            animation.dessiner(liste_chute)

            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)

            nom_bouton = bouton.dessiner_boutons(liste_boutons_menu)

            if tev == 'Quitte':
                fltk.ferme_fenetre()
                exit()

            elif tev == "ClicGauche":
                if nom_bouton == 'Jeu normal':
                    fin(jeu([cfg.nombre_allumettes]))
                if nom_bouton == 'Jeu de Marienbad':
                    fin(jeu(cfg.liste_marienbad))
                if nom_bouton == 'Options':
                    options()

            fltk.mise_a_jour()

        except KeyboardInterrupt:
            gameplay.message_interruption()


def fin(joueur: int):
    """
    :param int joueur: Numéro du joueur
    """
    global image_allumette, image_allumette_brulee, liste_chute	
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
            animation.dessiner(liste_chute) 

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


def jeu(liste_marienbad):
    # coup_possibles = gen_set_coup_possibles(cfg.k)
    bouton_precedent = None
    indice_coups_possibles = -1
    joueur = 1
    liste_allumettes = gameplay.initialiser_allumettes(liste_marienbad)

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

    while True:
        try:
            fltk.efface_tout()
            graphiques.background("#3f3e47")
            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)

            nom_bouton = bouton.dessiner_boutons(liste_boutons_jeu)

            if tev == 'Quitte':
                fltk.ferme_fenetre()
                exit()

            elif tev == "ClicGauche":
                indice_coups_possibles, bouton_precedent = gameplay.check_hitbox(
                    nom_bouton, liste_allumettes, indice_coups_possibles, bouton_precedent, tev
                )
                indice_coups_possibles = gameplay.appliquer_selection_allumettes(
                    indice_coups_possibles, 1, cfg.coups_possibles,
                    liste_allumettes, nom_bouton
                )

                if nom_bouton == 'Fin de tour' and indice_coups_possibles != -1:
                    gameplay.jouer_tour(liste_allumettes, liste_boutons_jeu)
                    joueur = 2 - (joueur - 1)
                    liste_boutons_jeu[1].texte = f'Joueur {joueur}'
                    indice_coups_possibles = -1

            elif tev == "ClicDroit":
                indice_coups_possibles, bouton_precedent = gameplay.check_hitbox(
                    nom_bouton, liste_allumettes, indice_coups_possibles, bouton_precedent, tev
                )
                indice_coups_possibles = gameplay.appliquer_selection_allumettes(
                    indice_coups_possibles, -1, cfg.coups_possibles,
                    liste_allumettes, nom_bouton
                )

            if not gameplay.coup_possible(liste_allumettes, cfg.coups_possibles):
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
        bouton.cree_bouton_factice(
            0.4, 0.45, 0.6, 0.55,
            cfg.nombre_allumettes
        ),
        bouton.cree_bouton_simple(
            0.2, 0.75, 0.8, 0.85,
            'Menu'
        ),
        bouton.cree_bouton_simple(
            0.2, 0.45, 0.35, 0.55,
            '-10', police='Arial'
        ),
        bouton.cree_bouton_simple(
            0.4, 0.45, 0.5, 0.55,
            '-1', police='Arial'
        ),
        bouton.cree_bouton_simple(
            0.5, 0.45, 0.6, 0.55,
            '+1', police='Arial'
        ),
        bouton.cree_bouton_simple(
            0.65, 0.45, 0.8, 0.55,
            '+10', police='Arial'
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

                if nom_bouton == '-10':
                    cfg.nombre_allumettes -= 10
                if nom_bouton == '-1':
                    cfg.nombre_allumettes -= 1
                if nom_bouton == '+1':
                    cfg.nombre_allumettes += 1
                if nom_bouton == '+10':
                    cfg.nombre_allumettes += 10
                liste_boutons_options[1].texte = cfg.nombre_allumettes

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
