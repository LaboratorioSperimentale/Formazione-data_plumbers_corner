curl https://raw.githubusercontent.com/LaboratorioSperimentale/Formazione-data_plumbers_corner/refs/heads/main/02-materials/alice.txt > alice.txt
cat alice.txt | tr " " "\n" | sort | uniq -c | sort -nr | head -n10
