# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

import re


def sum_numbers(string: str) -> int:
    """fonction de l'exercice 3
    ----
    :pre:
        - string est un str
    ;post:
        - somme est un int
    """

    assert isinstance(string, str), \
        "string must be a intager, not {}".format(type(string))

    somme = 0

    regex = "[0-9]+"

    reseacrh = re.search(regex, string)

    while reseacrh is not None:

        start, end = reseacrh.span()

        # si le nombre introduit la chaine et que le nombre n'introduit un mot
        # ou si le nombre ne commence pas un mot ni n'en termine un
        # ou si le nombre termine la chaine et ne termine pas de mot
        if (len(string) == end) \
                or (start == 0 and " " == string[end]) \
                or (re.findall(" [0-9]+ ", string[start - 1:end + 1])) \
                or (end == len(string) and " " == string[start - 1]):

            # le programme ajoute la valeur du nombre
            somme += int(string[start:end])

        # le programme reforme la chaîne sans le nombre traité
        string = string[end:]
        # il relance une recherche
        reseacrh = re.search(regex, string)

    assert isinstance(somme, int), \
        "somme must be a int, not {}".format(type(somme))

    return somme


if __name__ == "__main__":
    print(sum_numbers("hi"))
    print(sum_numbers("who is 1st here"))
    print(sum_numbers("my numbers is 2"))
    print(sum_numbers(
            'This picture is an oil on canvas '
            'painting by Danish artist Anna '
            'Petersen between 1845 and 1910 year'
        )
    )
    print(sum_numbers("5 plus 6 is"))
    print(sum_numbers(''))
