"""
Sobreposição de Membros
"""

from classes import Cliente, ClienteVip

c1 = Cliente('Italo', 20)
print(c1.nome)
c1.falar()
c1.comprar()

print()

c2 = ClienteVip('Violeta', 79, 'Calazans')
print(c2.nome)
c2.falar()
