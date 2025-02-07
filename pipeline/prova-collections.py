import sys
import collections

filename_input = sys.argv[1]

frequencies = collections.defaultdict(int)

with open(filename_input, "r", encoding="utf-8") as file_input:
	for line in file_input:
		linesplit = line.strip().split(" ")

		for word in linesplit:
			# if not word in frequencies:
			# 	frequencies[word] = 0

			frequencies[word] += 1