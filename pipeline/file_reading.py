nome_file = input("Inserisci nome file:")

file_handler = open(nome_file, "r", encoding="utf-8")

for line in file_handler:
	print("NUOVA RIGA")
	print(line.strip())


print("-------")

print("2+5\tciao")

word = "alice"
frequency = 145
print(f"{word:30}\t{frequency}")
word = "alicenelpaesedellemeraviglie"
frequency = 1
print(f"{word:30}\t{frequency}")

x = 0.000006572645477987

print(f"{x:.3f}")