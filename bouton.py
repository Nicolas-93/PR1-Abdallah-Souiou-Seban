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
    enable_hovered : bool    
    taille_texte = None
    marge_texte = 0.8 # Proportion du texte par rapport au cadre
    police = 'Biometric Joe'
    couleur_texte = 'black'
    couleur_fond = 'white'
    couleur_hovered = '#848484'


def cree_bouton(ax: float, ay: float, bx: float, by: float, texte: str, hovered=True) -> Bouton:
    """
    Crée un bouton à partir de positions relatives à la fenêtre,
    et avec le libellé ``texte``
    Utilise les variables globales ``largeur_fenetre`` et ``hauteur_fenetre``
    
    :param float ax: Abscisse de a relative, entre 0 et 1 inclus
    :param float ay: Ordonnée de a relative, entre 0 et 1 inclus
    :param float bx: Abscisse de b relative, entre 0 et 1 inclus
    :param float by: Ordonnée de b relative, entre 0 et 1 inclus
    :param str texte: Libellé du bouton
    :return Bouton: Objet Bouton
    """
    bouton = Bouton(
                ax*cfg.largeur_fenetre,
                ay*cfg.hauteur_fenetre,
                bx*cfg.largeur_fenetre,
                by*cfg.hauteur_fenetre,
                texte, hovered
             )
    bouton.taille_texte = taille_texte_bouton(bouton)
    return bouton
    

def unifier_taille_texte(liste_boutons):

    taille_min = float('inf')
    for bouton in liste_boutons:
        if bouton.taille_texte < taille_min:
            taille_min = bouton.taille_texte
    
    for bouton in liste_boutons:
        bouton.taille_texte = taille_min


def dessiner_bouton(bouton: Bouton) -> bool:
    """
    Dessine un bouton et change sa couleur lors de son survole
    par la souris.
    Et renvoie ``True`` si le bouton à été survolé.

    :param Bouton bouton: Objet Bouton
    :return bool: Bouton survolé
    """

    survole = curseur_sur_bouton(bouton)
    fltk.rectangle(
        bouton.ax, bouton.ay,
        bouton.bx, bouton.by,
        'black',
        bouton.couleur_hovered if ( survole and bouton.enable_hovered) else bouton.couleur_fond
    )

    fltk.texte(
        (bouton.ax + bouton.bx)/2, (bouton.ay + bouton.by)/2,
        bouton.texte, bouton.couleur_texte, 'center',
        bouton.police, bouton.taille_texte
    )

    return survole


def dessiner_boutons(liste_boutons: List[Bouton]):
    """
    Dessine tous les boutons de la liste, et renvoie également le texte
    d'un bouton si celui-ci est survolé

    :param list liste_boutons: liste d'objets boutons
    :return str: Texte du bouton qui a été survolé 
    """
    
    nom_bouton_survole = None

    for bouton in liste_boutons:
        survole = dessiner_bouton(bouton)
        if survole:
            nom_bouton_survole = bouton.texte
    
    return nom_bouton_survole


def curseur_sur_bouton(Bouton):
    """
    Détecte si le curseur est situé sur le rectangle formé par ses composantes ax, ay, bx et by,
    définies dans l'objet Bouton
    Chaque composante doit être compris entre 0 et 1
    et renvoie True si tel est le cas
    """
    return ((Bouton.ax <= fltk.abscisse_souris() <= Bouton.bx)
            and (Bouton.ay <= fltk.ordonnee_souris() <= Bouton.by))


def taille_texte_bouton(bouton: Bouton):
    """
    Détermine une taille de texte optimisé pour le bouton

    :param Bouton bouton: Objet Bouton
    :return int: Taille du texte à utiliser
    """

    hauteur_bouton = (bouton.by - bouton.ay)*bouton.marge_texte
    largeur_bouton = (bouton.bx - bouton.ax)*bouton.marge_texte
    taille_texte = 1

    while True:
        largeur_hauteur = fltk.taille_texte(bouton.texte, bouton.police, taille_texte)
        if largeur_hauteur[0] > largeur_bouton or largeur_hauteur[1] > hauteur_bouton:
            break
        taille_texte += 1

    return taille_texte


def intervertir_pos_boutons(bouton1: Bouton, bouton2: Bouton):
    bouton1.ay, bouton1.by, bouton2.ay, bouton2.by = bouton2.ay, bouton2.by, bouton1.ay, bouton1.by
    bouton1.ax, bouton1.bx, bouton2.ax, bouton2.bx = bouton2.ax, bouton2.bx, bouton1.ax, bouton1.bx