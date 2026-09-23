import logging

#logging.basicConfig(level=logging.INFO)
# o nivel info sao informações gerais do programa
#logging.info("Programa iniciado")

logging.basicConfig(level=logging.DEBUG) #detalhes de funcionamento
#muito importante!!
logging.debug("Mensagem de Debug")
logging.warning("Mensagem de Atenção")
logging.error("Mensagem de Erro")
logging.info("Programa iniciado")