# criando dicionários 
# {}

pessoa = {"nome": "Angelo", "idade": 18}

pessoa = dict(nome="Angelo", idade=28)
#mesma coisa

pessoa["telefone"] = "2222-1313" 
#adicionar info -  dado: valor

print(pessoa)

contatos = {
    "angelica90@gmail.com": {"nome": "Angelica", "telefone": "2222-2222"},
    "carlos23@gmail.com": {"nome": "Carlos", "telefone": "3333-3333", "teste": {"a": 1}}
}

print(contatos["angelica90@gmail.com"]["telefone"])
print(contatos["carlos23@gmail.com"]["teste"]["a"])

for chave in contatos:
    print (chave, contatos)


contatos = {
    "angelica90@gmail.com": {"nome": "Angelica", "telefone": "2222-2222"},
}

copia = contatos.copy()
copia["angelica90@gmail.com"] = {"nome": "Ang"}

print(contatos)
print(copia)

dict.fromkeys({"nome", "telefone"})

dict.fromkeys(({"nome", "telefone"}), "vazio")

print(contatos.get("chave")) #se tiver ele diz
print(contatos.get("angelica90@gmail.com"))

resultado = contatos.keys()
print (resultado)

resultado = contatos.pop("angelica90@gmail.com")
print (resultado)

resultado = contatos.pop("angelica90@gmail.com", "argumento pra nao dar erro")

print (resultado)

contatos = {"nome": "Angelica", "telefone": "2222-2222"}
#print(contatos.popitem())


contatos.setdefault("nome", "Sara") #volta angelica
print(contatos)

contatos.setdefault("idade", 89) 
print (contatos)

contatos = {
    "angelica90@gmail.com": {"nome": "Angelica", "telefone": "2222-2222"},
}
contatos.update({"angelica90@gmail.com": {"nome": "Ang"}})
contatos.update({"carlos23@gmail.com": {"nome": "Carlos", "telefone": "3333-3333", "teste": {"a": 1}}
})

print(contatos)

print(contatos.values()) #so diz os valores

print("angelica90@gmail.com" in contatos)