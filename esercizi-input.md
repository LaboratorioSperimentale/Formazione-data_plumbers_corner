Abbiamo visto un primo modo per leggere l'input da un file invece che da prompt. Per esempio, consideriamo il caso di un programma che deve leggere da una fonte di input dei numeri finchè non incontra lo zero e poi stampare la lista di numeri trovati:

```python
lista_numeri = []

number = int(input())
while number != 0:
	lista_numeri.append(number)
	number = int(input())

print("Numeri letti:", lista_numeri)
```

Questo programma produrrà `Numeri letti: [4, 3]` in output sul terminale nel caso dei due file [`input_1.txt`](input_streams/input_1.txt) e [`input_2.txt`](input_streams/input_2.txt) usati come input.

```sh
$ python3 script.py < input_1.txt
Numeri letti: [4, 3]
```

```sh
$ python3 script.py < input_2.txt
Numeri letti: [4, 3]
```

Nei seguenti esercizi provare, dove possibile, a usare un file di input invece che l'input interattivo.

1. Scrivi un programma che legge una serie di numeri finchè non incontra `0`. Per ogni numero `n` letto il programma stampa tutti i numeri pari compresi tra `0` (incluso) e `n` (escluso).
Esempio:

	Input:
	```
	6
	10
	0
	```

	Output:
	```
	0
	2
	4
	0
	2
	4
	6
	8
	```

2. Scrivi un programma che legge una stringa e controlla se è palindroma. Es. `I topi non avevano nipoti` è considerata una stringa palindroma

3. Scrivi un programma che legge una sequenza di stringhe, finchè non incontra la parola `fine`. Il programma conta il numero di parole che iniziano per ogni vocale (`a`, `e`, `i`, `o`, `u`).

3. Scrivi un programma che legge una sequenza di stringhe, finchè non incontra la parola `fine`. Il programma conta il numero di parole che iniziano per ogni vocale (`a`, `e`, `i`, `o`, `u`).

4. Scrivi un programma che legge `5` lettere, e poi una sequenza di stringhe finchè non incontra la parola `fine`. Il programma conta il numero di parole che iniziano per ogni lettera letta.

5. Scrivi un programma che legge tre serie di numeri. Ogni serie è definita dal fatto che finisce con `0`. Per ogni serie letta, il programma stampa tutti i numeri letti al contrario.

	Input:
	```
	4
	12
	0
	9
	7
	6
	0
	4
	1
	-3
	8
	0
	```

	Output:
	```
	[12, 4]
	[6, 7, 9]
	[8, -3, 1, 4]
	```

6. Scrivi un programma che legge una serie di numeri dispari terminata da `0`. Per ogni numero `n` della serie il programma stampa un rombo di asterischi come negli esempi seguenti:

	```
	# n = 3
	  *
	 ***
	  *
	```

	```
	# n = 7
	   *
	  ***
	 *****
	*******
     *****
	  ***
	   *
	```