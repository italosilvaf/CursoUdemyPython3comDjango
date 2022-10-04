"""
count - Itertools
"""

from itertools import count

contador = count(start=10, step=-1)
# count(start="Começo", step="Pulo")
# "Começo" = De onde quer que o contador comece, podendo ser negatico
# "Pulo" = O pulo da contagem. Pode ser negativo, assim a contagem é regressiva.

for valor in contador:
    print(valor)

    if valor >= 100 or valor <= -100:
        break
