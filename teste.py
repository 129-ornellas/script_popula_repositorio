import csv

arquivo_csv = 'customizados_rede_inspira.csv'
with open(arquivo_csv, "r", encoding="utf8") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    count = 0
    for i,linha in enumerate(arquivo_csv):
       if i == 0:
            continue
       count +=1
       print(f"{linha[0]} > {linha[1]}")
    print(count)