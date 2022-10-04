"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""
from classes import Pessoa, Cliente, Aluno

p1 = Pessoa('Hermelindo', 80)
print(p1.nome)
p1.falar()

print()

c1 = Cliente('Italo', 20)
print(c1.nome)
c1.falar()
c1.comprar()

print()

a1 = Aluno('Giovanna', 21)
print(a1.nome)
a1.falar()
a1.estudar()

