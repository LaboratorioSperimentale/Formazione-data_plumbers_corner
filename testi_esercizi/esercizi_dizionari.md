# Esercizi su dizionari e file

1. Dato il seguente dizionario:
   ```python
   traduzione = {"gatto": "cat", "cane": "dog", "topo": "mouse", "uccello": "bird"}
   ```
   Scrivi un programma che chiede all'utente di inserire una parola italiana e stampa la traduzione in inglese. Se la parola non è nel dizionario, stampa `Parola non trovata`.

2. Scrivi un programma che legge un file di testo contenente una parola per riga. Il programma memorizza le parole in un dizionario dove la chiave è la parola e il valore è la sua lunghezza. Alla fine stampa il dizionario.

   Esempio: se il file `parole.txt` contiene:
   ```
   anatroccolo
   testo
   grammatica
   ```
   Il programma stampa:
   ```
   {'anatroccolo': 11, 'testo': 5, 'grammatica': 10}
   ```

3. Scrivi un programma `conta_lettere.py` che prende come parametro una parola e conta quante volte compare ciascuna lettera, usando un dizionario. Alla fine stampa il dizionario.

   Esempio:
   ```
   python conta_lettere.py banana
   ```

   ```
   {'b': 1, 'a': 3, 'n': 2}
   ```

4. Scrivi un programma che legge un file di testo contenente una parola per riga e stampa la parola che compare più volte. Se ci sono pareggi, basta stamparne una.

5. Scrivi un programma che legge un file di testo riga per riga e produce un secondo file che contiene solo le righe che contengono la parola `palla` (senza distinzione tra maiuscole e minuscole).

6. Scrivi un programma che legge un file di testo riga per riga e conta quante righe ci sono, quante parole ci sono in totale e quanti caratteri ci sono in totale. Alla fine stampa i tre conteggi.

7. Scrivi un programma che legge un file di testo e scrive su un nuovo file lo stesso testo, ma con tutte le lettere trasformate in minuscolo e le righe vuote rimosse.

8. Scrivi un programma che legge un file di testo e conta la frequenza di ogni parola, usando un dizionario. Alla fine stampa le parole e il loro conteggio, una per riga.

9. Scrivi un programma che legge due file di testo e confronta il vocabolario dei due testi: stampa quante parole distinte compaiono in entrambi i file, quante compaiono solo nel primo e quante solo nel secondo.
