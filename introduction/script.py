newlines = {"\n": "only \\n", "\r\n": "both \\r and \\n"}
# encs = ["ascii", "utf-7", "utf-8", "utf-16", "cp1250"]
encs = ["utf-8", "utf-16", "cp1252"]

eng_text = "The quick brown fox".split(" ")
ita_text = "Con molto più amore".split(" ")

i=0
for newline in newlines:
	for enc in encs:
		with open(f"eng/{str(i).zfill(2)}.txt", "wb") as fout:
			print(f"eng/{str(i).zfill(2)}.txt", newlines[newline], enc)
			for item in eng_text:
				item_to_print = f"{item}{newline}".encode(enc)
				fout.write(item_to_print)
		i+=1


i=0
for newline in newlines:
	for enc in encs:
		with open(f"ita/{str(i).zfill(2)}.txt", "wb") as fout:
			print(f"ita/{str(i).zfill(2)}.txt", newlines[newline], enc)
			for item in ita_text:
				item_to_print = f"{item}{newline}".encode(enc)
				fout.write(item_to_print)
		i+=1



with open("verylongfile.txt", "w", encoding="utf-8") as fout:
	for i in range(5000000):
		for item in eng_text:
			print(item, file=fout)
