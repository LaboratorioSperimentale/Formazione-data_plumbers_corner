import csv


fin = open("0803-input2.tsv", "r", encoding="utf-8")

file_content = csv.DictReader(fin, delimiter="\t")

for line in file_content:
    # print(line)

    lista_stringhe = line["stringhe"].split()
    print(line["joinatore"].join(lista_stringhe))




























# dict_join = {
#     "joinatore": "",
#     "lista_stringhe": []
# }

# fin = open("0803-input.txt", "r", encoding="utf-8")
# lines = fin.readlines()

# dict_join["joinatore"] = lines[0].strip("\n")

# for line in lines[1:]:
#     dict_join["lista_stringhe"].append(line.strip("\n"))



# print(dict_join["joinatore"].join(dict_join["lista_stringhe"]))


# joinatore = input()

# cibi = []

# cibo = input()

# while cibo != "fine":
#     cibi.append(cibo)
#     cibo = input()

# stampa = cibo[0]
# for i in cibi[1:]:
#     stampa = joinatore + i

# # stampa = stampa + cibi[-1]

# print(stampa)
# # print(stampa[0:-len(joinatore)])

# ## [pane][, ][formaggio][, ][salame]
# ## (    )(                         )