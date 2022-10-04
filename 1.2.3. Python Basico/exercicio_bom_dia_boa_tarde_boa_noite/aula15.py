
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input('Digite um número inteiro: ')

if num.isdigit():
    num = int(num)

    if (num % 2) == 0:
        print(f'{num} é Par')

    else:
        print(f'{num} é Impar')

else:
    print('Você não digitou um número inteiro!')

print("\n---------------------------------------------------------------------------------\n")

"""
Faça um programa que pergunte a hora ao usuário e, basenado-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.
"""

hora = input('Digite o hora de agora: ')
min = input('Agora digite os minutos: ')

if hora.isdigit() and min.isdigit():

    hora = int(hora)
    min = int(min)

    if 0 <= min <= 59:

        if 0 <= hora < 12:
            print(f'Bom dia {hora}:{min}')

        elif 12 <= hora < 18:
            print(f'Boa Tarde {hora}:{min}')

        elif 18 <= hora <= 23:
            print(f'Boa Noite {hora}:{min}')

        else:
            print('Você não digitou valores válidos.')

    else:
        print('Você não digitou valores válidos.')

else:
    print('Você não digitou valores válidos.')

print("\n---------------------------------------------------------------------------------\n")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreve "Seu nome é grande".
"""

nome = input('Digite seu nome: ')

if 0 < len(nome) <= 4:
    print('Seu nome é curto')

elif len(nome) == 5 or len(nome) == 6:
    print('Seu nome é normal')

elif len(nome) > 6:
    print('Seu nome é grande')

else:
    print('Você não digitou nada.')

print("\n---------------------------------------------------------------------------------\n")
