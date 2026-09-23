#tuplas são mais simples, imutáveis

frutas = ("laranja", "pera", "uva",) #ultima virgula pra nao bugar
print (frutas[0])
print (frutas[-1])

letras = tuple("python")

numeros = tuple([1,2,3,4])

pais = ("brasil",)

#tuplas aninhadas

matriz = (
    ("a", 1, 3),
    (2, 3, "b"),
    (5, "c", 6)
)
print(matriz[0][0])
print(matriz[0])

tupla = ("a","n", "g", "e","l","o")
print(tupla [2:])
print(tupla [0:3])

print(tupla.count("g")) #quantas tem
print (tupla.index("a")) #onde ta