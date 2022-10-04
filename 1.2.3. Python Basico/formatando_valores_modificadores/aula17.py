"""
Formatando valores com modificadores

:s - Texte (string)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIADE)(TIPO - s, d oou f)

> - Esuqerda
< - Direita
^ - Centro
"""

num1 = int(input('Vamos fazer uma divisão \nDigite o numerador: '))
num2 = int(input('Digite o denominador: '))

divisao = num1 / num2

print('O Resultado é {:.3f}'.format(divisao))

print('\n---------------------------------------------------------------------------------------\n')

nome = 'Italo'
sobrenome1 = 'silva'
sobrenome2 = 'fErNaNdEs'

print(f'{nome:#>11}')
print(f'{nome:#<11}')
print(f'{nome:#^11}')

print('\n---------------------------------------------------------------------------------------\n')

nome_formatado1 = '{nf:@>11} {sn1:@>11}'.format(nf=nome, sn1=sobrenome1)
nome_formatado2 = '{nf:@<11} {sn1:@<11}'.format(nf=nome, sn1=sobrenome1)
nome_formatado3 = '{nf:@^11} {sn1:@^11}'.format(nf=nome, sn1=sobrenome1)

print(nome_formatado1)
print(nome_formatado2)
print(nome_formatado3)

print('\n---------------------------------------------------------------------------------------\n')

print(f'{nome.lower()} {sobrenome1.lower()} {sobrenome2.lower()}')  # Tudo minusculo
print(f'{nome.upper()} {sobrenome1.upper()} {sobrenome2.upper()}')  # Tudo maiúsculo
print(f'{nome.title()} {sobrenome1.title()} {sobrenome2.title()}')  # Primeiras letras maiusculos

print('\n---------------------------------------------------------------------------------------\n')


