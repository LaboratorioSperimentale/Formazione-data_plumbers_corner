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


