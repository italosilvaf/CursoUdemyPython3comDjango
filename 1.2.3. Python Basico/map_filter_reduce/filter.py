"""
Filter
"""
from dados import pessoas, produtos, lista

nova_lista = filter(lambda x: x > 5, lista)
nova_lista1 = [x for x in lista if x > 5]

print('A lista foi filtrada em números maiore que 5:\n')

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

print('A lista de produtos foi filtrada em produtos que tem o preço maior que 50: \n')


def filtra_preco(p):
    if p['preco'] > 50:
        return True
    else:
        return False


filtro_precos = filter(filtra_preco, produtos)

for produto in filtro_precos:
    print(produto)

print('\n---------------------------------------------\n')

print('A lista de produtos foi filtrada em pessoas que são menor de idade: \n')


def filtro_idade(i):
    if i['idade'] < 18:
        return True
    else:
        return False


filtro_idades = filter(filtro_idade, pessoas)

for pessoa in filtro_idades:
    print(pessoa)
