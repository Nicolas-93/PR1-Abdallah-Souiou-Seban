import fltk
# Configuration

largeur_fenetre, hauteur_fenetre = 500,500
nombre_allumettes = 10
misere = False
coups_possibles = [1,3,4]
liste_marienbad=[1,3,5,7]
mode_solo = False
mode_difficile = False

zoom_allumette = 0.5
taille_image = fltk.taille_image('allumette.png')
largeur_allumette = zoom_allumette*0.00015*largeur_fenetre*taille_image[0]
hauteur_allumette = zoom_allumette*0.00015*hauteur_fenetre*taille_image[1]
rayon_cercle_allumette = largeur_allumette*0.70

marge = 10
k = 5
