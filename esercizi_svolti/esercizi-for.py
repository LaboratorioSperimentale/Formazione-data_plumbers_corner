# parola = input("Inserisci una parola: ")

# for lettera in parola:
#     print(lettera)

# i = 0
# while i<len(parola):
#     lettera = parola[i]
#     print(lettera)
#     i += 1

# parola = input("Inserisci una parola: ")

# posizione = 0
# for carattere in parola:
#     print(carattere, posizione)
#     posizione += 1

# for posizione, carattere in enumerate(parola):
#     posizione += 1
#     print(carattere, posizione)

# # NO PERCHè povero index
# for carattere in parola:
# 	posizione = parola.index(carattere) + 1


# numero = input("Inserisci un numero: ")

# # posizione = 0
# tabella = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in tabella:
# 	print(int(numero)*i)
# 	# posizione += 1

# numero = input("Inserisci un numero: ")
# lista = []

# lista.append(int(numero))

# tabella = 0
# for numero in lista:
#     print(int(numero)*int(tabella))
#     tabella += 1
#     print(int(numero)*int(tabella))
#     tabella += 1
#     print(int(numero)*int(tabella))
#     tabella += 1
#     print(int(numero)*int(tabella))
#     tabella += 1


# numero = int(input("inserisci un numero: "))

# for moltiplicatore in range(10):
# 	moltiplicatore += 1
# 	print(f"{numero}x{moltiplicatore} = {numero*(moltiplicatore)}")
	# moltiplicatore += 1 # NON SERVE

# numero = int(input("inserisci un numero: "))
# moltiplicatori = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for moltiplicatore in moltiplicatori:
#     print(moltiplicatore)
	# print(f"{numero}x{moltiplicatore} = {numero*moltiplicatore}")

# numero = input("Inserisci un numero: ")
# # # variabile = 1


# for i in range(1, int(numero)+1):
# 	stringa_da_costruire = ''
# 	for j in range(i):
# 		# stringa_da_costruire += "*"
# 		stringa_da_costruire = stringa_da_costruire + "*"

# 	print(stringa_da_costruire)

# numero = input("Inserisci un numero: ")
# stringa = "*"
# for i in range(1, int(numero)+1):
#     print(stringa)
#     stringa = stringa+"*"


lista = []
for i in range(0, 5):
    parola = input("Inserisci una parola: ")
    lista.append(parola)

# else:
if lista[0] == lista[-1]:
	print("Lista corretta")
else:
	print("Lista scorretta")