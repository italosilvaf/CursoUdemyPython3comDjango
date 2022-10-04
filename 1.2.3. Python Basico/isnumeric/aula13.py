
num1 = input('Digite um número positivo: ')
num2 = input('Digite outro número positivo: ')

if num1.isnumeric() and num2.isnumeric():

    num1 = int(num1)
    num2 = int(num2)
    soma = num1 + num2

    print(f'{num1} + {num2} = {soma}')

else:
    print('Você não digitou um número positivo.')
