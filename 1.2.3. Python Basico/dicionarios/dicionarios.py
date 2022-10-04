"""
Dicionarios
"""

dicionario1 = {'Chave1': 'Valor da chave1'}
dicionario1['Nova chave'] = 'Valor da nova chave'

print(dicionario1)
print(dicionario1['Chave1'])

print('--------------------------------------------------------------------------')

dicionario2 = dict(Chave1='Valor da chave', Chave2='Valor da outra chave')
print(dicionario2)

print('--------------------------------------------------------------------------')

dicionario3 = {'Chv': 'Italo', 'Chv': 'Silva', 'Chv': 'Fernandes'}
print(dicionario3)  # Se tiver chaves iguais, é considerado a ultima chave.

print('--------------------------------------------------------------------------')

dicionario4 = {
    'str': 'String',
    1: 'Int',
    (1, 2, 3): 'Tupla'
}  # Qual tipo de dado pode ser uma chave.
print(dicionario4)

print('--------------------------------------------------------------------------')

dicionario5 = {1: 'a', 2: 'b', 3: 'c'}
dici5 = dicionario5

dici5[1] = 'ABC'  # dessa forma os dois dicionarios são mudados

print(dicionario5)
print(dici5)

print('--------------------------------------------------------------------------')

import copy

dicionario6 = {1: 'a', 2: 'b', 3: 'c'}
dici6 = copy.deepcopy(dicionario6)

dici6[1] = 'ABC'  # dici6 é uma copia de dicionario6

print(dicionario6)
print(dici6)

print('--------------------------------------------------------------------------')

clientes = {
    'cliente1': {
        'nome': 'Italo',
        'sobrenome': 'Fernandes',
        'idade': 20
    },

    'cliente2': {
        'nome': 'Giovanna',
        'sobrenome': 'Martins',
        'idade': 20
    },

    'cliente3': {
        'nome': 'João',
        'sobrenome': 'Silva',
        'idade': 50
    }
}

for cliente, clientedados in clientes.items():
    print(f'Exibinco o {cliente}')
    for tipodados, dados in clientedados.items():
        print(f'\t {tipodados} = {dados}')
    print('\n')

print('--------------------------------------------------------------------------')

dicionarioA = {1: 'Oi', 2: 'Olá', 3: 'Hello', 4: 'Hi'}
print(dicionarioA[5])  # Chave não esxite, porem o resto do codigo não funciona.

print('Tuso bem?')
