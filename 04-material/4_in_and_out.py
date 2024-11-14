from collections import Counter
from sys import argv

in_path = argv[1]
out_path = argv[2]

with open(in_path) as f:
    alice = f.read()

words = alice.split()

counter = Counter()
for word in words:
    if word.isalpha():
        counter[word] += 1

with open(out_path, "w") as f:
    f.write("word,count\n")
    for word, count in counter.most_common():
        f.write(f"{word},{count}\n")
