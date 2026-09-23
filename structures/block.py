def sacar(self, valor: float) -> None:

    if self.saldo >= valor:

        self.saldo -= valor

#fim do bloco if

#espaçamento de boas práticas (4line) - fim do metodo
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado")
        print ("retire seu dinheiro no caixa.")

    print ("obrigado por ser nosso cliente, tenha um bom-dia!")

def depositar(valor):
    saldo = 500
    saldo += valor 



sacar(100)