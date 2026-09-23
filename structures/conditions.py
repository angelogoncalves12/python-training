#saldo = 2000.0
#saque = float (input("Informe valor do saque: "))

#if saldo >= saque:
 #   print ("Saque em Andamento")
#else:
  #  print ("Saldo insuficiente")




opcao = int(input ("Informe uma opção\n [1] SACAR\n [2] Extrato\n :"))
saldo = 1000.0
retorno = True

while retorno == True:
    if opcao == 1:
        valor = float(input("informe a Quantia do Saque: "))
        if valor > saldo:
          print ("Saque Negado, Insira valor Válido")
        else:
         print ("Saque realizado. Tire as cédulas no Caixa")
    elif opcao == 2:
     print ("Exibindo o extrato...")
     print (saldo)
    else:
        print("Opção Inválida")
    retorno = str(input ("Deseja realizar outra operação?"))
    if retorno == "s" or "sim" or "Sim":
        retorno == True


#identacao
def sacar(self,valor: float) -> None:
  saldo = 500 #bloco metodo

  if self.saldo >= valor: #bloco if
    self.saldo -= valor
    print ("Valor SACADO!")
    print ("Retire seu dinheiro no Caixa")

  #fim do bloco if  
  print ("Obrigado por ser nosso cliente")

# fim do bloco metodo   
def depositar (valor):
  saldo = 500 
  saldo += valor
sacar (100)