numero = input("Digite um número: ")

if numero.isdigit():
    numero = int(numero)
    print (numero)
else: 
    print ("Valor Inválido")
#prevenção de erros com condicionais

try: 
    numero = int(input("Digite um numero: "))
    print (10 / numero)

except ZeroDivisionError:
    print ("Zero não é divisor")
except ValueError:
    print ("Digite apenas numeros.")
#SEJA CLARO NAS MENSAGENS!!

