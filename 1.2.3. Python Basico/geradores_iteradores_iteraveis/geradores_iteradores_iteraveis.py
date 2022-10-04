import sys

lista1 = [0, 1, 2, 3, 4, 5]
lista1 = iter(lista1)  # Iterador

print(next(lista1))
print(next(lista1))
print(next(lista1))
print(next(lista1))
print(next(lista1))
print(next(lista1))

lista2 = list(range(1000))
print(sys.getsizeof(lista2))  # Número de bits

lista3 = [valor for valor in range(1000000)]
print(sys.getsizeof(lista3), type(lista3))
lista4 = (valor for valor in range(1000000))
print(sys.getsizeof(lista4), type(lista4))

print('-' * 1000)

nome = 'Italo Silva'  # list, tuple, str -> Seqeuncer -> Iterável

for letra in nome:
    print(letra)

print('-' * 1000)

iterador = iter(nome)

print(next(iterador))  # I
print(next(iterador))  # t
print(next(iterador))  # a
print(next(iterador))  # l
print(next(iterador))  # o
print(next(iterador))  #
print(next(iterador))  # S
print(next(iterador))  # i
print(next(iterador))  # l
print(next(iterador))  # v
print(next(iterador))  # a
# print(next(iterador)) Se eu colocar esse comando da um erro, pois o interador fa foi consumido inteiro

gerador = (letra for letra in nome)
print('-' * 1000)

print(next(gerador))  # I
print(next(gerador))  # t
print(next(gerador))  # a
print(next(gerador))  # l
print(next(gerador))  # o
print(next(gerador))  #
print(next(gerador))  # S

print('For funciona apartir daqui: ')

for letra in gerador:
    print(letra)
