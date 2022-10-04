"""
Reduce
"""
from dados import produtos, pessoas, lista
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)

print('Somando todos os itens da lista:\n')

print(lista)
print(soma_lista)

print('\n---------------------------------------------\n')

print('Lista de produtos:\n')

for produto in produtos:
    print(produto)

print('\n---------------------------------------------\n')

print('Lista de pessoas:\n')

for pessoa in pessoas:
    print(pessoa)

print('\n---------------------------------------------\n')

print('Imprimindo a média de preços dos produtos:\n')

soma_preco = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_preco / len(produtos))

print('\n---------------------------------------------\n')

print('Imprimindo a média de idade das pessoas:\n')

soma_idade = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(soma_idade / len(pessoas))
