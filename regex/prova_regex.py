import re

# palla -> pal:a
# mamma -> mam:a

file = open("corpus/source/first_chapter.txt")
testo = file.read()

nuovo_testo = re.sub(r"\n", " ", testo)

file_output = open("corpus/source/first_chapter_nuovo.txt", "w")
print(nuovo_testo, file=file_output)