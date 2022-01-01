import fltk
# Configuration

largeur_fenetre, hauteur_fenetre = 500,500
nombre_allumettes = 10
misere = True

taille_image = fltk.taille_image('allumette.png')
zoom_allumette = 0.5

largeur_allumette, hauteur_allumette = zoom_allumette*(0.00015*largeur_fenetre)*taille_image[0], (zoom_allumette*0.00015*hauteur_fenetre)*taille_image[1]
rayon_cercle_allumette = largeur_allumette*0.70

marge = 10
k = 5