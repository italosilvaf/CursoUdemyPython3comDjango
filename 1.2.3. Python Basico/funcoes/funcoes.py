"""
1- Crie um função que exibe uma saudação com os parâmetros saudacao e nome.
"""


def saudacao_nome(saudacao, nome):
    return print(f'{saudacao} {nome}')


saudacao_nome('Oi', 'Italo')
saudacao_nome('Hello', 'World')

print('------------------------------------------------------------------------------------------')

"""
2- Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles
"""


def soma_numeros(num1, num2, num3):
    soma = num1 + num2 + num3
    return print(f'{num1} + {num2} + {num3} = {soma}')


soma_numeros(1, 1, 1)
soma_numeros(1, 2, 3)
soma_numeros(10, 5, 15)

print('------------------------------------------------------------------------------------------')

"""
Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual.
Retorne o valor do primeiro número do aumento do percentual do mesmo.
"""


def percentual(num, nump):
    resultado = ((nump * num) / 100)+ num
    return print(f'{num} + {nump}% de {num} = {resultado}')


percentual(100, 10)
percentual(100, 50)
percentual(8456, 25)

print('------------------------------------------------------------------------------------------')

"""
4- Fizz Buzz - Se o parâmetro da funcção for divisível por 3, retorne fizz, 
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e 3, retorne FizzBuzz, caso contrário retorne o número enviado.
"""


def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return print(f'FizzBuzz, {numero} é divisicel por 3 e 5.')
    if numero % 3 == 0:
        return print(f'Fizz, {numero} é divisicel por 3.')
    if numero % 5 == 0:
        return print(f'Buzz, {numero} é divisicel por 5')
    return print(numero)


fizzbuzz(7)
fizzbuzz(9)
fizzbuzz(10)
fizzbuzz(15)
