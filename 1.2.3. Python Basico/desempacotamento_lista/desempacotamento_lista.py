"""
Desempacotamento de listas
"""

lista = ['um', 'dois', 'tres', 'quatro', 'cinco']

one, two, *_ = lista

print(one)
print(two)
print(_)
