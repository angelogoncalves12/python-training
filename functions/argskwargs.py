# args na tupla - representado por *
# kargs no dicionário (chave = valor)  representado por **

def exibir_poema(data_extenso, *pipipi, **popopo):
    texto = "\n".join(pipipi)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in popopo.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Domingo, 20 de Setembro de 2026",
    
    "Meu Deus! E este morcego! E, agora, vede:",
    "Na bruta ardência orgânica da sede,",
    "Morde-me a goela ígneo e escaldante molho.",
    
   
    "Vou mandar levantar outra parede...",
    "— Digo. Ergo-me a tremer. Fecho o ferrolho",
    "E olho o teto. E vejo-o ainda, igual a um olho,",
    "Circularmente sobre a minha rede!",
    
    "Pego de um pau. Esforços faço. Chego",
    "A tocá-lo. Minh'alma se concentra.",
    "Que ventre produziu tão feio parto?!",

    "A Consciência Humana é este morcego!",
    "Por mais que a gente faça, à noite, ele entra",
    "Imperceptivelmente em nosso quarto!",
    autor="Augusto dos Anjos",
    ano=1999,
)