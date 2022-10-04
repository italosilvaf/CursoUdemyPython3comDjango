print('###############################################')
print('Aruivo de texto 1:')
print('###############################################')

file1 = open('texto1.txt', 'w+')
file1.write('Linha 1\n')
file1.write('Linha 2\n')
file1.write('Linha 3\n')

file1.seek(0, 0)
print('Lendo linha:')
print(file1.read())

print('-----------------------------------------------')

file1.seek(0, 0)
print(file1.readline(), end='')
print(file1.readline(), end='')
print(file1.readline(), end='')

print('-----------------------------------------------')

file1.seek(0, 0)
print(file1.readlines())

print('-----------------------------------------------')

file1.seek(0, 0)
for linha in file1.readlines():
    print(linha, end='')

file1.close()

print('###############################################')
print('Aruivo de texto 2:')
print('###############################################')

with open('texto2.txt', 'w+') as file2:
    file2.write('Linha 1\n')
    file2.write('Linha 2\n')
    file2.write('Linha 3\n')

    file2.seek(0)
    print(file2.read())

print('-----------------------------------------------')

with open('texto2.txt', 'r') as file2:

    file2.seek(0)
    print(file2.read())

print('-----------------------------------------------')

with open('texto2.txt', 'a+') as file2:
    file2.write('Linha 4\n')
    file2.write('Linha 5\n')
    file2.write('Linha 6\n')

    file2.seek(0)
    print(file2.read())

print('-----------------------------------------------')

# file3 = open('texto3.txt', 'w+')

import os
os.remove('texto3.txt')

print('-----------------------------------------------')

import json

dicinario = {
    'Pessoa 1': {
        'nome': 'Italo',
        'idadde': 20
    },

    'Pessoa 2': {
        'nome': 'Giovanna',
        'idadde': 20
    },
}

dicinario_json = json.dumps(dicinario, indent=True)

with open('texto.json', 'w+') as file4:
    file4.write(dicinario_json)

print(dicinario_json)
