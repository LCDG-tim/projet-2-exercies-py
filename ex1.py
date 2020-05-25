# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

"""

exercie 1 du projet :

réaliser un pgm de calcul de masse

"""

# =============================================================================
# importations :

import re
# =============================================================================


def calul(poids: int) -> int:
    """fct qui calcule la poids de carburant pour une personne selon son poids
    ----
    :pre:
        - poids est un int

    :post:
        - return_value est un int
    """
    pass


def ex1(n: int, weight: str) -> None:
    """fonction de l'exercice 1
    ----
    :pre:
        - n est un int compis entre 0 et 100 inclus

    :post:
        - p est int compris entre 1 et 1 000 inclus
    """

    assert 0 <= n <= 100, \
        "le nombre de passagers n'est pas convenable, il vaut {}".format(n)

    poids_carbu = 0
    for i in weight.split(" "):
        poids_carbu += (60, 80)[int(i) > 90]
        # condition ternaire
        # 60 si poids <= 90
        # 80 = 60 + 20 si poids > 90

    assert 1 <= poids_carbu <= 1_000, \
        "le poids nécessaire est supérieur à 1 000 kg, il est de {}" \
        .format(poids_carbu)

    return poids_carbu


if __name__ == "__main__":

    nb_passengers = input()
    while re.search("[0-9]+", nb_passengers) is None:
        nb_passengers = input("mauvais format = ")

    nb_passengers = int(nb_passengers)

    weights_passengers = input()
    while re.search(" ".join(["[0-9]+"]*nb_passengers), weights_passengers) \
            is None:
        weights_passengers = input("mauvais format =")

    print("\n{}".format(ex1(nb_passengers, weights_passengers)))
