import fltk
# Configuration

largeur_fenetre, hauteur_fenetre = 500,500
nombre_allumettes = 10

taille_image = fltk.taille_image('allumette.png')
zoom_allumette = 1

misere = True

largeur_allumette, hauteur_allumette = zoom_allumette*(0.00015*largeur_fenetre)*taille_image[0], (zoom_allumette*0.00015*hauteur_fenetre)*taille_image[1]
rayon_cercle_allumette = largeur_allumette*0.70

marge = 10
k = 5

bouton_fdt_ax, bouton_fdt_ay, bouton_fdt_bx, bouton_fdt_by  = 0.3, 0.05, 0.7, 0.15
bouton_cki_ax, bouton_cki_ay, bouton_cki_bx, bouton_cki_by = 0.3, 0.85, 0.7, 0.95