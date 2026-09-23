import requests
import json

url = "https://api.agify.io/?name=angelo"

resposta = requests.get(url)

dados = resposta.json() #conversão de formato
# print (resposta.status_code)
# print (resposta.text)

print("Nome: ", dados["name"])
print("Idade Estimada: ", dados["age"])
print("Número de Registros: ", dados["count"])

#transformar em arquivo

with open("data.json", "w") as arq:
    json.dump(dados,arq)
