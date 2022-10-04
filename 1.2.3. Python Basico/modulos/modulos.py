"""
Módulos padrão do Python:
Módulos são arquivos .py (que contém código python) e servem
para expandir as funionalidades parão da linguagem.
"""
import sys
print(sys.platform)
# assim importo tudo de sys.

#################################################################

import random
# assim importo tudo de random.

lista1 = []
lista2 = []

for numero_aleatorio in range(10):
    numero_ale = random.randint(0, 10)
    lista1.append(numero_ale)

print(lista1)

#################################################################

from random import randint
# assim eu importo apenas o randint, que está em random.

for numero_aleatorio in range(10):
    numero_ale = randint(0, 10)
    lista2.append(numero_ale)

print(lista2)

#################################################################

from random import random as randomisar_entre_0_e_1
# assim eu importo apenas o random, que está em ransom e ainda renomeio como eu quiser.
print(randomisar_entre_0_e_1())

#################################################################
