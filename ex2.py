# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme


def sans_interference(nb_carract: int, message: str):

    assert isinstance(nb_carract, int), "nb_carract must be a int, not {}" \
        .format(type(nb_carract))
    assert len(message) == nb_carract, \
        "error of according {} characters instead of {} annonced" \
        .format(len(message), nb_carract)

    real_message = ""
    astesrix = False

    for i in message:

        if i == "*":
            astesrix = not astesrix

        elif i != "." and not astesrix:
            real_message += i

    assert isinstance(real_message, str), \
        "real_message must be a int, not {}".format(type(real_message))

    return real_message


if __name__ == "__main__":

    nb_carract = input("nombre de caractère ")
    message = input("message ")

    print(sans_interference(int(nb_carract), message))
