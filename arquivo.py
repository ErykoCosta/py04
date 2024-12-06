import csv

path: str = "arquivo.csv"

lista: list = []

with open(file = path, mode ="r", encoding="utf-8") as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        lista.append(linha)
print(lista)