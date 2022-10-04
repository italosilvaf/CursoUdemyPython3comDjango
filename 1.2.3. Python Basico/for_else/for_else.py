"""
For / Else em Python
"""
num = int(input('DIgite um número de 0 a 10: '))

listanum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in listanum:
    if 0 <= num <= 10:

        resultado = num % 2

        if resultado == 0:
            print(f'{num} é um número par.')
            break
        else:
            print(f'{num} é um número impar.')
            break
else:
    print('Você não digitou um número valido.')
