conta_normal = True
conta_universitaria = False

saldo = 2000.0
print ("Seu saldo é de", saldo)
saque = float(input ("Qual o valor do Saque? "))
cheque_especial = 450.0

if conta_normal:
    if saldo >= saque:
        print ("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print ("Saque realizado com Cheque Especial!")
    else:
        print ("Saldo Insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print ("Saque realizado com sucesso!")
    else:
        print ("Saldo Insuficiente")

#if ternário 
status = "Sucesso" if saldo >= saque else "Falha"
print (f"{status} ao realizar o saque!")