curso = "Python Lerning" 
nome_curso = curso 
saldo, limite = 200, 200

print (curso is nome_curso)
print (curso is not nome_curso)
print (saldo is limite)


#asoociação 

curso = "python learning"
frutas = ["laranja", "uva", "limão"]
saques = [1200, 100]

print ("python" in curso)
print ("maçã" not in frutas)
print ("laranja" not in frutas)
print (200 in saques)