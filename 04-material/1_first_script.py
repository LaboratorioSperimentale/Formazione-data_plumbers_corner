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


map = {}
for word in words:
    if word[0] not in map:
        map[word[0]] = []

    map[word[0]].append(word)


print("----------------------------------")

for key, value in map.items():
    print(f"Le parole che iniziano con '{key}' sono: {value}")
