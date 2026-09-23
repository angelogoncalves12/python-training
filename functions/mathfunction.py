def somar(a, b):
    return a + b

def exibir_resultado(a,b,funcao):
    total = funcao(a, b)
    print(f"O resultado total é {a} + {b} = {total}")

exibir_resultado(10,10, somar)
op = somar

print(op(1,2))