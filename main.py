import fltk
import graphiques
import gameplay
import bouton
import cfg


def fin():
    print(f"Lol ta perdu, Joueur {joueur} (t'-'t) ")
    exit(0)


liste_boutons_jeu = []
liste_boutons_jeu.append(
    bouton.cree_bouton(
        0.3, 0.05, 0.7, 0.15,
        'Fin de tour'
    )
)
hitbox_allumettes = bouton.cree_bouton(0, 0.5, 1, 0.7, '')
selection = 0
joueur = 1

if __name__ == "__main__":

    # coup_possibles = gen_set_coup_possibles(cfg.k)
    coup_possibles = [1,2,4,5]
    liste_allumettes = gameplay.initialiser_allumettes()

    fltk.cree_fenetre(cfg.largeur_fenetre, cfg.hauteur_fenetre)
    while True:
        try:
            fltk.efface_tout()
            fltk.rectangle(0, 0, cfg.largeur_fenetre, cfg.hauteur_fenetre, remplissage = "#3f3e47")
            ev = fltk.donne_ev()
            tev = fltk.type_ev(ev)

            nom_bouton = bouton.dessiner_boutons(liste_boutons_jeu)

            if tev == 'Quitte':
                fltk.ferme_fenetre()
                exit()

            elif tev == "ClicGauche":
                if (bouton.curseur_sur_bouton(hitbox_allumettes)
                    and gameplay.selection_possible(liste_allumettes, selection, coup_possibles)):
                    selection = gameplay.selectionCoups(selection, 1, coup_possibles)

                if nom_bouton == 'Fin de tour':
                    gameplay.jouer_tour(selection, liste_allumettes, coup_possibles)
                    joueur = 2 - (joueur - 1)
                    selection = 0

            elif tev == "ClicDroit":
                if bouton.curseur_sur_bouton(hitbox_allumettes):
                    selection = gameplay.selectionCoups(selection, -1, coup_possibles)
            
            if not gameplay.coup_possible(liste_allumettes, coup_possibles):
                joueur = 2 - (joueur - 1)
                fin()

            graphiques.dessiner_allumettes(liste_allumettes)
            
            graphiques.encadre(liste_allumettes, selection, coup_possibles)

            fltk.texte(
                cfg.largeur_fenetre/2, 100, f'Joueur {joueur}',
                couleur='white', ancrage='center', police='Helvetica', taille=24)

            fltk.mise_a_jour()

        except KeyboardInterrupt:
            print("\nVous devriez pouvoir fermer la fenêtre avec la croix",
                  "théoriquement...",
                  "\nMais merci d'y avoir pris plaisir!! A bientôt!!")
            break


