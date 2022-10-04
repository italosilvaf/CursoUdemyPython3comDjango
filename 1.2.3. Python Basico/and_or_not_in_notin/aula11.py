"""
Oderadores Lógicos
and, or, not
in e not in
"""

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

if 18 <= idade <= 35:
    resposta = input('Você deseja fazer um emprestimo? ')

    if 's' in resposta:
        print('Otimo, vamos ligar para você para pegarmos os seus dados.')
        telefone = input('Qual o seu número de telefone? ')
        respostatel = input(f'Seu número de telefone é {telefone}? ')

        if 's' in respostatel:
            print('Ok, ligaremos assim que possivel.')

        elif 'n' in resposta:
            print('Que pena, vamos começar do início.')

        else:
            print('Não entendi sua resposta.')

    elif 'n' in resposta:
        print('Ok, Obrigado por responder.')

    else:
        print('Não entendi sua resposta.')

else:
    print('Você não pode fazer nenhum tipo de empretimo com a gente.')
