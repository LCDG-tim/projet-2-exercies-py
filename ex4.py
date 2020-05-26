# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme


def ex4(n: int, m: int, days_f: list) -> int:

    assert isinstance(n, int), \
        'n must be a int, not {}'.format(type(n))
    assert isinstance(m, int), \
        'm must be a int, not {}'.format(type(m))
    assert isinstance(days_f, list), \
        'days_f must be a list, not {}'.format(type(days_f))
    assert 1 <= n <= 100, \
        "n must be between 1 and 100 includes, not {}".format(n)
    assert 1 <= m <= 36, \
        "m must be between 1 and 36 includes, not {}".format(m)

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
    nb_amis, nb_jours = input().split(" ")
    nb_amis: int = int(nb_amis)
    nb_jours: int = int(nb_jours)
    day_with_friends: list = sorted([int(i) for i in input().split()])
    print(ex4(nb_amis, nb_jours, day_with_friends))
