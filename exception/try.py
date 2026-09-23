try:
    numero = 10/0
    print (numero) #ele nao para o programa, yey
except ZeroDivisionError:
    print ("Erro: Bicho burro dividindo por zero")

try:
    numero = int("10a")
    print (numero)
except ValueError:
    print ("Porra véi, errou de novo")
finally:
    print ("EU NÃO SEI SE FOI ERRO, MAS ENCERRO POR AQUI.")