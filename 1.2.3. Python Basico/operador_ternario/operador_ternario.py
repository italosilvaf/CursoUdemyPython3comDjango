"""
Operador ternário
"""
logged = True

msg = 'Usuário logado.' if logged == True else 'Usuário precisa logar.'
print(msg)

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg1 = 'Pode acessar' if e_de_maior else 'Não pode acessar.'

    print(msg1)
