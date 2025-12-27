from parola_segreta import PAROLA_SEGRETA, GUESS

def update(guess, parola_segreta, lettera):
    new_guess = ''

    for i, char in enumerate(parola_segreta):
        if char.lower() == lettera.lower():
            new_guess += lettera
        else:
            new_guess += guess[i]

    return new_guess


# INSERIRE QUI IL CODICE PER GIOCARE!
#
#
#
#
#
#
