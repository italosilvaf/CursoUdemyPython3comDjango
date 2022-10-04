"""
Exercicio de função:

1- Crei uma função que recebe uma função2 como parametro e retorne o valor da função2 executada.
"""


def funcao1():
    return 'Oi'


def funcao2(func):
    return func()


executar = funcao2(funcao1)
print(executar)

print('---------------------------------------------------------------------------------------------------------')
"""
2- Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
Faça a função1 executar duas funções que recebam um número diferente de argumentos.
"""


def mestre(func1, *agrs, **kwagrs):
    return func1(*agrs, **kwagrs)


def funcao_oi(nome):
    return f'Oi {nome}'


def funcao_saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando1 = mestre(funcao_oi, 'Italo')
print(executando1)

executando2 = mestre(funcao_saudacao, 'Italo', saudacao='Olá')
print(executando2)
