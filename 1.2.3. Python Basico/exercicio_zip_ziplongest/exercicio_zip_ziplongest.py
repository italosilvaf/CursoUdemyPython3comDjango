"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma noca lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exe,plo:
lista_a    =   [1, 2, 3, 4, 5, 6, 7]
lista_b    =   [1, 2, 3, 4]

==================================== resultado
lista_soma  =  [2, 4, 6, 8]
"""
import random

lista_a = [random.randrange(1, 10) for numeros_a in range(random.randrange(1, 10))]
print(lista_a)

lista_b = [random.randrange(1, 10) for numeros_b in range(random.randrange(1, 10))]
print(lista_b)

lista_soma = []
contagem = 0

for numeros_a in lista_a:
    numero_somado = numeros_a + lista_b[contagem]
    lista_soma.append(numero_somado)
    contagem += 1
    if len(lista_b) > len(lista_a) == contagem:
        break
    elif len(lista_a) > len(lista_b) == contagem:
        break

print(lista_soma)

print('--------------------------------------------------------------------------------------')

# Outra solução mais complexa e pequena:

lista_A = [random.randrange(1, 10) for numeros_a in range(random.randrange(1, 10))]
print(lista_A)

lista_B = [random.randrange(1, 10) for numeros_b in range(random.randrange(1, 10))]
print(lista_B)

lista_SOMA = [x + y for x, y in zip(lista_A, lista_B)]

print(lista_SOMA)
