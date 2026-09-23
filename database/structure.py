open("dados.txt", "r")

##open importa o banco de dados especifico
# r - read / w - write / a - adicionar
#WRITE SOBRESCREVE O ARQUIVO CHAMADO!!!!!!!!


#WTIH CRIA UM NOVO E PODEMOS ESCREVER NO WRITE
with open("dados2.txt", "w") as arquivo: #ARQUIVO É A VARIÁVEL PRA MEXER NELE
    arquivo.write ("AWAWAWA \n")
    arquivo.write ("EU sou FODA\n")

#with open("dados2.txt", "r") as arquivo: #ARQUIVO É A VARIÁVEL PRA MEXER NELE
#    conteudo = arquivo.read()

#print (conteudo)


with open("dados2.txt", "a") as arquivo: #ARQUIVO É A VARIÁVEL PRA MEXER NELE
    arquivo.write ("dev senior python\n")
    arquivo.write ("imagina o cara erra o a e bota w \n KKKKKKKKKK")


with open("dados2.txt", "r") as arquivo: #le linha por linha
    for linha in arquivo:
        print (linha.strip())