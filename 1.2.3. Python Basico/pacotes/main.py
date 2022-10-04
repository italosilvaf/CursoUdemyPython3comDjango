"""
Main do programa
"""
from vendas.calculo_preco import aumeta_preco, reduz_preco
from vendas.formata.preco import real

preco1 = 1000

print(aumeta_preco(preco1, 27, True))
print(reduz_preco(preco1, 30, True))

preco2 = 7
print(aumeta_preco(preco2, 0.516))
print(aumeta_preco(preco2, 0.516, True))

print(real(15))
