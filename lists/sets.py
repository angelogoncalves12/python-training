# sets ou conjuntos
#coleção que não possui objetos repetidos,
#elimina os repetidos

conjunto = set ([1,2,3,4,2,3,4,5,6])
conjunto = set("abacaxi")
conjunto =  {"python", "java", "python"} 
#chaves também faz o set
print (conjunto)

#não suporta indexação como (valor[3]),
#precisa converter pra lista

numeros = {1,2,3,4,2}
numeros = list(numeros)
print(numeros)


#mas ele pode ser percorrido
listas = {1,2,2,2,2,3,4,5}
for lista in listas:
    print (lista)

for indice, lista in enumerate(listas):
    print(f"{indice+1}:{lista}")



#uniao de elementos
conjunto1 = {1,2,3}
conjunto2 = {2,3,4}

print(conjunto1.union(conjunto2))

# da pra unir os que são iguais e apagar os demais
#intersecção

print(conjunto1.intersection(conjunto2))

#tem como tirar a diferença tbm

print(conjunto1.difference(conjunto2)) # oque tem no a que nao tem no b
print(conjunto2.difference(conjunto1)) # oq tem no b q nao tem no a

#diferença simétrica é a diferença completa entre os dois

print(conjunto1.symmetric_difference(conjunto2))

#conjunto logico com subconjunto
conjunto1 = {1,2,3,4}
conjunto2  = {1,3,4,5,2,6,7,8,9}

print(conjunto1.issubset(conjunto2)) # todos elementos de 1 pertencem a 2
#verdadeiro

print(conjunto2.issubset(conjunto1))# todos elementos de 2 pertence a 1
#falso

# e temos o processo contrario

print(conjunto1.issuperset(conjunto2)) #falso

print(conjunto2.issuperset(conjunto1)) #verdadeiro

# também tem a função que nenhum deles pode ter conjunção

conjunto1 = {1,2,3,4,5}
conjunto2 = {6,7,8,9}
conjunto3 = {1,0}

print(conjunto1.isdisjoint(conjunto2))  # diferente - vrdd
print(conjunto1.isdisjoint(conjunto3)) # repete o 1 - falso


# dá pra adicionar um valor na lista também
sorteio = {3,12}

sorteio.add(14)
sorteio.add(20)
sorteio.add(50)
print(sorteio)


sorteio2 = sorteio.copy()

# taticas de remoção 

sorteio.discard(14)
sorteio.discard (40) #nao da erro
print(sorteio)

sorteio.clear()
print(sorteio)

sorteio = {1,2,1,3,6,7,8,9,5,3,1,2,3,4,5}
sorteio.pop() #remove o primeiro da lista
sorteio.pop() #remvoe o segund...


sorteio.remove(5) #discard é mais versatil, pois nao da erro
print(sorteio)
print(len(sorteio))
print (5 in sorteio) #false
print (6 in sorteio) #true
