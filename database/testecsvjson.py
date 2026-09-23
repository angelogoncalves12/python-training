import csv 
import csv

dados = [
    ["nome", "idade", "cidade"],
    ["Angelo","18", "São Cristóvão"],
    ["Matteo","19", "Aracaju"],
    ["Angelica", "89", "Ns. Senhora do Socorro"],
]

with open("pessoas.csv", "w", newline ="") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerows(dados)

with open("pessoas.csv", "r") as arquivo:
    reader = csv.reader(arquivo)

    for linha in reader:
        print(linha)

import json

data = {
    "nome": "Angelica",
    "idade": "89",
    "cidade": "Lagarto",
}

with open ("usuario.json", "w") as arq:
    json.dump(data, arq) #dados,arquivos que estão os dados


with open ("usuario.json", "r") as arq:
    data = json.load(arq)
    print (data)  #dados,arquivos que estão os dados
    