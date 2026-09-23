#def é a palavra reservada para funções

def mensagem():
    print ("Olá Mundo!")

def mensagem2(nome):
    print (f"Seja bem vindo {nome}!")

def mensagem3(nome = "sem nome"):
    print (f"Seja bem vindo {nome}!")


mensagem()
mensagem2 (nome="Angelo")
mensagem3()

def calcular_total(numeros):
    return sum(numeros)

def ante_e_suces(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return sucessor, antecessor

print (calcular_total([10,20,30]))
print (ante_e_suces(10))

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234") #se inverter algo, ele vai registrar errado
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") #aqui não tem chance disso acontecer
#se qualquer parte da função for modificada, para de funcionar ^^^

salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
#passando como dicionário