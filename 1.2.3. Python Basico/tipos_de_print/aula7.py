
nome = 'Italo SF'
idade = 20
altura = 1.83
e_maior = idade > 18
peso = 72
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos')
print(f'{nome} tem {idade} anos')
print(f'{nome} tem {idade} anos e seu imc é {imc}')
print(f'{nome} tem {idade} anos e seu imc é {imc:0.2f}')
print('{} tem {} anos e seu imc é {}'.format(nome, idade, imc))
print('{} tem {} anos e seu imc é {:0.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos e seu imc é {2}'.format(nome, idade, imc))
print('{2} tem {0} anos e seu imc é {1}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))
