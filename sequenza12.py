
numero = int(input("Inserisci un numero: "))
condizione = True
prec_num = 0

while numero != 0 and condizione:


    if condizione and (prec_num == 1 and numero != 2):
        condizione = False

    prec_num = numero

    numero = int(input("Inserisci un numero: "))

if condizione:
    print("Sequenza corretta!")
else:
    print("Sequenza errata!")



## ESERCIZIO:
## leggere una stringa dall'input e controllare se è palindroma

# if [ESPRESSIONE BOOLEANA]:
#	istr-x
# else:
#	istr-y
#

# if 3 == numero_trovato:
#	istr-x
# else:
#	istr-y
#

# >(int, int) -> BOOL
# >(str, str) -> BOOL