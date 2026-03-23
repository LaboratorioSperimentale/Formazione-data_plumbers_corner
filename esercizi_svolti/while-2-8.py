# Scrivi un programma che chiede all'utente di inserire una parola.
# Il programma continua finché l’utente non scrive `fine`. Alla fine, il programma stampa quante delle parole che sono state inserite finiscono per vocale.

parola = input("Inserisci una parola: ")

vocali = "aeiou"

parole_fine_vocale = 0

while parola.strip().lower() != "fine":

    if parola[-1] in vocali:
        parole_fine_vocale += 1

    parola = input("Inserisci una parola: ")

print(f"Parole che finiscono per vocale: {parole_fine_vocale}")
