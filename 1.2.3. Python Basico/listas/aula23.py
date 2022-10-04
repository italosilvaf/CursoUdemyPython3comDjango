"""
Listas em pyhton
fatiamento
append, insert, pop, del, clear,extend, +
min, max
range
"""
#         0    1    2    4    5
lista = ['A', 'B', 'C', 'D', 'E']
#    -    5    4    3    2    1

print(lista[1])
print(lista[0:3])
print(lista[1:4])
print(lista[0:5:2])

lista[2] = 'Oi'
print(lista)

print('\n------------------------------------------------------------------------\n')

l1 = [1, 2, 3]
l2 = [4, 5, 6]

#  Somando listas
l3 = l1 + l2
print(l3)

l1.extend(l2)
print(l1)

#  Adicionando item no final da lista
l2.append('A')
print(l2)

#  Adicionando item em lugar especifico na lista
l1.insert(0, 'Italo')
print(l1)

#  Excluindo um item na lista
l1.pop(0)
print(l1)

#  Excluindo varios items na lista
del(l1[1:5])
print(l1)

#  Inprimindo o ultimo item da lista
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(l4))

#  Inprimindo o primeiro item da lista
print(min(l4))

#  Criando lista com range
l5 = list(range(1, 10))
print(l5)

l5 = list(range(0, 100, 7))
print(l5)
