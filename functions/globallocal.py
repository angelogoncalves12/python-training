# escopo global vs escopo local

salario = 2000 #global

def decimo_terceiro(bonus):
    global salario #avisando pra função que tá fora dela!!
    #OBRIGATORIO PARA ESSES CASOS
    lista.append(2) #vai adicionar de qualquer jeito
 #a dica é criar uma cópia se não quiser alterar o externo
    salario += bonus
    return salario

lista = [1]
salario_bonus = decimo_terceiro(1600, lista)
print(salario_bonus)