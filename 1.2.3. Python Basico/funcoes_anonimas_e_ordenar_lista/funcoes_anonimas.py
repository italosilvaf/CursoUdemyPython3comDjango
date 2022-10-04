"""
Expressões lambda (funções anônimas) em Python

def funcao(ordem):       É a mesma coisa de -->  lambda ordem: ordem[0]
    return ordem[0]

"""

lista = [
    ['Produto-4', 12.89],
    ['Produto-1', 24.35],
    ['Produto-3', 4.32],
    ['Produto-2', 89.72],
    ['Produto-5', 156.78],
]

while True:
    lugar = 0
    if lugar >= 0:
        for ordemlista in lista:
            print(lista[lugar])
            lugar += 1
            continue
    elif lugar == len(lista):
        continue
    print('-------------------------------------------------------------------------')
    break

lista1 = sorted(lista, key=lambda ordem: ordem[0])
while True:
    lugar = 0
    if lugar >= 0:
        for ordemlista in lista1:
            print(lista1[lugar])
            lugar += 1
            continue
    elif lugar == len(lista1):
        continue
    print('-------------------------------------------------------------------------')
    break

lista2 = sorted(lista, key=lambda ordem: ordem[1])
while True:
    lugar = 0
    if lugar >= 0:
        for ordemlista in lista2:
            print(lista2[lugar])
            lugar += 1
            continue
    elif lugar == len(lista2):
        continue
    print('-------------------------------------------------------------------------')
    break
