#argumentos de posição, não importa o nome

def carro(modelo,ano,placa, /, marca, motor, combustivel):
    print(modelo,ano,placa, marca, motor, combustivel)

carro("Palio", 2014, "ABC-1234", marca="Fiat",
motor="1.0", combustivel="gasolina")
# valido, argumentos antes da barra nao podem 
#ser citados na nomeação

##carro(modelo="Palio", ano=2014, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="gasolina")
#invalido, nao registra


#argumentos de nome (keyword)

def salvar_carro(*,marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


#salvar_carro("Fiat", "Palio", 1999, "ABC-1234") #invalido
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")


#modelo hibrido

def carro(modelo,ano,placa, /,marca, *, motor, combustivel): #o que fica entre os dois é opcional
    print(modelo,ano,placa, marca, motor, combustivel)

carro("Palio", 2014, "ABC-1234", marca="Fiat",
motor="1.0", combustivel="gasolina") #meio positiion, meio key

 