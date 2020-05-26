# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

# =============================================================================
# importations :

import re
# =============================================================================

def ex4(n: int, m: int, days_f: list) -> int:

    assert isinstance(n, int), \
        'n must be a int, not {}'.format(type(n))
    assert isinstance(m, int), \
        'm must be a int, not {}'.format(type(m))
    assert isinstance(days_f, list), \
        'days_f must be a list, not {}'.format(type(days_f))
    assert 1 <= n <= 100, \
        "n must be between 1 and 100    includes, not {}".format(n)
    assert 1 <= m <= 36, \
        "m must be between 1 and 36 includes, not {}".format(m)
    assert len(days_f) == n, \
        "il n'y a pas le même nombre d'amis que de disponibilité {} au lieu " \
        "de {}".format(len(days_f), n)
    for j, i in enumerate(days_f):
        assert 1 <= i <= 10 ** 6, \
            "l'élément {} de days_f n'est pas compris entre 1 et 1000" \
            "".format(j, i)

    amis_vu = 0
    start = days_f[0]
    end = start + m
    while end <= days_f[-1]:

        amis = 0
        for j in days_f:
            if j in list(range(start, end + 1)):
                amis += 1

        if amis > amis_vu:
            amis_vu = amis

        start += 1
        end += 1

    return amis_vu


if __name__ == "__main__":
    # 1ere ligne d'entrée nb_ami et nobre de jours de voyage
    input1 = input("1ere entrée : ")

    # vérification format
    while not re.findall(r"^\d+ \d+$", input1):
        input1 = input('format non valide réessaye : ')

    nb_amis, nb_jours = input1.split(" ")

    # transition str -> int
    nb_amis: int = int(nb_amis)
    nb_jours: int = int(nb_jours)

    # 2e ligne entrée liste d'entiers séparés par un espace
    input2 = input()
    # vérification format
    while not re.findall(" ".join([r"\d+"] * nb_amis), input2):
        input2 = input("format non valide réessaye : ")

    day_with_friends: list = sorted([int(i) for i in input2.split(" ")])
    # le programme appelle la fonction
    print(ex4(nb_amis, nb_jours, day_with_friends))

    # nettoyage de la mémoire vive
    del nb_amis, nb_jours, ex4, day_with_friends
