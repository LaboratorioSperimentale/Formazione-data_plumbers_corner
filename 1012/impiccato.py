from parola_segreta import PAROLA_SEGRETA, GUESS

def update(guess, parola_segreta, lettera):
    new_guess = ''

    for i, char in enumerate(parola_segreta):
        if char.lower() == lettera.lower():
            new_guess += lettera
        else:
            new_guess += guess[i]

    return new_guess


while GUESS != PAROLA_SEGRETA:
	nuova_lettera = input("Inserisci una lettera! ")
	GUESS = update(GUESS, PAROLA_SEGRETA, nuova_lettera.strip())

	print("Stato corrente:", GUESS)

print("Hai indovinato! La parola era", PAROLA_SEGRETA)