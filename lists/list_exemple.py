frutas = ["maçã", "banana", "uva"]
print(frutas)
print(frutas[0])
print(frutas[-1])

frutas = []
print (frutas)

letras = list("python")
print (letras)

numeros = list(range(10))
print (numeros)

carro = ["Ferrari", "V8", 42000000, 2023, 2900, "Aracaju", True]
print (carro)

#listas aninhadas 

matriz = [
    ["a", 1, 3],
    [2, 3, "b"],
    [5, "c", 6]
]
print(matriz[0][0])




# fatiamento 
##start, stop, step

lista = ["c","l","a","n","g","s"]

print(lista[2:])
print(lista[:2])
print(lista [::])
print(lista[2:5])




#citar listas
carros = ["gol", "palio", "kwid"];

for carro in carros:
    print(carro)

##enumerate
for indice, carro in enumerate(carros):
    print(f"{indice+1}: {carro}")


#filtragem

numeros = [1,23,24,38,39,47,58,70]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

pares.append(2)
pares.append("fim da lista")
print (pares)

pares.clear()
print (pares)

