
# while True:
#     parola = input("Metti una parola: ")
#     if parola == "fine":
#         print("fine")
#         break
#     else:
#         print("non hai indovinato")


# parola = input("Scrivi una parola: ")

# while parola != "fine":
#     print(parola)
#     # parola = input("Scrivi una parola: ")

# print("Il programma si è fermato")

parola = input("Scrivi una parola: ")

while parola.lower().strip() != "fine":
    print(parola)
    parola = input("Scrivi una parola: ")

print("Il programma si è fermato")

# https://docs.python.org/3/library/stdtypes.html#str.strip