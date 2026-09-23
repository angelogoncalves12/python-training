lista = []

lista.append(2)
lista.append("Clangs")
lista.append([10,20,30])

print (lista)

lista.clear()
print (lista)

lista = [1,2,3]

lista2 = lista.copy()
print (id(lista2), id(lista)) #elas sao diferentes
lista2[0] = 2

print(lista2)
print(lista)


favorite_languages = ["javascript", "java", "python"]
print (favorite_languages)

favorite_languages.extend(["C", "Kotlin"])
print (favorite_languages)
print (favorite_languages.index("C"))
print (favorite_languages.index("javascript"))

print(favorite_languages.pop()) #funciona como uma pilha de pratos, 
# vai imprimindo de tras pra frente e VAI REMOVENDO!!!
print(favorite_languages.pop()) 
print(favorite_languages.pop()) 
print(favorite_languages.pop()) 
print(favorite_languages.pop()) 

favorite_languages = ["javascript", "java", "python", "c", "kotlin"]
favorite_languages.remove("kotlin")
print (favorite_languages)

favorite_languages.reverse()
print(favorite_languages)

favorite_languages.sort() #organiza em ordem alfabetica
print (favorite_languages)

favorite_languages.sort(reverse=True) #ao contrario
print (favorite_languages)

favorite_languages.sort(key=lambda x: len(x)) #x é o argumento e len tira o tamanho, qual for menor ele ordena
print (favorite_languages) #ordem crescente de caracteres

print (len(favorite_languages)) #tamanho

#OUTRA VERSAO DO .SORT - sorted (cria função)

print (sorted(favorite_languages, key=lambda x: len(x)))