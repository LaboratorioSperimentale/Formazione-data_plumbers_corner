with open("../02-materials/alice.txt") as f:
    alice = f.read()

# TODO: check it accounts for utf-8
characters = len(alice)
print(f"number of characters: {characters}")

words = alice.split()

word_counter = 0
for word in words:
    if not word.isalpha():
        word_counter += 1

print(f"number of word: {word_counter}")
