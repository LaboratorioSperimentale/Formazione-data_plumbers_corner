# Regular expressions

1. come matchare caratteri singoli, anche "speciali" (es. `.` per qualsiasi carattere, `\t` per la tabulazione, `\n` per il ritorno a capo)
2. i moltiplicatori che si applicano **sempre** al carattere che li precede (`*` per indicare una ripetizione da 0 a n volte, `+` per 1 o più volte, `?` per 0 oppure 1 volta, `{x}`, `{x, y}`, `{x,}`. `{,y}` per indicare esattamente x, tra x e y, almeno x, al più y volte rispettivamente)
3. alcune sequenze speciali che ci permettono di individuare un carattere di un insieme definito dall'interprete (`\s` per tutti gli spazi, `\w` per gli alfanumerici, `\d` per le cifre...)
4. le ancore, per indicare che la nostra espressione deve rispettare delle condizioni sulla sua occorrenza (`^` all'inizio della riga, `$` alla fine della riga, `\b` al confine di token)
5. come definire un insieme di caratteri custom, ovvero utilizzando le parentesi quadre `[]` con all'interno i caratteri che vogliamo facciano parte del nostro gruppo (es. `[aeiou]` per definire il gruppo delle vocali italiane non accentate)
6. che le parentesi quadre supportano anche le operazioni di range (es. `[a-z]` tutti i caratteri tra la a e la z, ma `[a-f]` tutti i caratteri tra la a e la f)
7. come creare un insieme per negazione, tramite l'uso di `^` dentro le parentesi quadre (es. `[^ab0]` quasiasi carattere ad eccezione di a, b e 0)
8. che gli interpreti più diffusi per i linguaggi regolari ci permettono in realtà anche di esprimere delle espressioni che proprio regolari non sono, e "memorizzare" una sequenza per poi cercarla in un punto successivo della stringa. Queste sottosequenze memorizzate prendono il nome di **gruppi** (es. `([bdmns]a)\1` per matchare un qualsiasi carattere tra b, d, m, n, s, seguito da a, e poi di nuovo la stessa coppia di caratteri. Quindi matcha `baba`, `nana`, `mama`, ma non `bana` per esempio)
