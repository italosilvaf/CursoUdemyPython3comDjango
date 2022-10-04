"""
Entrada de dados
"""

nome = input('Qual o seu nome? ')
print(f'O usuário digitou {nome} e o tipo de variável é {type(nome)}.')

idade = input('Qual a sua idade? ')
print(f'O usuário digitou {idade} e o tipo de variável é {type(idade)}.')

ano = input('Em que ano estamos? ')
print(f'O usuário digitou {ano} e o tipo de variável é {type(ano)}.')

anoNascimento = int(ano) - int(idade)
print(f'{nome} tem {idade} anos. Consequentemente nasceu em {anoNascimento}.')

print('----------------------------------------------------------------------------------------------')

num1 = input('Digite um numero: ')
num2 = input('digite outro numero: ')

print(f'A soma deles é: {int(num1) + int(num2)}')
