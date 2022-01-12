"""
PROJET 1, TP 11 GROUPE 4
Amal Abdallah, Nicolas Seban, Adam Souiou
"""

import fltk


#------------------------------ Configuration -----------------------------#

largeur_fenetre, hauteur_fenetre    =   500, 500
coups_possibles                     =   [1,2,4,5]
liste_marienbad                     =   [1, 3, 5, 7, 4]
nombre_allumettes                   =   20
misere                              =   False
animation                           =   True
mode_solo                           =   True
mode_difficile                      =   False
son                                 =   True
espacement_allumettes               =   20

#----------------------- A modifier avec précaution -----------------------#

image_allumette                     =   'allumette.png'
image_allumette_brulee              =   'allumette-brulee.png'
taille_image                        =   fltk.taille_image(image_allumette)
nombre_allumettes_animation         =   int((30*(largeur_fenetre*hauteur_fenetre))/(250000))
