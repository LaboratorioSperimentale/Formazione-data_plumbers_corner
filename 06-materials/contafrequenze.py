import sys
import pathlib

import collections

frequencies = collections.defaultdict(int)

path = pathlib.Path(sys.argv[1])
if not path.is_dir():
	print(f"{path} is not a folder", file=sys.stderr)
	sys.exit(1)

for file in path.rglob("*.txt"):
	with open(file, encoding="utf-8") as fin:
		print(f"Reading {file} ...", file=sys.stderr)
		for lineno, line in enumerate(fin):
			if not lineno % 100:
				print(f"  Reading line {lineno} ...", file=sys.stderr)

			linesplit = line.strip().split()
			for word in linesplit:
				if all(c.isalpha() for c in word):
					frequencies[word] +=1

for key, value in sorted(frequencies.items(), key=lambda x: -x[1]):
	print(f"{key}\t{value}")
