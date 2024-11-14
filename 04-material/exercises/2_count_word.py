with open("../02-materials/alice.txt", "r", encoding="utf-8") as f:
    alice = f.read()

characters = len(alice)
print(f"number of characters: {characters}")

words = alice.split()

word_counter = 0
for word in words:
    if any(char.isalpha() for char in word):
        word_counter += 1

print(f"number of word: {word_counter}")
