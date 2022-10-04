"""
public, protected, private
"""
from classe_base_de_dados import BaseDeDados

bd = BaseDeDados()

bd.inserir_cleinte(1, 'Italo')
bd.inserir_cleinte(2, 'Giovanna')
bd.__dados = 'Outra coisa'

print(bd.__dados)
print(bd._BaseDeDados__dados)

print()

bd.lista_clientes()

print()

print(bd.dados)
