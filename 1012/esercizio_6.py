parola = input("Inserisci una parola: ")

# parola = "supercalifraginistichespiralidoso"

# vocali = ["albero", "erba", "i", "o", "u"]
vocali = "aeiou"


contatore_vocali = 0

lunghezza_parola = len(parola)
i = 0

while i<lunghezza_parola:
    carattere_da_controllare = parola[i]
    carattere_da_controllare = carattere_da_controllare.lower()

    # if carattere_da_controllare == "a" or carattere_da_controllare == "e" or carattere_da_controllare == "i" or carattere_da_controllare == "o" or carattere_da_controllare == "u":
    if carattere_da_controllare in vocali:
        contatore_vocali = contatore_vocali + 1



    i = i+1

print(f"{parola} contiene {contatore_vocali} vocali")


"pippo"[1]