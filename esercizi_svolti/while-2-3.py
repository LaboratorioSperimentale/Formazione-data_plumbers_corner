# Scrivi un programma che legge un numero compreso tra 1 e 10 (controlla che il numero inserito sia lecito, altrimenti stampa un messaggio di errore!) e stampa la tabellina di quel numero.
# Se ad esempio viene inserito il numero 3, il programma deve stampare:
# 	```
# 	3 x 0 = 0
# 	3 x 1 = 3
# 	3 x 2 = 6
# 	...
# 	3 x 10 = 30
# 	```
# 	Usa le `formatted strings`!

numero = int(input("Inserisci un numero tra 1 e 10: "))

# if 1<=numero<=10:

# IF (ESPRESSIONE BOOLEANA)
# IF "Numero compreso tra 1 e 10" or "numero compreso tra 20 e 30"
# IF (1 <= numero and numero <= 10) or (20 <= numero and numero <= 30)

if 1 <= numero and numero <= 10:

    moltiplicatore = 0

    while moltiplicatore <= 10:
        print(f"{numero}x{moltiplicatore}={numero*moltiplicatore}")
        moltiplicatore += 1
else: ## not (1 <= numero and numero <= 10)
    print("Errore")



if numero>10 or numero<1:

    print("Errore")

else: ## not (numero>10 or numero<1)
    while ...


