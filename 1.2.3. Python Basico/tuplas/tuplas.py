"""
Tuplas - Não pode ser editada
"""

tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5
print(tupla2)
print(type(tupla2))

tupla3 = 1,
print(tupla3)
print(type(tupla3))

# Conversão de tupla pra lsita

tupla = (1, 2, 3, 4, 5)
tupla = list(tupla)
tupla[0] = 'Italo'

print(tupla)
