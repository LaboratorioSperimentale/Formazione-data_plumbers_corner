1. Scrivi un programma che stampi i numeri da 1 a 10.

2. Scrivi un programma che legge un numero `n` dall'input e stampa i numeri da `n` a `0`.

3. Scrivi un programma che legge un numero `n` dall'input e stampa i numeri da `-n` a `n`.

4. Dato un certo numero (es. `pagine = 120`), stampa:
	```
	Sto leggendo la pagina 1
	Sto leggendo la pagina 2
	...
	```
	fino all’ultima pagina.

5. Scrivi un programma che chiede all'utente di inserire una parola.
Il programma continua finché l’utente non scrive `fine`.

	```
	Inserisci una parola: storia
	Inserisci una parola: linguistica
	Inserisci una parola: fine
	```

6. Chiedi all'utente di inserire una stringa e calcola quante vocali ci sono nella stringa.

7. Scrivi un programma che chiede all'utente di inserire un numero. Il programma si ferma quando l'utente inserisce `0` e conta quanti numeri interi sono stati inseriti.

8. Scrivi un programma che chiede all'utente di inserire un numero. Il programma si ferma quando l'utente inserisce `0` e, per ogni numero inserito, se il numero è pari stampa `Hai inserito un numero pari!` altrimenti stampa `Hai inserito un numero dispari!`.

9. Scrivi un programma che chiede all'utente di inserire una parola. Il programma si ferma quando l'utente inserisce la parola `fine`. Per ogni parola inserita, se la parola è più lunga di 5 caratteri stampa `parola lunga` altrimenti stampa `parola breve`.

10.  Scrivi un programma che dati due numeri (es. `pagine = 3` e `righe = 5`), stampa tutte le combinazioni di pagine e righe
	```
	Pagina 1 Riga 1
	Pagina 1 Riga 2
	Pagina 1 Riga 3
	Pagina 1 Riga 4
	Pagina 1 Riga 5
	Pagina 2 Riga 1
	...
	Pagina 3 Riga 4
	Pagina 3 Riga 5
	```

11.  Data una stringa letta dall'input (es. `adoro programmare in Python!`) scrivere un programma che stampa la frequenza di ogni lettera all'interno della stringa (non importa se alcune lettere vengono conteggiate più volte!)

12. Scrivere un programma che fa giocare l'utente al gioco dell'impiccato.
    - Nel gioco dell’impiccato, un giocatore (A) pensa a una parola e la mantiene segreta. L’altro giocatore (B) deve cercare di indovinarla proponendo una lettera alla volta. Se il giocatore B sceglie una lettera che è effettivamente presente nella parola segreta, tutte le posizioni in cui essa compare vengono svelate, aggiornando lo stato corrente del gioco.
    - per giocare all'impiccato sono necessari dei due file `parola_segreta.py` e `impiccato.py` che si trovano nella cartella [`impiccato/`](./impiccato/)
    - è importante salvare entrambi i file nella stessa cartella sul proprio computer
    - il file `parola_segreta.py` contiene le seguenti righe, potete cambiare il valore della variabile `PAROLA_SEGRETA` per giocare altre partite.

    ```python
    PAROLA_SEGRETA = "Natale"
    GUESS = "_"*len(PAROLA_SEGRETA)
    ```

    - il file `impiccato.py` contiene:
      - la variabile `PAROLA_SEGRETA` importata da `parola_segreta.py`
      - la variabile `GUESS`, importata da `parola_segreta.py`. All'inizio del gioco `GUESS` è una stringa formata da un numero di underscore pari alla lunghezza di `PAROLA_SEGRETA`
      - una funzione `update`, che data una stringa tipo `GUESS`, una stringa contenente una parola e una stringa contenente una lettera, restituisce una stringa `GUESS` aggiornata in base alla lettera proposta.
        - es. `update("____", "casa", "a") > "_a_a"`
        - `update("_a_a", "casa", "b") > "_a_a"`
        - `update("_a_a", "casa", "c") > "ca_a"`

13. Come rendere l'impiccato più divertente?
    - aggiungere un numero massimo di tentativi! Nella versione classica del gioco i tentativi sono 6
    - aggiungere un numero di tentativi che dipende dalla lunghezza della parola segreta
    - aggiungere la possibilità, per il giocatore B, di provare ad indovinare la parola segreta ad ogni turno