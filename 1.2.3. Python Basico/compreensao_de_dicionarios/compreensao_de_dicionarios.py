"""
Compreensão de Dicionarios
"""

lista = [
    ('chave1', 1),
    ('chave2', 2),
    ('chave3', 3),
]

dici1 = {x: y*2 for x, y in lista}
print(dici1)

dici2 = {x.upper(): y for x, y in lista}
print(dici2)

set1 = {f'chave_{valor}': valor+5 for valor in range(10)}
print(set1)
