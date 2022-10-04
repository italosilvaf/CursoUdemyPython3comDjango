"""
Fuções em Python - Escopo
"""
variavel = 'Valor'


def funcao1():
    print(variavel)


def funcao2():
    global variavel  # Só assim para mudar a variavel glogalmente
    variavel = 'Outro valor'
    print(variavel)


funcao1()
funcao2()

print(variavel)
