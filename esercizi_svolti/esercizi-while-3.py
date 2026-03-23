# lista_numeri = []

# numero = int(input("Scrivi un numero: "))

# while numero != 0:
# 	lista_numeri.append(numero)
# 	numero = int(input("Scrivi un numero: "))

# if 1 not in lista_numeri:
#     print("Sequenza errata")
# elif lista_numeri[lista_numeri.index(1)+1] == 2:
#     print("Sequenza corretta")
# else:
#     print("Sequenza errata")

# 9, 1, 6, 1, 2, 0
# 9, 1, 2, 1, 6, 0


# numeri = []
# numero = int(input("Inserisci un numero: "))

# contatore_posizioni = 0
# if numero == 1:
# 	posizione_uno = contatore_posizioni
# elif numero == 2:
# 	posizione_due = contatore_posizioni

# while numero != 0:
# 	numeri.append(numero)
# 	numero = int(input("Inserisci un numero: "))
# 	contatore_posizioni +=1
# 	if numero == 1:
# 		posizione_uno = contatore_posizioni
# 	elif numero == 2:
# 		posizione_due = contatore_posizioni

# if 1 in numeri and 2 in numeri:
# 	if posizione_due == posizione_uno+1:
# 		print("Sequenza corretta")
# 	else:
# 		print("Sequenza errata")
# else:
#     print("Sequenza errata")

# 1, 3, 4, 1, 2


# numeri = []
# numero = int(input("Inserisci un numero: "))

# while numero != 0:
# 	numeri.append(numero)
# 	numero = int(input("Inserisci un numero: "))
# print(numeri)
# # 1, 2, 3, 4, 1, 2, 1
# # ^ ^^
# lista_flag = []
# pos = 0
# while pos < len(numeri)-1:
# 	if numeri[pos] == 1:
# 		if numeri[pos+1] == 2:
# 			lista_flag.append(True)
# 		else:
# 			lista_flag.append(False)
# 	pos += 1

# if numeri[pos] == 1:
#     lista_flag.append(False)

# print(lista_flag)

# if False in lista_flag:
#     print("Sequenza errata")
# else:
#     print("Sequenza corretta")


# numeri = []
# numero = int(input("Inserisci un numero: "))

# while numero != 0:
# 	numeri.append(numero)
# 	numero = int(input("Inserisci un numero: "))
# print(numeri)

# condizione = True
# pos = 0
# while pos < len(numeri)-1:
# 	if numeri[pos] == 1:
# 		if numeri[pos+1] != 2:
# 			condizione = False
# 	pos += 1

# if numeri[pos] == 1:
#     condizione = False

# if condizione:
#     print("Sequenza corretta")
# else:
#     print("Sequenza errata")


# numeri = []
# numero = int(input("Inserisci un numero: "))

# while numero != 0:
# 	numeri.append(numero)
# 	numero = int(input("Inserisci un numero: "))
# print(numeri)

# condizione = True
# pos = 0
# while pos < len(numeri)-1:
# 	if numeri[pos] == 1:
# 		if numeri[pos+1] == 2:
# 			condizione  = condizione and True
# 		else:
# 			condizione  = condizione and False
# 	pos += 1

# if numeri[pos] == 1:
#     condizione = condizione and False

# if condizione:
#     print("Sequenza corretta")
# else:
#     print("Sequenza errata")


# numero = int(input("Inserisci un numero: "))
# condizione = True
# trovato_uno = False
# numero_pred = 0

# while numero != 0:

# 	if numero_pred == 1:
# 		if numero != 2:
# 			condizione = False

# 	if numero == 1:
# 		trovato_uno = True

# 	numero_pred = numero
# 	numero = int(input("Inserisci un numero: "))

# if numero_pred == 1:
#     condizione = False

# print(condizione and trovato_uno)

numero = int(input("Inserisci un numero: "))
massimo = -1

while numero != 0:

	if numero > massimo:
		massimo = numero
	numero = int(input("Inserisci un numero: "))

print(massimo)