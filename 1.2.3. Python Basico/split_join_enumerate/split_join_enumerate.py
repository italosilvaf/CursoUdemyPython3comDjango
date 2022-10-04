"""
Split, Join, Enumerate em Python
* Split - DIvidir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""

frase = 'O Brasil é o pais do futebol, por isso o Brasil é penta campeão.'

lista1 = frase.split(' ')
print(lista1)
for valor in lista1:
    print(valor)

print('___________________________________________________________________________________')

lista2 = frase.split(',')
print(lista2)
for valor in lista2:
    print(valor.strip().capitalize())

print('___________________________________________________________________________________')

for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)} vezes na frase.')

print('___________________________________________________________________________________')

palavra = ''
contagem = 0

for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes foi "{palavra}" ({contagem}x).')

print('___________________________________________________________________________________')

string2 = 'O Brasil é o pais do futebol, por isso o Brasil é penta campeão.'
lista3 = string2.split(' ')

print(lista3)

string3 = '_'.join(lista3)
print(string3)

print('___________________________________________________________________________________')

string4 = 'O Brasil é o pais do futebol, por isso o Brasil é penta campeão.'
lista4 = string2.split(' ')

for indice, valor_real in enumerate(lista4):
    print(indice, valor_real)

print('___________________________________________________________________________________')

lista5 = [
  # 0              1            2
    ['Italo',      'Silva',     'Fernandes'],   # 0
    ['Giovanna',   'Martins',   'Oliveira'],    # 1
    ['00001',      '0002',      '0003'],        # 2
]

# lista5[linha][coluna]
print(lista5[1][1])
print(lista5[0][2])
print(lista5[2][1])

enumerada = enumerate(lista5)
print(list(enumerada))

