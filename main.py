import fltk
import graphiques
import gameplay
import bouton
import cfg

# Gérer le mode misère/normal
# Mode joueur solo
# Ajuster/Zoomer les allumettes de manière à optimiser l'espace disponible
# Animer le menu avec des allumettes se déplaçant en diagonale
# Chute d'allumettes
# Effet de disparition des allumettes: les allumer!!
# Mettre un beau message en cas de valeurs incohérentes (minimum 30 pages) :)

def fin(joueur: int):
    """
    :param int joueur: Numéro du joueur
    """
    print(f"Lol t'as perdu, Joueur {joueur}")

def menu():

    liste_boutons_menu = [
        bouton.cree_bouton(
            0.2, 0.45, 0.8, 0.55,
            'Jeu normal'
        ),
        bouton.cree_bouton(
            0.2, 0.60, 0.8, 0.70,
            'Jeu de Marienbad'
        ),
        bouton.cree_bouton(
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

            fltk.mise_a_jour()

        except KeyboardInterrupt:
            gameplay.message_interruption()            


def jeu():
    # coup_possibles = gen_set_coup_possibles(cfg.k)
    hitbox_allumettes = bouton.cree_bouton(0, 0.5, 1, 0.7, '')
    selection = 0
    joueur = 1
    coup_possibles = [1,2,4,5]
    liste_allumettes = gameplay.initialiser_allumettes()
    liste_boutons_jeu = [
        bouton.cree_bouton(
            cfg.bouton_fdt_ax, cfg.bouton_fdt_ay, cfg.bouton_fdt_bx, cfg.bouton_fdt_by,
            'Fin de tour'
        ),
        bouton.cree_bouton(
            cfg.bouton_cki_ax, cfg.bouton_cki_ay, cfg.bouton_cki_bx, cfg.bouton_cki_by, 
            "Joueur 1", hovered=False
        )
    ]
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
                if (bouton.curseur_sur_bouton(hitbox_allumettes)
                and gameplay.selection_possible(liste_allumettes, selection, coup_possibles)):
                    selection = gameplay.selectionCoups(selection, 1, coup_possibles)

                if nom_bouton == 'Fin de tour':
                    gameplay.jouer_tour(selection, liste_allumettes, coup_possibles)
                    bouton.intervertir_pos_boutons(liste_boutons_jeu[0], liste_boutons_jeu[1])
                    joueur = 2 - (joueur - 1)
                    liste_boutons_jeu[1].texte = f"Joueur {joueur}"
                    selection = 0

            elif tev == "ClicDroit":
                if bouton.curseur_sur_bouton(hitbox_allumettes):
                    selection = gameplay.selectionCoups(selection, -1, coup_possibles)
            
            if not gameplay.coup_possible(liste_allumettes, coup_possibles):
                joueur = 2 - (joueur - 1)
                return joueur

            graphiques.dessiner_allumettes(liste_allumettes, image_allumette, image_allumette_brulee)
            graphiques.encadre(liste_allumettes, selection, coup_possibles)

            fltk.mise_a_jour()

        except KeyboardInterrupt:
            gameplay.message_interruption()


if __name__ == "__main__":
    
    fltk.cree_fenetre(cfg.largeur_fenetre, cfg.hauteur_fenetre)
    
    menu()
