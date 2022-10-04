"""
Groupby
"""

from itertools import groupby, tee

alunos = [
    {'nome': 'Italo', 'nota': 'A'},
    {'nome': 'Silva', 'nota': 'B'},
    {'nome': 'Fernandes', 'nota': 'D'},
    {'nome': 'Giovanna', 'nota': 'A'},
    {'nome': 'Martins', 'nota': 'C'},
    {'nome': 'Oliveira', 'nota': 'B'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'D'},
    {'nome': 'José', 'nota': 'C'},
    {'nome': 'Josefa', 'nota': 'A'},
    {'nome': 'Juana', 'nota': 'C'},
    {'nome': 'Mario', 'nota': 'D'},
    {'nome': 'Carlos', 'nota': 'C'},
    {'nome': 'Izadora', 'nota': 'A'},
    {'nome': 'Gabriela', 'nota': 'B'},
    {'nome': 'Leonardo', 'nota': 'A'},
    {'nome': 'Igor', 'nota': 'A'},
    {'nome': 'Vitoria', 'nota': 'C'},
]

ordem = lambda item: item['nota']

alunos.sort(key=ordem)
alunos_agrupados = groupby(alunos, ordem)

for agrupamento, valores_agrupados in alunos_agrupados:

    valor1, valor2 = tee(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')

    for aluno in valor1:
        print(f'\t{aluno}')

    quantidade = len(list(valor2))
    print(f'\t{quantidade} tirou {agrupamento}.\n')
