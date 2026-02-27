# Scrivi un programma che chiede in input un intero e stampa le potenze di quel numero finchè il valore non eccede 1000.
# Ad esempio, se viene inserito il numero `2`, il programma in output deve stampare:
# 	```
# 	2^1 = 2
# 	2^2 = 4
# 	2^3 = 8
# 	2^4 = 16
# 	2^5 = 32
# 	2^6 = 64
# 	2^7 = 128
# 	2^8 = 256
# 	2^9 = 512
# 	```

numero = int(input("Inserisci un numero: "))

esponente = 1
potenza = numero**esponente

while potenza < 1000:

    print(f"{numero}^{esponente}={potenza:>3}")

    esponente += 1
    potenza = numero**esponente