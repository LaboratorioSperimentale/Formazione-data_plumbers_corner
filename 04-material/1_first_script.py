words = ["mela", "banana", "ciliegia", "dattero", "fico", "uva"]

for word in words:
    chars = len(word)
    print(f"La parola '{word}' ha {chars} caratteri.")


print("----------------------------------")

for word in words:
    chars = len(word)
    if chars > 5:
        print(f"La parola '{word}' ha più di 5 caratteri.")
