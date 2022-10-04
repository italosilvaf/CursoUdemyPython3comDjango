"""
Condições If, Elif e Else
"""

num = int(input('Digite um número inteiro para que podemos classifica-lo entre'
                '\npositivo ou negativo e impar ou Par: '))
if num >= 0:
    if num % 2 == 0:
        print(f'O número {num} é positivo e par.')
    else:
        print(f'O numero {num} é positivo e impar.')
else:
    if num % 2 == 0:
        print(f'O número {num} é negativo e par.')
    else:
        print(f'O numero {num} é negativo e impar.')

idade = int(input('\nDigite sua idade: '))
numq = int(input('Digite um número qualquer: '))

if numq > idade:
    print(f'{numq} é maior que {idade}.')
elif numq < idade:
    print(f'{numq} é menor que {idade}.')
else:
    print(f'{numq} é igual a {idade}.')
