from collections import Counter

with open("../02-materials/alice.txt", "r", encoding="utf-8") as f:
    alice = f.read()

words = alice.split()

counter = Counter()
for word in words:
    if any(char.isalpha() for char in word):
        counter[word] += 1

for word, count in counter.most_common(10):
    print(f"{word:15} {count}")
