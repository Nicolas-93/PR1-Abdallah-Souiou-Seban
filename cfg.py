"""
PROJET 1, TP 11 GROUPE 4
Amal Abdallah, Nicolas Seban, Adam Souiou
"""

import fltk


#------------------------------ Configuration -----------------------------#

largeur_fenetre, hauteur_fenetre    =   800, 640
coups_possibles                     =   [1,2,4,5]
liste_marienbad                     =   [1,3,5,7]
nombre_allumettes                   =   21
misere                              =   False
animation                           =   True
mode_solo                           =   True
mode_difficile                      =   False
son                                 =   True

#----------------------- A modifier avec précaution -----------------------#

zoom_allumette                      =   0.5
image_allumette                     =   'allumette.png'
image_allumette_brulee              =   'allumette-brulee.png'
taille_image                        =   fltk.taille_image(image_allumette)
largeur_allumette                   =   zoom_allumette*0.00015*largeur_fenetre*taille_image[0]
hauteur_allumette                   =   zoom_allumette*0.00015*hauteur_fenetre*taille_image[1]
nombre_allumettes_animation         =   int((30*(largeur_fenetre*hauteur_fenetre))/(250000))
