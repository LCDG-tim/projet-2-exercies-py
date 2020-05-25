# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme

import re


def sum_numbers(string: str) -> int:

    assert isinstance(string, str), "string must be a str, not {}" \
        .format(type(string))

    somme = 0

    regex = (
        "^[0-9]+[^A-Za-z0-9_]|"
        "[^A-Za-z0-9_][0-9]+[^A-Za-z0-9_]|"
        "[^A-Za-z0-9_][0-9]+$|"
        "^[0-9]+$"
        )
    a = re.findall(regex, string)

    for i in a:
        somme += int(i)

    return somme


if __name__ == "__main__":
    tta = sum_numbers("hi 4st 5 dr 2")
    ttb = sum_numbers("5 4st 21 13")
    ttc = sum_numbers("5")
    print(tta)
    print(ttb)
    print(ttc)
