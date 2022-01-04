import fltk
import graphiques
import gameplay
import bouton
import cfg
import animation
import solo
import random

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
    coeff = graphiques.calcul_taille_image(
        cfg.taille_image,
        (cfg.largeur_allumette, cfg.hauteur_allumette)
    )

    image_allumette = fltk.redimensionner_image(cfg.image_allumette, coeff)
    image_allumette_brulee = fltk.redimensionner_image(cfg.image_allumette_brulee, coeff)

    liste_chute = animation.initialisation(20)

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
            if cfg.animation:
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
            
            if cfg.animation:
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
    image_allumette = fltk.redimensionner_image('allumette.png', 0.05)
    image_allumette_brulee = fltk.redimensionner_image('allumette-brûée.png', 0.05)

    bouton_precedent = None
    indice_coups_possibles = -1
    joueur = 1
    liste_allumettes = gameplay.initialiser_allumettes(liste_marienbad)

    coups_gagnants = solo.coups_gagnants(cfg.nombre_allumettes, cfg.coups_possibles)

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
                if not cfg.mode_solo or joueur == 1:
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
                    if joueur == 2 and cfg.mode_solo:
                        liste_boutons_jeu[1].texte = "3X-PL0-X10N"
                    indice_coups_possibles = -1

            elif tev == "ClicDroit" and (not cfg.mode_solo or joueur == 1):
                indice_coups_possibles, bouton_precedent = gameplay.check_hitbox(
                    nom_bouton, liste_allumettes, indice_coups_possibles, bouton_precedent, tev
                )
                indice_coups_possibles = gameplay.appliquer_selection_allumettes(
                    indice_coups_possibles, -1, cfg.coups_possibles,
                    liste_allumettes, nom_bouton
                )

            if cfg.mode_solo and joueur == 2:
                if cfg.mode_difficile:
                    coup = coups_gagnants[len(liste_allumettes[0])]
                elif len(liste_allumettes[0]) > 0:
                    coup = random.randint(0, min(len(cfg.coups_possibles), len(liste_allumettes[0])) - 1)
                indice_coups_possibles = gameplay.appliquer_selection_allumettes(
                    coup, 0, cfg.coups_possibles,
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
            0.05, 0.60, 0.95, 0.70,
            'Misere',
            cfg.misere,
            'Mode misère', 'Mode normal',
            invert_color=True
        ),
        bouton.cree_bouton_booleen(
            0.05, 0.15, 0.45, 0.25,
            'Solo',
            cfg.mode_solo,
            'Mode solo', '2 joueurs'
        ),
        bouton.cree_bouton_factice(
            0.4, 0.45, 0.6, 0.55,
            cfg.nombre_allumettes
        ),
        bouton.cree_bouton_simple(
            0.05, 0.75, 0.95, 0.85,
            'Menu'
        ),
        bouton.cree_bouton_factice(
            0.05, 0.30, 0.95, 0.40,
            "Nombre d'allumettes"
        ),
        bouton.cree_bouton_simple(
            0.05, 0.45, 0.2, 0.55,
            '-10', police='Arial'
        ),
        bouton.cree_bouton_simple(
            0.25, 0.45, 0.35, 0.55,
            '-1', police='Arial'
        ),
        bouton.cree_bouton_simple(
            0.65, 0.45, 0.75, 0.55,
            '+1', police='Arial'
        ),
        bouton.cree_bouton_simple(
            0.8, 0.45, 0.95, 0.55,
            '+10', police='Arial'
        ),
        bouton.cree_bouton_booleen(
            0.05, 0.9, 0.225, 1,
            'Animation', cfg.animation,
            'Animé', 'Non animé',
            unifier_texte=False
        ),
        bouton.cree_bouton_booleen(
            0.5, 0.15, 0.95, 0.25,
            'Difficulte',
            cfg.mode_difficile,
            'difficile', 'facile',
            invert_color=True, invisible=(not cfg.mode_solo)
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
                if nom_bouton == 'Misere':
                    cfg.misere = not cfg.misere
                    liste_boutons_options[0].etat = cfg.misere
                if nom_bouton == 'Solo':
                    cfg.mode_solo = not cfg.mode_solo
                    liste_boutons_options[1].etat = cfg.mode_solo
                    liste_boutons_options[10].invisible = not cfg.mode_solo
                if nom_bouton == 'Difficulte':
                    cfg.mode_difficile = not cfg.mode_difficile
                    liste_boutons_options[10].etat = not liste_boutons_options[10].etat
                if nom_bouton == '-10':
                    cfg.nombre_allumettes -= 10
                if nom_bouton == '-1':
                    cfg.nombre_allumettes -= 1
                if nom_bouton == '+1':
                    cfg.nombre_allumettes += 1
                if nom_bouton == '+10':
                    cfg.nombre_allumettes += 10
                if nom_bouton == 'Animation':
                    cfg.animation = not cfg.animation
                    liste_boutons_options[9].etat = cfg.animation

                cfg.nombre_allumettes = 1 if cfg.nombre_allumettes <= 0 else cfg.nombre_allumettes
                print(cfg.misere)

                liste_boutons_options[2].texte = cfg.nombre_allumettes

                if nom_bouton == 'Menu':
                    break

            if tev == 'Quitte' or tev == 'Touche' and fltk.touche(ev) == 'Escape':
                exit()

            fltk.mise_a_jour()

        except KeyboardInterrupt:
            gameplay.message_interruption()


if __name__ == "__main__":

    fltk.cree_fenetre(cfg.largeur_fenetre, cfg.hauteur_fenetre)

    menu()
