# Leitura da linha de identificadores de transações
entrada = input()
transacoes = entrada.split()
transacoes_unicas = []
# TODO: Crie uma lista com as transações sem duplicatas, mantendo a ordem da primeira ocorrência
for transacao in transacoes:
  if (transacao not in transacoes_unicas):
    transacoes_unicas.append(transacao)




print(' '.join(transacoes_unicas))  
    # Dica: Percorra cada transação e adicione à lista apenas se ainda não estiver presente
    