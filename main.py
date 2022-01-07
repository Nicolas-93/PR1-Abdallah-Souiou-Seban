import fltk
import graphiques
import gameplay
import bouton
import cfg
import animation
import solo
import music


def menu():

    music.initialisation()
    liste_boutons_menu = [
        bouton.cree_bouton_simple(
            0.2, 0.45, 0.8, 0.55,
            'Jeu classique'
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

            fltk.texte(
                cfg.largeur_fenetre//2, cfg.hauteur_fenetre//4,
                'Jeux de Nim', police='Biometric Joe',
                taille=liste_boutons_menu[0].taille_texte*2,
                ancrage='center', couleur='white'
            )

            nom_bouton = bouton.dessiner_boutons(liste_boutons_menu)

            if tev == 'Quitte':
                fltk.ferme_fenetre()
                exit()

            elif tev == "ClicGauche":
                if nom_bouton == 'Jeu classique':
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

    music.song('Neutral')

    if cfg.mode_solo and cfg.mode_difficile:
        message = "Comment avez pu croire\nà avoir une chance\nface à 3X-PL0-X10N ?"
        music.song('WORST END')

    elif cfg.misere:
        message = f"Quel dommage Joueur {joueur},\ntu as pris l'allumette de trop !\n:("

    else:
        message = f"Bien joué Joueur {joueur}!\nTu as chapardé la\
        \ndernière allumette !"

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
                cfg.largeur_fenetre/2, 0.25*cfg.hauteur_fenetre,
                message, couleur="white", ancrage='center',
                police='Biometric Joe',
                taille=liste_boutons_fin[0].taille_texte//2
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

    coeff = graphiques.calcul_taille_image(
        cfg.taille_image,
        (cfg.largeur_allumette, cfg.hauteur_allumette)
    )
    image_allumette = fltk.redimensionner_image('allumette.png', coeff)
    image_allumette_brulee = fltk.redimensionner_image(
        'allumette-brulee.png', coeff
    )
    liste_allumettes = gameplay.initialiser_allumettes(liste_marienbad)
    adversaire = (('3X-PL0-X10N' if cfg.mode_difficile else 'T3R3Z1')
                  if cfg.mode_solo else
                  'Joueur 2')

    bouton_precedent = None
    indice_coups_possibles = -1
    joueur = 1
    coups_possibles = (range(1, max(liste_marienbad) + 1)
                       if len(liste_marienbad) > 1 else
                       cfg.coups_possibles)

    coups_gagnants = solo.coups_gagnants(
        cfg.nombre_allumettes, coups_possibles, cfg.misere
    )
    coup, rangee_coup = coups_gagnants[len(liste_allumettes[0])], 0

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

    if adversaire == "3X-PL0-X10N":
        music.song('3X-PL0-X10N')
        if ((len(liste_allumettes) == 1 and coups_gagnants[len(liste_allumettes[0])] is not None)
        or (len(liste_allumettes) >= 2 and int(solo.nimsomme([len(liste_allumettes[x]) for x in range(len(liste_allumettes))])))):
            joueur = 2
            liste_boutons_jeu[1].etat = False
    else:
        music.song('friendly_duel')
        liste_boutons_jeu[1].etat = True

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
                    (indice_coups_possibles, bouton_precedent) =\
                        gameplay.check_hitbox(
                            liste_allumettes, indice_coups_possibles,
                            nom_bouton, bouton_precedent, tev
                        )
                    indice_coups_possibles =\
                        gameplay.appliquer_selection_allumettes(
                            indice_coups_possibles, 1, coups_possibles,
                            liste_allumettes, nom_bouton
                        )

                if (nom_bouton == 'Fin de tour'
                   and indice_coups_possibles != -1):
                    music.BoutonAccept()
                    gameplay.jouer_tour(liste_allumettes, liste_boutons_jeu)
                    joueur = 3 - joueur
                    if joueur == 2 and cfg.mode_solo:
                        (rangee_coup, coup) = solo.coup_bot(
                            liste_allumettes,
                            coups_gagnants, coups_possibles
                        )

                    indice_coups_possibles = -1
                    liste_boutons_jeu[1].etat = not liste_boutons_jeu[1].etat

            elif tev == "ClicDroit" and (not cfg.mode_solo or joueur == 1):
                (indice_coups_possibles, bouton_precedent) =\
                    gameplay.check_hitbox(
                        liste_allumettes, indice_coups_possibles,
                        nom_bouton, bouton_precedent, tev
                    )
                indice_coups_possibles =\
                    gameplay.appliquer_selection_allumettes(
                        indice_coups_possibles, -1, coups_possibles,
                        liste_allumettes, nom_bouton
                    )

            if cfg.mode_solo and joueur == 2:
                if cfg.mode_difficile and len(liste_allumettes) > 1:
                    rangee_coup, coup = solo.coups_gagnants_marienbad(
                        [len(liste_allumettes[x]) for x in range(len(liste_allumettes))]
                    )

                indice_coups_possibles =\
                    gameplay.appliquer_selection_allumettes(
                        coup, 0, coups_possibles,
                        liste_allumettes, str(rangee_coup)
                    )

            if not gameplay.coup_possible(liste_allumettes, coups_possibles):
                joueur = 3 - joueur
                return joueur

            graphiques.dessiner_allumettes(
                liste_allumettes, image_allumette, image_allumette_brulee
            )

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
            '-10'
        ),
        bouton.cree_bouton_simple(
            0.40, 0.30, 0.50, 0.40,
            '-1'
        ),
        bouton.cree_bouton_simple(
            0.70, 0.30, 0.80, 0.40,
            '+1'
        ),
        bouton.cree_bouton_simple(
            0.85, 0.30, 0.95, 0.40,
            '+10'
        ),
        bouton.cree_bouton_booleen(
            0.05, 0.60, 0.20, 0.7,
            'Animation', cfg.animation,
            'Animé', 'Animé',
            unifier_texte=False
        ),
        bouton.cree_bouton_booleen(
            0.5, 0.15, 0.95, 0.25,
            'Difficulte',
            cfg.mode_difficile,
            'hardcore', 'facile',
            invert_color=True, invisible=(not cfg.mode_solo)
        ),
        bouton.cree_bouton_booleen(
            0.25, 0.60, 0.35, 0.7,
            'Son', cfg.son,
            'Son', 'Son', unifier_texte=False
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

            if tev == 'ClicGauche' and nom_bouton is not None:
                if nom_bouton not in {'Difficulte', 'Nombre', 'Menu'}:
                    music.BoutonAccept()
                if nom_bouton == 'Misere':
                    cfg.misere ^= 1
                    liste_boutons_options[0].etat = cfg.misere
                elif nom_bouton == 'Solo':
                    cfg.mode_solo ^= 1
                    liste_boutons_options[1].etat = cfg.mode_solo
                    liste_boutons_options[10].invisible = not cfg.mode_solo
                elif nom_bouton == 'Difficulte':
                    if not liste_boutons_options[10].invisible:
                        music.BoutonAccept()
                    cfg.mode_difficile ^= 1
                    liste_boutons_options[10].etat ^= 1

                elif nom_bouton == '-10':
                    cfg.nombre_allumettes -= 10
                elif nom_bouton == '-1':
                    cfg.nombre_allumettes -= 1
                elif nom_bouton == '+1':
                    cfg.nombre_allumettes += 1
                elif nom_bouton == '+10':
                    cfg.nombre_allumettes += 10

                elif nom_bouton == 'Animation':
                    cfg.animation ^= 1
                    liste_boutons_options[9].etat = cfg.animation
                elif nom_bouton == 'Son' and music.pygame_available:
                    cfg.son ^= 1
                    liste_boutons_options[11].etat = cfg.son
                    music.toggle_sound()
                elif nom_bouton == 'Menu':
                    music.MenuChange()
                    break

                if cfg.nombre_allumettes < 1:
                    cfg.nombre_allumettes = 1
                liste_boutons_options[2].texte = cfg.nombre_allumettes

            if tev == 'Quitte':
                exit()

            fltk.mise_a_jour()

        except KeyboardInterrupt:
            gameplay.message_interruption()


if __name__ == "__main__":
    if fltk.PIL_AVAILABLE:
        fltk.cree_fenetre(
            cfg.largeur_fenetre, cfg.hauteur_fenetre,
            'Jeux de Nim'
        )
        liste_chute = animation.initialisation(cfg.nombre_allumettes_animation)
        music.song('Neutral')
        menu()
    else:
        print("Veuillez installer PIL pour le bon fonctionnement du projet.")
