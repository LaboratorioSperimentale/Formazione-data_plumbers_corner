# Scrivi un programma che legge una serie di numeri dispari terminata da `0`. Per ogni numero `n` della serie il programma stampa un rombo di asterischi come negli esempi seguenti

# numero = int(input())
# lista_numeri = []

# while numero != 0:
# 	lista_numeri.append(numero)
# 	numero = int(input())

# n=1
# for numero in lista_numeri:
# 	for n in range(1, numero, 2):
# 		# print(("*"*n).center(max(lista_numeri)+1))
# 		print(("*"*n).center(numero))

# 	for n in range(numero, 0, -2):
# 		print(("*"*n).center(numero))

# 		# print(("*"*n).center(max(lista_numeri)+1))


# while numero != 0:
#     i = 0

#     while i <= numero //2:
#         j = 2*i
#         k = (numero - j)//2
#         spazi = " "*k
#         asterischi = "*"*(j+1)

#         print(spazi+asterischi)
#         i += 1

#     i = numero//2 - 1

#     while i >= 0:
#         j = 2*i
#         k = (numero - j)//2
#         spazi = " "*k
#         asterischi = "*"*(j+1)

#         print(spazi+asterischi)
#         i -= 1

#     numero = int(input())

numero = int(input())
while numero != 0:
	# print("NUMERO LETTO:", numero)
	posizione_centrale = numero // 2
	# print("POSIZIONE CENTRALE:", posizione_centrale)
	# STAMPA TRIANGOLO SUPERIORE

	for numero_riga in range(1, numero, 2):

		stringa_da_stampare = ''
		for i in range(posizione_centrale):
			stringa_da_stampare += " "

		stringa_da_stampare += "*"*numero_riga
		print(stringa_da_stampare)
		posizione_centrale -=1

	# STAMPA RIGA
	print("*"*numero)

	posizione_centrale += 1
	# STAMPA TRIANGOLO INFERIORE

	for numero_riga in range(numero-2, 0, -2):
		stringa_da_stampare = ''
		for i in range(posizione_centrale):
			stringa_da_stampare += " "
		stringa_da_stampare += "*"*numero_riga
		print(stringa_da_stampare)
		posizione_centrale +=1

	numero = int(input())