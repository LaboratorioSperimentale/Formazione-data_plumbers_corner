lista_di_parole = []

parola = input("Inserisci una parola: ")
lista_di_parole.append(parola)

while parola != "fine":
	parola = input("Inserisci una parola: ")
	lista_di_parole.append(parola)
	### SINTASSI APPEND
	### [nome_di_variabile_tipoLista].append(ESPRESSIONE)


# lista_di_parole.append(parola)
print(", ".join(lista_di_parole))

### SINTASSI JOIN
### ESPRESSIONE_TIPO_STRINGA.join(ESPRESSIONE_TIPO_LISTA)
### SEMANTICA
### restituisce gli elementi della lista intervallati dalla stringa

### SINTASSI FOR
### for [NOME_VARIABILE] in [INSIEME--LISTA]:
###		istruzione-1
###		istruzione-2

>>> personaggi
['topolino', 'minnie', 'paperino', 'paperina']
>>> posizione = 0
>>> while posizione<len(personaggi):
...     print(f"Il personaggio è {personaggi[posizione]}")
...     posizione += 1
...
Il personaggio è topolino
Il personaggio è minnie
Il personaggio è paperino
Il personaggio è paperina
>>> for elemento in personaggi:
...     print(f"Il personaggio è {elemento}")
...
Il personaggio è topolino
Il personaggio è minnie
Il personaggio è paperino
Il personaggio è paperina