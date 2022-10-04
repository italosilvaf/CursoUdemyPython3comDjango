"""
Exercício  de Compreensão de listas, objetivo:

Transformar a string = '01234567890123456789012345678901234567890123456789'
em retorno = '0123456789.0123456789.0123456789.0123456789.0123456789'
"""

string = '012345678901234567890123456789012345678901234567890123456789'

lista = [string[num:num + 10] for num in range(0, len(string), 10)]
retorno = '.'.join(lista)

print(retorno)
