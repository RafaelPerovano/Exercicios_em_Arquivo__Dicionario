import csv
from quest_9 import importar_compras
compras = importar_compras()
with open('compras.csv', 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        for produto, preco in compras.items():
            escritor.writerow([produto, preco])