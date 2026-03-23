# stringa = "I topi, non avevano ni'poti."
# print(" ".join(stringa.lower().split("'")))

# print("---------")
# parole_punct = " ".join(stringa.lower().split("'")).split()

# parole_senza_punteggiatura = []

# for x in parole_punct:
#     y = x.strip(".,?!")
#     parole_senza_punteggiatura.append(y)

# stringa_adattata = "".join(parole_senza_punteggiatura)

# print(stringa_adattata)

stringa = "I topi, non avevano ni'poti."
print(stringa)

stringa1 = stringa.lower()
stringa_senza_spazi = ""
caratteri = [".", ",", "?", "!", " ", "'", "`"]

i = 0
while i < len(stringa1):
    if stringa1[i] not in caratteri:
        stringa_senza_spazi = stringa_senza_spazi + stringa1[i]
    i += 1

print(stringa_senza_spazi)

# # print(stringa_adattata)

# condizione = True
# for i in range(len(stringa_adattata)//2):
#     if stringa_adattata[i] != stringa_adattata[-1-i]:
#         condizione = False

# print(condizione)