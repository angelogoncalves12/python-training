curso = "pYtHon"

print(curso.upper())

print(curso.lower())

print(curso.title())

curso = "   Python"
print(curso.strip())

print(curso.lstrip())

print(curso.rstrip())

curso = "Python"

print(curso.center(10,"$"))
#se nao informar caracter nas aspas, vai espaço vazio.
print (".".join(curso))


#variaveis com string - %d  %f %s
nome = "Angelo"
idade = 18
profissao = "Programador"
linguagem = "Python"
dados = {"nome": "Angelo", "profissao": "Programador", "linguagem": "Python", "idade": 18}

print ("Olá, me chamo %s. Eu tenho %d anos de idade," 
"trabalho como %s e estou revisando %s" % (nome,idade,profissao,linguagem))
#abordagem oldstylw


#metodo format
print ("Olá, me chamo {}. Eu tenho {} anos de idade," 
"trabalho como {} e estou revisando {}" .format(nome,idade,profissao,linguagem))

print ("Olá, me chamo {0}. Eu tenho {1} anos de idade," 
"trabalho como {2} e estou revisando {3}" .format(nome,idade,profissao,linguagem))

print ("Olá, me chamo {nome}. Eu tenho {idade} anos de idade," 
"trabalho como {profissao} e estou revisando {linguagem}" .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print (f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade," 
f"trabalho como {profissao} e estou revisando {linguagem}" .format(**dados))

#metodo f-string
print (f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade," 
f"trabalho como {profissao} e estou revisando {linguagem}" )

PI = 2.14159

print(f"Valor de PI: {PI:.2f}")