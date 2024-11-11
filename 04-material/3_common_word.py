from collections import Counter

with open("../02-materials/alice.txt") as f:
    alice = f.read()

words = alice.split()

counter = Counter()
for word in words:
    if word.isalpha():
        counter[word] += 1

for word, count in counter.most_common(10):
    print(f"{word:15} {count}")
