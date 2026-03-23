eta = input("Inserisci la tua età: ")
eta_da_raggiungere = input("Che età vuoi raggiungere? ")
distanza = int(eta_da_raggiungere) - int(eta)

soglia = 5

condizione1 = int(eta)<soglia
condizione2 = int(eta_da_raggiungere)<=soglia

if condizione1 and condizione2:
    print("Impossibile!")
elif condizione1 or condizione2:
    print("")


# se eta<0 and eta_da_raggiungere<=0, allora print("Impossibile!")
# altrimenti se eta<0 and eta_da_raggiungere>=0, allora print("Non puoi avere età negativa!")
# altrimenti se eta>=0 and eta_da_raggiungere<0, allora print("Non sei Benjamin Button")
# altrimenti, allora esegui stampa_messaggio_giusto()





# IF A:
#	fai questo
# ELIF B:
#	fai quello
# ELIF C:
#	fai altro
#...
# ELSE:
# 	vai al mare

# IF A:
#	fai questo
# ELSE:
# 	IF B:
#		fai quello
# 	ELSE:
# 		IF C:
#			fai altro
#...
# ELSE:
# 	vai al mare