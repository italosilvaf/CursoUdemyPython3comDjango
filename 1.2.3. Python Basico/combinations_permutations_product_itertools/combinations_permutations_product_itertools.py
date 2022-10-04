"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Italo', 'Silva', 'Fernandes', 'Calazans', 'Calazencio']

print('Usando combinations (Ordem não importa):')
for grupo in combinations(pessoas, 2):
    print(grupo)

print('\n----------------------------------------------------------------------------------\n')

print('Usando permutations (Ordem importa):')
for grupo in permutations(pessoas, 2):
    print(grupo)

print('\n----------------------------------------------------------------------------------\n')

print('Usando pruduct (Ordem importa e repete valores únicos):')
for grupo in permutations(pessoas, 2):
    print(grupo)
