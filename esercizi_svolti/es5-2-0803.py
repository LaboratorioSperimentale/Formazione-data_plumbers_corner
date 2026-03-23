n = 5

# ciclo su n righe 1... n
for i in range(1, n+1):
	stringa_da_stampare = ''
	# costruisco la stringa
	for j in (1, i+1):
		stringa_da_stampare += str(j)

	print(stringa_da_stampare)


