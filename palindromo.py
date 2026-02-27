## ESERCIZIO:
## leggere una stringa dall'input e controllare se è palindroma

# CASI
# anna - True
# onorarono - True
# macchina - False
# olmo - False
# olivo - False
# i topi non avevano nipoti
# angolo bar a bologna
# do geese see god


parola = input("Inserisci una parola: ")

condizione = True

# pos_i = 0
# pos_f = -1

for i in range(len(parola)//2):
	if parola[i] != parola[-1-i]:
		condizione = False
	# pos_i += 1
	# pos_f -= 1


# n = 0
# while n < len(parola)/2:
#     if parola[n] != parola[-1-n]:
#         condizione = False

#     n += 1

print(condizione)

