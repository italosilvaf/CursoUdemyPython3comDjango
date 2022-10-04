"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count

indice = count()  # contador no início de cada valor
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro', 'Patos de Minas']
estados = ['SP', 'MG', 'BA', 'RJ']

cidades_estados_zip = zip(cidades, estados)  # Uniu cidades e estados e Patos de Minas não aparece por não ter o estado
print(list(cidades_estados_zip))  # Dei print e passei a junção para lista

estados_cidades_zip = zip(estados, cidades)  # Uniu estados e cidades e Patos de Minas não aparece por não ter o estado
print(dict(estados_cidades_zip))  # Dei print e passei a junção para dicionário

cidades_estados_ziplongest = zip_longest(cidades, estados)  # Dei print e passei a junção para dicionário
print(list(cidades_estados_ziplongest))  # Dei print e passei a junção para lista

estados_cidades_ziplongest = zip_longest(estados, cidades, fillvalue='Estado')
# Dei print, passei a junção para dicionário e adicionai o estado para Patos de Minas
print(dict(estados_cidades_ziplongest))  # Dei print, passei a junção para dicionário e criei o estado de Patos de Minas

indice_estados_cidades = zip(indice, estados, cidades)  # com o indice os valores serão enumerados
for indice, estados, cidades in indice_estados_cidades:
    print(indice, estados, cidades)
