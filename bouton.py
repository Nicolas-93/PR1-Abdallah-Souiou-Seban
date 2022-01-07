"""
PROJET 1, TP 11 GROUPE 4
Amal Abdallah, Nicolas Seban, Adam Souiou
"""

# Sobre bibliothèque pour créer, gérer, et afficher des boutons.
# Permet la création de boutons cliquables simples, de boutons
# booléens qui peuvent enregistrer leur état et l'afficher
# par leur couleur, et de boutons invisibles.

from dataclasses import dataclass
from typing import List, Union
import fltk
import cfg


@dataclass
class Bouton:
    ax: float
    ay: float
    bx: float
    by: float
    identificateur: str
    invisible = False
    factice = False


@dataclass
class BoutonTexte(Bouton):
    texte: str
    taille_texte = None
    unifier_texte = True
    marge_texte = 0.8
    police = 'Biometric Joe'
    couleur_texte = 'black'
    couleur_fond = 'white'


@dataclass
class BoutonSimple(BoutonTexte):
    enable_hovered = True
    couleur_hovered = '#848484'


@dataclass
class BoutonBooleen(BoutonTexte):
    etat: bool
    texte_actif: str
    texte_desactive: str
    couleur_actif = '#0a8029'
    couleur_hovered_actif = '#0b4f34'
    couleur_desactive = '#cf0e0e'
    couleur_hovered_desactive = '#941010'


def cree_bouton_texte(ax: float, ay: float, bx: float, by: float,
                      identificateur: str, **kwargs) -> BoutonTexte:
    """
    Crée un bouton factice (ne change pas de couleur lors de son survol)
    à partir de positions relatives à la fenêtre, avec comme
    identificateur : ``identificateur``. Le libéllé du bouton sera
    celui de l'identificateur.
    Utilise les variables globales ``largeur_fenetre`` et ``hauteur_fenetre``

    :param float ax: Abscisse de a relative, entre 0 et 1 inclus
    :param float ay: Ordonnée de a relative, entre 0 et 1 inclus
    :param float bx: Abscisse de b relative, entre 0 et 1 inclus
    :param float by: Ordonnée de b relative, entre 0 et 1 inclus
    :param str identificateur: Nom du bouton

    :param bool hovered: Optionnel, détermine si le bouton change de couleur
    lors  de son survol. Par défaut: ``True``
    :param str couleur_hovered: Optionnel, couleur du fond du bouton
    lors de son survol par la souris. Par défaut: ``'#848484'``
    :param str police: Optionnel, nom de la typographie à utiliser pour
    le texte du bouton. Par défaut, ``'Biometric Joe'``
    :param bool unifier_texte: Optionnel, spécifie si la taille de texte
    de ce bouton sera pris en compte lors de l'utilisation de
    la fonction unifier_taille_texte()
    :param bool invisible: Optionnel, rend le bouton invisible
    :param bool factice: Optionnel, si à ``True`` le bouton ne
    changera pas de couleur à son survol, et l'appel à dessiner_boutons()
    ne le mentionnera pas

    :return: Objet Bouton factice
    """
    bouton = BoutonTexte(
                ax*cfg.largeur_fenetre,
                ay*cfg.hauteur_fenetre,
                bx*cfg.largeur_fenetre,
                by*cfg.hauteur_fenetre,
                identificateur,
                identificateur
             )
    parse_optionnal_args(kwargs, bouton)

    bouton.taille_texte = taille_texte_bouton(bouton)
    return bouton


def cree_bouton_invisible(ax: float, ay: float, bx: float, by: float,
                          identificateur: str) -> Bouton:
    """
    Crée un bouton invisible à partir de positions relatives à la fenêtre,
    avec comme identificateur : ``identificateur``
    Utilise les variables globales ``largeur_fenetre`` et ``hauteur_fenetre``

    :param float ax: Abscisse de a relative, entre 0 et 1 inclus
    :param float ay: Ordonnée de a relative, entre 0 et 1 inclus
    :param float bx: Abscisse de b relative, entre 0 et 1 inclus
    :param float by: Ordonnée de b relative, entre 0 et 1 inclus
    :param str identificateur: Nom du bouton
    :return: Objet Bouton invisible
    """
    bouton = Bouton(
                ax*cfg.largeur_fenetre,
                ay*cfg.hauteur_fenetre,
                bx*cfg.largeur_fenetre,
                by*cfg.hauteur_fenetre,
                identificateur,
             )
    bouton.invisible = True

    return bouton


def cree_bouton_booleen(
        ax: float, ay: float, bx: float, by: float,
        identificateur: str,
        etat: bool,
        texte_actif: str, texte_desactive: str,
        invert_color=False, **kwargs) -> BoutonBooleen:
    """
    Crée un bouton booléen à partir de positions relatives
    à la fenêtre, et l'initialise à la valeur du booléen ``etat``.
    Le libellé du bouton sera ``texte_actif`` lorsque
    l'attribut ``etat`` du bouton vaut ``True``, sinon
    le libellé ``texte_desactive``.
    Utilise les variables globales ``cfg.largeur_fenetre``
    et ``cfg.hauteur_fenetre``

    :param float ax: Abscisse de a relative, entre 0 et 1 inclus
    :param float ay: Ordonnée de a relative, entre 0 et 1 inclus
    :param float bx: Abscisse de b relative, entre 0 et 1 inclus
    :param float by: Ordonnée de b relative, entre 0 et 1 inclus
    :param str identificateur: Nom du bouton
    :param str texte_actif: Libellé du bouton à l'état actif
    :param str texte_desactive: Libellé du bouton à l'état désactivé
    :param bool invert_color: Inverse la couleur activé/désactivé

    :param str police: Optionnel, nom de la typographie à utiliser pour
    le texte du bouton. Par défaut, ``'Biometric Joe'``
    :param bool unifier_texte: Optionnel, spécifie si la
    taille de texte de ce bouton sera pris en compte lors de
    l'utilisation de la fonction unifier_taille_texte()
    :param bool invisible: Optionnel, rend le bouton invisible
    :param bool factice: Optionnel, si à ``True``,
    le bouton ne changera pas de couleur à son survol, et
    l'appel à dessiner_boutons() ne le mentionnera pas

    :return BoutonBooleen: Objet bouton booléen
    """
    bouton = BoutonBooleen(
                ax*cfg.largeur_fenetre,
                ay*cfg.hauteur_fenetre,
                bx*cfg.largeur_fenetre,
                by*cfg.hauteur_fenetre,
                identificateur,
                '',
                etat,
                texte_actif,
                texte_desactive,
             )
    parse_optionnal_args(kwargs, bouton)
    if invert_color:
        bouton.couleur_actif, bouton.couleur_desactive = \
            bouton.couleur_desactive, bouton.couleur_actif

        bouton.couleur_hovered_actif, bouton.couleur_hovered_desactive = \
            bouton.couleur_hovered_desactive, bouton.couleur_hovered_actif

    bouton.taille_texte = taille_texte_bouton(bouton)

    return bouton


def cree_bouton_simple(ax: float, ay: float, bx: float, by: float,
                       identificateur: str, **kwargs) -> BoutonSimple:
    """
    Crée un bouton simple, c'est à dire survolable, à partir de
    positions relatives à la fenêtre, ayant comme libellé
    et identificateur: ``identificateur``.
    Le paramètre ``hovered`` détermine si le bouton devra changer
    de couleur à son survol.
    Utilise les variables globales ``largeur_fenetre`` et ``hauteur_fenetre``

    :param float ax: Abscisse de a relative, entre 0 et 1 inclus
    :param float ay: Ordonnée de a relative, entre 0 et 1 inclus
    :param float bx: Abscisse de b relative, entre 0 et 1 inclus
    :param float by: Ordonnée de b relative, entre 0 et 1 inclus
    :param str identificateur: Nom et libéllé du bouton

    :param bool hovered: Optionnel, détermine si le bouton change
    de couleur lors de son survol. Par défaut: ``True``
    :param str couleur_hovered: Optionnel, couleur du fond du bouton
    lors de son survol par la souris. Par défaut: ``'#848484'``
    :param str police: Optionnel, nom de la typographie à utiliser
    pour le texte du bouton. Par défaut, ``'Biometric Joe'``
    :param bool unifier_texte: Optionnel, spécifie si la
    taille de texte de ce bouton sera pris en compte lors de l'utilisation
    de la fonction unifier_taille_texte()
    :param bool invisible: Optionnel, rend le bouton invisible
    :param bool factice: Optionnel, si à ``True``, le bouton ne
    changera pas de couleur à son survol, et l'appel à dessiner_boutons()
    ne le mentionnera pas

    :return Bouton: Objet Bouton
    """
    bouton = BoutonSimple(
                ax*cfg.largeur_fenetre,
                ay*cfg.hauteur_fenetre,
                bx*cfg.largeur_fenetre,
                by*cfg.hauteur_fenetre,
                identificateur,
                identificateur
             )
    parse_optionnal_args(kwargs, bouton)

    bouton.taille_texte = taille_texte_bouton(bouton)

    return bouton


def parse_optionnal_args(args: dict, bouton):
    """
    Parsing des arguments optionnels pour les fonctions
    cree_bouton_simple() et cree_bouton_factice()
    """

    for arg, value in args.items():
        if type(bouton) == BoutonSimple:
            if arg == 'hovered':
                bouton.enable_hovered = value
                break
            elif arg == 'couleur_hovered':
                bouton.couleur_hovered = value
                break
        if arg == 'unifier_texte':
            bouton.unifier_texte = value
            break
        elif arg == 'police':
            bouton.police = value
        elif arg == 'invisible':
            bouton.invisible = value
        elif arg == 'factice':
            bouton.factice = value

        else:
            raise KeyError(f"L'argument {arg} n'existe pas, ou le bouton de \
                        type {type(bouton)} ne possède pas la propriété {arg}")


def unifier_taille_texte(liste_boutons: List[Bouton]) -> None:
    """
    Unifie la taille des textes de chaque bouton de la ``liste_boutons``
    à la plus petite taille de texte rencontrée

    :param list liste_boutons: Liste d'objets ``Bouton``
    """

    taille_min = float('inf')
    for bouton in liste_boutons:

        if (bouton.unifier_texte and (not bouton.invisible)
           and (bouton.taille_texte < taille_min)):

            taille_min = bouton.taille_texte

    for bouton in liste_boutons:
        if (not bouton.invisible) and bouton.unifier_texte:
            bouton.taille_texte = taille_min

    return None


def dessiner_bouton(bouton: Bouton) -> bool:
    """
    Dessine un bouton et change sa couleur lors de son survol
    par la souris, si il n'est pas invisible. Et dans le cas d'un
    bouton booléen, change sa couleur en fontion de son attribut ``etat``.
    Renvoie ``True`` si le bouton à été survolé.

    :param Bouton bouton: Objet Bouton
    :return bool: Bouton survolé
    """

    survole = curseur_sur_bouton(bouton) if not bouton.factice else False
    if not bouton.invisible:
        if type(bouton) == BoutonBooleen:
            if survole:
                if bouton.etat:
                    remplissage = bouton.couleur_hovered_actif
                else:
                    remplissage = bouton.couleur_hovered_desactive
            else:
                if bouton.etat:
                    remplissage = bouton.couleur_actif
                else:
                    remplissage = bouton.couleur_desactive
        else:
            if (survole
               and (type(bouton) != BoutonTexte and bouton.enable_hovered)):

                remplissage = bouton.couleur_hovered
            else:
                remplissage = bouton.couleur_fond

        fltk.rectangle(
            bouton.ax, bouton.ay,
            bouton.bx, bouton.by,
            'black',
            remplissage
        )
        fltk.texte(
            (bouton.ax + bouton.bx)/2, (bouton.ay + bouton.by)/2,
            (bouton.texte_actif if bouton.etat else bouton.texte_desactive)
            if type(bouton) == BoutonBooleen else bouton.texte,
            bouton.couleur_texte, 'center',
            bouton.police, bouton.taille_texte
        )

    return survole


def dessiner_boutons(liste_boutons: List[Bouton]) -> str:
    """
    Dessine tous les boutons de la liste, et renvoie également l'identificateur
    d'un bouton si celui-ci est survolé, et ``None`` si aucun ne l'a été.

    :param list liste_boutons: liste d'objets boutons
    :return str: Texte du bouton qui a été survolé
    """

    nom_bouton_survole = None

    for bouton in liste_boutons:
        survole = dessiner_bouton(bouton)
        if survole:
            nom_bouton_survole = bouton.identificateur

    return nom_bouton_survole


def curseur_sur_bouton(Bouton) -> bool:
    """
    Détecte si le curseur est situé sur le rectangle formé par
    ses composantes ax, ay, bx et by, définies dans l'objet Bouton
    et renvoie ``True`` si tel est le cas.

    :param Bouton: Objet ``Bouton``
    :return bool:
    """
    return ((Bouton.ax <= fltk.abscisse_souris() <= Bouton.bx)
            and (Bouton.ay <= fltk.ordonnee_souris() <= Bouton.by))


def taille_texte_bouton(bouton: Union[BoutonSimple, BoutonBooleen]) -> int:
    """
    Détermine une taille de texte optimisé pour le bouton

    :param Bouton bouton: Objet Bouton
    :return int: Taille du texte à utiliser
    """

    hauteur_bouton = (bouton.by - bouton.ay)*bouton.marge_texte
    largeur_bouton = (bouton.bx - bouton.ax)*bouton.marge_texte
    taille_texte = 1

    while True:
        if type(bouton) == BoutonBooleen:
            largeur_hauteur = max(
                fltk.taille_texte(
                    bouton.texte_actif, bouton.police, taille_texte
                ),
                fltk.taille_texte(
                    bouton.texte_desactive, bouton.police, taille_texte
                )
            )
        else:
            largeur_hauteur = fltk.taille_texte(
                bouton.texte, bouton.police, taille_texte
            )

        if (largeur_hauteur[0] > largeur_bouton
           or largeur_hauteur[1] > hauteur_bouton):
            break
        taille_texte += 1

    return taille_texte


def intervertir_pos_boutons(bouton1: Bouton, bouton2: Bouton):
    """
    Intervertit la position de deux boutons
    """
    bouton1.ay, bouton1.by, bouton2.ay, bouton2.by\
        = bouton2.ay, bouton2.by, bouton1.ay, bouton1.by

    bouton1.ax, bouton1.bx, bouton2.ax, bouton2.bx\
        = bouton2.ax, bouton2.bx, bouton1.ax, bouton1.bx

    return None
