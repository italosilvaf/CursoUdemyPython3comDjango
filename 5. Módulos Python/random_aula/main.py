
import random
import string

print('\n------------------------------------------------------------------------\n')
print('Gera um número inteiro entre A e B')
inteiro1 = random.randint(0, 100)
print(inteiro1)

print('\n------------------------------------------------------------------------\n')
print('Gera um número aleatório usando a função range()')
inteiro2 = random.randrange(900, 1000, 10)
print(inteiro2)

print('\n------------------------------------------------------------------------\n')
print('Gera um número de ponto flutuante entre A e B:')
flutuante1 = random.uniform(0, 100)
print(flutuante1)

print('\n------------------------------------------------------------------------\n')
print('Gera um número de ponto flutuante entre 0 e 1:')
flutuante2 = random.random()
print(flutuante2)

print('\n------------------------------------------------------------------------\n')
print('Sorteia algum item da lista:')
lista1 = ['Italo', 'Giovanna', 'Clelia', 'Leonardo', 'Bruno', 'Leticia']
sorteio1 = random.choice(lista1)
print(sorteio1)

print('\n------------------------------------------------------------------------\n')
print('Sorteia "k" itens da lista, que pode se repetir:')
lista1 = ['Italo', 'Giovanna', 'Clelia', 'Leonardo', 'Bruno', 'Leticia']
sorteio2 = random.choices(lista1, k=2)
print(sorteio2)

print('\n------------------------------------------------------------------------\n')
print('Sorteia "k" itens da lista, que não se repete:')
lista1 = ['Italo', 'Giovanna', 'Clelia', 'Leonardo', 'Bruno', 'Leticia']
sorteio3 = random.sample(lista1, k=2)
print(sorteio3)

print('\n------------------------------------------------------------------------\n')

print('Embaralha os itens da lista:')
lista2 = ['Italo', 'Giovanna', 'Clelia', 'Leonardo', 'Bruno', 'Leticia']
random.shuffle(lista2)
print(lista2)

print('\n------------------------------------------------------------------------\n')

print('Gerando uma senha alearótia de 8 digitos')
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres

senha = ''.join(random.choices(geral, k=8))
print(senha)
