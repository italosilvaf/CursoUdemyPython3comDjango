"""
Compreensao de Listas
"""

listas1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(listas1)

l1 = [variavel for variavel in listas1]
print(l1)

l2 = [variavel * 2 for variavel in listas1]
print(l2)

l3 = [(variavel, variavel2) for variavel in listas1 for variavel2 in range(3)]
print(l3)

listas2 = ['Italo', 'Silva', 'Fernandes']
print(listas2)

l4 = [variavel.replace('a', '@') for variavel in listas2]
print(l4)

tuplas1 = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
print(tuplas1)
print('oiiiiiiiiiiiii')
t1 = dict([(y, x) for x, y in tuplas1])
print(t1)

listas3 = list(range(11))
print(listas3)

l5 = [variavel for variavel in listas3 if variavel % 2 == 0]
print(l5)

l6 = [variavel for variavel in listas3 if variavel % 2 == 0 if variavel % 4 == 0]
print(l6)

l7 = [variavel if variavel % 3 == 0 else '*' for variavel in listas3]
print(l7)

