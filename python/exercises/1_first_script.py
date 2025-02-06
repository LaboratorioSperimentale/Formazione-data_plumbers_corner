words = [
    "mela",
    "banana",
    "ciliegia",
    "dattero",
    "fico",
    "uva",
    "limone",
    "mandarino",
    "noce",
    "castagna",
    "fragola",
]

for word in words:
    chars = len(word)
    print(f"La parola '{word}' ha {chars} caratteri.")


print("----------------------------------")

for word in words:
    chars = len(word)
    if chars > 5:
        print(f"La parola '{word}' ha più di 5 caratteri.")


alpha_map = {}
for word in words:
    if word[0] not in alpha_map:
        alpha_map[word[0]] = []

    alpha_map[word[0]].append(word)


print("----------------------------------")

for key, value in alpha_map.items():
    print(f"Le parole che iniziano con '{key}' sono: {value}")
