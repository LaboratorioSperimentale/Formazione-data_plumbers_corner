import sys

in_path = sys.argv[1]
out_path = sys.argv[2]

word_counter = {}
with open(in_path, "r", encoding="utf-8") as f:
    for line in f:
        words = line.split()
        for word in words:
            if any(char.isalpha() for char in word):
                word_counter[word] += 1

with open(out_path, "w", encoding="utf-8") as f:
    f.write("word,count\n")
    for word, count in word_counter.items():
        f.write(f"{word},{count}\n")
