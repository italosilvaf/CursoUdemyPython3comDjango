"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Italo'
print(nome, type(nome))

print('---------------------------------------------------------------------------')

nome = 'Italo SF'
idade = 20
altura = 1.83
e_maior = idade > 18

print('Nome:', nome)
print('Idade:', idade)
print('Altura', altura)
print('É Maior: ', e_maior)

print('---------------------------------------------------------------------------')

print('Vamos fazer uma duvisão:')
x = int(input('Digite o numerador: '))
y = int(input('Digite o divisor: '))

resultado = float(x / y)
print('O resultador é: ', resultado)
