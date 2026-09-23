texto = input("Informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper () in vogais:
        print(letra, end="")
else: # executa ao final do laco, nesse caso nem precisava
    print () #separa vogais 



#range - stop, start e step
for numero in range(0,11):
    print(numero, end=" ")



#tabuada do cinco
for numero in range(0, 51, 5):
    if numero % 2 == 0:
        continue

    if numero == 13:
        print ("Oia o L \n")
        break

    print(numero, end= " ")



opcao = -1
while opcao !=0:
    opcao = int(input("\n[1] Sacar \n[2] Depositar \n[0] Sair \n "))

    if opcao == 1:
        print("Saque Realizado...")
    elif opcao == 2:
        print("Exibindo o Extrato")
    else:
        print ("Obrigado por Utilizar nosso Sistema, Até Mais!")
    break

while True:
    numero = int(input("Digite um inteiro: "))

    if numero % 2 == 0:
        break  
     
    else:
        continue
     