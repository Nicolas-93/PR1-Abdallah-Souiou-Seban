from dataclasses import dataclass
from typing import List, Iterable
import fltk
import cfg

@dataclass
class Bouton:
    ax: float
    ay: float
    bx: float
    by: float
    texte: str
    taille_texte = 19
    police = 'Helvetica'
    couleur_texte = 'black'
    couleur_fond = 'white'
    couleur_hovered = 'green'


def cree_bouton(ax, ay, bx, by, texte):
    """
    Cree un bouton à partir de positions relatives à la fenêtre.
    Utilise les variables globales ``largeur_fenetre`` et ``hauteur_fenetre``
    """
    return Bouton(
                ax*cfg.largeur_fenetre,
                ay*cfg.hauteur_fenetre,
                bx*cfg.largeur_fenetre,
                by*cfg.hauteur_fenetre,
                texte
           )


def dessiner_bouton(Bouton: Bouton):

    fltk.rectangle(
        Bouton.ax, Bouton.ay,
        Bouton.bx, Bouton.by,
        'black',
        Bouton.couleur_hovered if curseur_sur_bouton(Bouton) else Bouton.couleur_fond
    )

    fltk.texte(
        (Bouton.ax + Bouton.bx)/2, (Bouton.ay + Bouton.by)/2,
        Bouton.texte, Bouton.couleur_texte, 'center',
        Bouton.police, Bouton.taille_texte
    )

def dessiner_boutons(liste_boutons: List[Bouton]):
    """
    Dessine tous les boutons de la liste, et renvoie également le texte
    d'un bouton si celui-ci est survolé

    :param list liste_boutons: liste d'objets boutons
    :return str: Texte du bouton qui a été survolé 
    """
    
    nom_bouton_survole = None

    for bouton in liste_boutons:
        dessiner_bouton(bouton)
        if curseur_sur_bouton(bouton):
            nom_bouton_survole = bouton.texte
    
    return nom_bouton_survole


def curseur_sur_bouton(Bouton):
    """
    Détecte si le curseur est situé sur le rectangle formé par ses composantes ax, ay, bx et by, définies dans l'objet Bouton
    Chaque composante doit être compris entre 0 et 1
    et renvoie True si tel est le cas
    """
    return (Bouton.ax <= fltk.abscisse_souris() <= Bouton.bx) and (Bouton.ay <= fltk.ordonnee_souris() <= Bouton.by)




def adapter_cadrage_texte():
    pass