import sys

filename_input = sys.argv[1]
filename_output = sys.argv[2]

frequencies = {}

with open(filename_input, "r", encoding="utf-8") as file_input:
	for line in file_input:
		linesplit = line.strip().split(" ")

		for word in linesplit:
			if not word in frequencies:
				frequencies[word] = 0

			frequencies[word] += 1

with open(filename_output, "w", encoding="utf-8") as file_output:
	for word in frequencies:
		print(f"{word:20}\t{frequencies[word]:5}", file=file_output)