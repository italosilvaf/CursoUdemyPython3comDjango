"""
Map
"""
from dados import produtos, pessoas, lista

nova_lista = map(lambda valor: valor * 2, lista)
nova_lista1 = [x * 2 for x in lista]

print('Multiplicando lista por 2:\n')

print(lista)
print(list(nova_lista))
print(nova_lista1)

print('\n---------------------------------------------\n')

print('Lista de produtos:\n')

for produto in produtos:
    print(produto)

print('\n---------------------------------------------\n')

print('Lista de pessoas:\n')

for pessoa in pessoas:
    print(pessoa)

print('\n---------------------------------------------\n')

print('Aumentando os preços em 50%:\n')


def aumenta_preco(p):
    p['preco'] = round(p['preco'] + 1.5, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)

print('\n---------------------------------------------\n')

print('Imprimindo apenas os nomes:\n')

nomes = map(lambda n: n['nome'], pessoas)

for nome in nomes:
    print(nome)

print('\n---------------------------------------------\n')

print('Imprimindo apenas as idades:\n')

idades = map(lambda i: i['idade'], pessoas)

for idade in idades:
    print(idade)

print('\n---------------------------------------------\n')

print('Aumentando a idade de cada pessoa com mais 5 anos:\n')


def aumenta_idade(p):
    p = p['idade'] + 5
    return p


idades_aumentadas = map(aumenta_idade, pessoas)

for pessoa in idades_aumentadas:
    print(pessoa)
