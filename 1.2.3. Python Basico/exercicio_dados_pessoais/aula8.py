"""
* Criar variáveis para nome (str),  idade (int)
* altura (float) e peso (float) de uma pessoa
* Criar variáveis com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valoes na tela usando F-Strings (com as chaves)
"""

nome = str(input('Qual o seu nome? '))
idade = int(input('Qual a sua idade? '))
altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
ano = int(input('Em que ano estamos? '))

anoNascimento = ano - idade
imc = peso / altura**2

print('\nResultados:\n')

print(f'{nome} tem {idade} anos de idade. Portanto {nome} nasceu em {anoNascimento}.'
      f'\nSua altura é de {altura} metros e seu peso de {peso} Kg.'
      f'\nConsequentemente seu IMC é de {imc:0.2f} kg/m^2.')
