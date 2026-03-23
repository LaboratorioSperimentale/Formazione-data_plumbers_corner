import sys

file_output_handler = open("output.txt", "w", encoding="utf-8")
files = sys.argv[1:]
for file in files:
    print(f"Sto leggendo dal file: {file}", file=file_output_handler)
    file_handler = open(file, mode = "r", encoding = "utf-8")
    contenuto = file_handler.readlines()

    for line in contenuto:
        n = int(line.strip())
        print(f"Ho letto {n} dal file:", file=file_output_handler)
        i = 1
        while i<=n:
            print(str(i)*i, file=file_output_handler)
            i+=1



