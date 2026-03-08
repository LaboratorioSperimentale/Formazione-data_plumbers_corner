1. scrivi un programma che effettua la stessa operazione della funzione `strip`.
   Il programma legge dall'input una stringa seguita da una sequenza di caratteri da rimuovere, ognuno su una riga diversa. La sequenza termina quando viene letta una riga vuota. Il programma deve rimuovere dall'inizio e dalla fine della stringa tutti i caratteri appartenenti alla sequenza letta. Infine stampa la stringa risultante (IMPORTANTE: senza usare la funzione `strip` ovviamente!).

   Ad esempio, dato l'input:
   ```
	..hello world!!
	.
	!


   ```
   Il programma deve restituire `hello world`

   Un altro esempio. Dato l'input:
   ```
     pic-nic -
	<spazio>
	.
	,
	-


   ```
   (la seconda riga contiene un carattere "spazio")
   Il programma deve restituire `pic-nic` (lo spazio iniziale viene rimosso, il `-` finale viene rimosso, il `-` dentro "pic-nic" rimane).

2. scrivi un programma che effettua la stessa operazione della funzione `join`.
   Il programma legge dall'input una stringa seguita da una sequenza di parole, una per riga. La sequenza termina quando viene letta la stringa `fine`. Il programma deve restituire una stringa composta da tutte le parole lette intervallate dalla stringa letta (IMPORTANTE: senza usare la funzione `join` ovviamente!).
   Ad esempio, dato l'input:
   ```
	,<spazio>
	pane
	formaggio
	salame
	fine

	```
	Il programma produce in output: "pane, formaggio, salame"

3. Scrivi un programma che legge due numeri dall'input (base, altezza) e stampa un rettangolo vuoto dentro di dimensioni base x altezza
   Ad esempio se legge i numeri:
   ```
   4
   6

   ```
	Produce in output
   ```
   ******
   *    *
   *    *
   ******
   ```

4. Scrivi un programma che legge tre numeri dall'input (k, base, altezza) e stampa k rettangoli vuoti dentro di dimensioni base x altezza.
   Ad esempio se legge i numeri:
   ```
   3
   4
   6

   ```
	Produce in output
   ```
   ****** ****** ******
   *    * *    * *    *
   *    * *    * *    *
   ****** ****** ******
   ```

5. Scrivi un programma che legge dall'input un numero e stampa una piramide come nell'esempio seguente:
   Input:
   ```
   5
   ```
   Output:
   ```
	1
	22
	333
	4444
	55555
   ```

5. Scrivi un programma che legge dall'input un numero e stampa una piramide come nell'esempio seguente:
   Input:
   ```
   5
   ```
   Output:
   ```
	1
	12
	123
	1234
	12345
   ```