import fltk
import graphiques
import gameplay
import bouton
import cfg
import animation
import solo
import random
import music

# README
# Mode joueur solo
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

    liste_chute = animation.initialisation(cfg.nombre_allumettes_animation)
    music.initialisation()
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
                    music.GameStart()
                    fin(jeu([cfg.nombre_allumettes]))
                if nom_bouton == 'Jeu de Marienbad':
                    music.GameStart()
                    fin(jeu(cfg.liste_marienbad))
                if nom_bouton == 'Options':
                    music.MenuChange()
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

    if cfg.mode_solo and cfg.mode_difficile:
        music.song('WORST END')
    else:
        music.song('Neutral')
    if cfg.misere:
        message = f"Quel dommage Joueur {joueur},\ntu as pris l'allumette de trop !\n:("
    elif cfg.mode_solo and cfg.mode_difficile:
        message = "Comment pouvez croire\nà avoir une chance\nface à 3X-PL0-X10N ?"
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
                    music.BoutonAccept()
                    if cfg.mode_solo and cfg.mode_difficile:
                        music.song('Neutral')
                    menu()
                if nom_bouton == 'Quitter':
                    fltk.ferme_fenetre()
                    exit()

            fltk.mise_a_jour()

        except KeyboardInterrupt:
            gameplay.message_interruption()


def jeu(liste_marienbad):
    # coup_possibles = gen_set_coup_possibles(cfg.k)
    coeff = graphiques.calcul_taille_image(
        cfg.taille_image,
        (cfg.largeur_allumette, cfg.hauteur_allumette)
    )
    image_allumette = fltk.redimensionner_image('allumette.png', coeff)
    image_allumette_brulee = fltk.redimensionner_image('allumette-brûée.png', coeff)

    bouton_precedent = None
    indice_coups_possibles = -1
    joueur = 1
    adversaire = ("3X-PL0-X10N" if cfg.mode_difficile else "T3R3Z1") if cfg.mode_solo else "Joueur 2"
    liste_allumettes = gameplay.initialiser_allumettes(liste_marienbad)
    coups_possibles = cfg.coups_possibles
    coup, rangee_coup = 0, 0
    if len(liste_marienbad) > 1:
        coups_possibles = range(1, max(liste_marienbad) + 1)

    coups_gagnants = solo.coups_gagnants(cfg.nombre_allumettes, coups_possibles, cfg.misere)

    for coup in coups_gagnants: pass

    if cfg.mode_solo and cfg.mode_difficile:
        music.song('3X-PL0-X10N')
    else:
        music.song('friendly_duel')

    if (cfg.mode_difficile and cfg.mode_solo
        and ((len(liste_allumettes) == 0 and coups_gagnants[len(liste_allumettes[0])] != None)
        or  (len(liste_allumettes) >= 1 and int(solo.nimsomme([len(liste_allumettes[x]) for x in range(len(liste_allumettes))]))))):
        joueur = 2

    liste_boutons_jeu = [
        bouton.cree_bouton_simple(
            0.3, 0.05, 0.7, 0.15,
            'Fin de tour'
        ),
        bouton.cree_bouton_booleen(
            0.3, 0.85, 0.7, 0.95,
            'Joueur', True, 'Joueur 1', adversaire, factice=True
        )
    ] + gameplay.hitbox_marienbad(liste_allumettes)

    while True:
        try:
            fltk.efface_tout()
            graphiques.background("#3f3e47")
            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)

            nom_bouton = bouton.dessiner_boutons(liste_boutons_jeu)
            
            liste_boutons_jeu[1].etat = True if joueur == 1 else False # A optimiser

            if tev == 'Quitte':
                fltk.ferme_fenetre()
                exit()
            elif tev == "ClicGauche":

                if not cfg.mode_solo or joueur == 1:
                    indice_coups_possibles, bouton_precedent = gameplay.check_hitbox(
                        nom_bouton, liste_allumettes, indice_coups_possibles, bouton_precedent, tev
                    )
                    indice_coups_possibles = gameplay.appliquer_selection_allumettes(
                        indice_coups_possibles, 1, coups_possibles,
                        liste_allumettes, nom_bouton
                    )

                if nom_bouton == 'Fin de tour' and indice_coups_possibles != -1:
                    music.BoutonAccept()
                    gameplay.jouer_tour(liste_allumettes, liste_boutons_jeu)
                    joueur = 3 - joueur
                    if joueur == 2 and cfg.mode_solo:
                        if not cfg.mode_difficile:
                            rangee_coup = random.randint(0, len(liste_allumettes) - 1)
                            while not liste_allumettes[rangee_coup] and any(liste_allumettes):
                                rangee_coup = random.randint(0, len(liste_allumettes) - 1)
                        if cfg.mode_difficile and len(liste_allumettes) == 1 and coups_gagnants[len(liste_allumettes[0])] != None:
                            coup = coups_gagnants[len(liste_allumettes[0])]
                        elif len(liste_allumettes[rangee_coup]) > 0:
                            coup = random.randint(0, min(len(coups_possibles), len(liste_allumettes[rangee_coup])) - 1)
                        graphiques.dessiner_allumettes(liste_allumettes, image_allumette, image_allumette_brulee)
                    indice_coups_possibles = -1

            elif tev == "ClicDroit" and (not cfg.mode_solo or joueur == 1):
                indice_coups_possibles, bouton_precedent = gameplay.check_hitbox(
                    nom_bouton, liste_allumettes, indice_coups_possibles, bouton_precedent, tev
                )
                indice_coups_possibles = gameplay.appliquer_selection_allumettes(
                    indice_coups_possibles, -1, coups_possibles,
                    liste_allumettes, nom_bouton
                )

            if cfg.mode_solo and joueur == 2:
                if cfg.mode_difficile and len(liste_allumettes) > 1:
                    rangee_coup, coup = solo.coups_gagnants_marienbad([len(liste_allumettes[x]) for x in range(len(liste_allumettes))])

                indice_coups_possibles = gameplay.appliquer_selection_allumettes(
                    coup, 0, coups_possibles,
                    liste_allumettes, str(rangee_coup)
                )

            if not gameplay.coup_possible(liste_allumettes, coups_possibles):
                joueur = 3 - joueur
                return joueur
            

            graphiques.dessiner_allumettes(liste_allumettes, image_allumette, image_allumette_brulee)

            fltk.mise_a_jour()

        except KeyboardInterrupt:
            gameplay.message_interruption()


def options():
    liste_boutons_options = [
        bouton.cree_bouton_booleen(
            0.05, 0.45, 0.95, 0.55,
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
        bouton.cree_bouton_texte(
            0.55, 0.30, 0.65, 0.40,
            cfg.nombre_allumettes, factice=True
        ),
        bouton.cree_bouton_simple(
            0.05, 0.75, 0.95, 0.85,
            'Menu'
        ),
        bouton.cree_bouton_texte(
            0.05, 0.30, 0.20, 0.40,
            "Nombre", unifier_texte=False, factice=True
        ),
        bouton.cree_bouton_simple(
            0.25, 0.30, 0.35, 0.40,
            '-10', police='Arial'
        ),
        bouton.cree_bouton_simple(
            0.40, 0.30, 0.50, 0.40,
            '-1', police='Arial'
        ),
        bouton.cree_bouton_simple(
            0.70, 0.30, 0.80, 0.40,
            '+1', police='Arial'
        ),
        bouton.cree_bouton_simple(
            0.85, 0.30, 0.95, 0.40,
            '+10', police='Arial'
        ),
        bouton.cree_bouton_booleen(
            0.05, 0.60, 0.20, 0.7,
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
        ),
        bouton.cree_bouton_booleen(
            0.25, 0.60, 0.35, 0.7,
            'Son', cfg.son,
            'Son!', 'Son'
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

            if tev == 'ClicGauche' and nom_bouton != None:
                if nom_bouton not in {'Difficulte', 'Nombre', 'Menu'}:
                    music.BoutonAccept()
                if nom_bouton == 'Misere':
                    cfg.misere = not cfg.misere
                    liste_boutons_options[0].etat = cfg.misere
                if nom_bouton == 'Solo':
                    cfg.mode_solo = not cfg.mode_solo
                    liste_boutons_options[1].etat = cfg.mode_solo
                    liste_boutons_options[10].invisible = not cfg.mode_solo
                if nom_bouton == 'Difficulte':
                    if not liste_boutons_options[10].invisible:
                        music.BoutonAccept()
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
                cfg.nombre_allumettes = 1 if cfg.nombre_allumettes <= 0 else cfg.nombre_allumettes
                liste_boutons_options[2].texte = cfg.nombre_allumettes

                if nom_bouton == 'Animation':
                    cfg.animation = not cfg.animation
                    liste_boutons_options[9].etat = cfg.animation
                if nom_bouton == 'Son':
                    cfg.son = not cfg.son
                    liste_boutons_options[11].etat = cfg.son
                    #toggle_sound()
                if nom_bouton == 'Menu':
                    music.MenuChange()
                    break

            if tev == 'Quitte' or tev == 'Touche' and fltk.touche(ev) == 'Escape':
                exit()

            fltk.mise_a_jour()

        except KeyboardInterrupt:
            gameplay.message_interruption()


if __name__ == "__main__":

    fltk.cree_fenetre(cfg.largeur_fenetre, cfg.hauteur_fenetre, 'Jeux de Nim')
    music.song('Neutral')
    menu()
