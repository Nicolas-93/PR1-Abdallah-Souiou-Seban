import fltk
# Configuration

largeur_fenetre, hauteur_fenetre    =   500, 500
nombre_allumettes                   =   10
misere                              =   False
coups_possibles                     =   [1,2,4,5]
liste_marienbad                     =   [1,3,5,7]
animation                           =   True
zoom_allumette                      =   0.5
image_allumette                     =   'allumette.png'
image_allumette_brulee              =   'allumette-brûée.png'
mode_solo                           =   False
mode_difficile                      =   False
son                                 =   True


taille_image                        =   fltk.taille_image(image_allumette)
largeur_allumette                   =   zoom_allumette*0.00015*largeur_fenetre*taille_image[0]
hauteur_allumette                   =   zoom_allumette*0.00015*hauteur_fenetre*taille_image[1]
