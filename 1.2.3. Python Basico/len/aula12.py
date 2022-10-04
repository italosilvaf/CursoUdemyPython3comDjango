
usuario = input('Digite seu usuário: ')
qtdc = len(usuario)

if qtdc != 7:
    print('Você precisa digitar 7 caracteres')
else:
    print('Cadastrado com sucesso')

print('-----------------------------------------------------------------------------')

str1 = input('Digite um nome: ')
str2 = input('Digite um sobrenome: ')

print(f'A quantidade de caracteres digitado foi de {len(str1) + len(str2)} catacteres.')
