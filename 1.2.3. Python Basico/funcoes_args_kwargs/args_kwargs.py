"""
Funções (def) em Python - *args **kwargs
Posso escolher o nome: *argumentos
"""


def func(*args, **kwargs):
    print(args)
    print(args[0])

    nomekw = kwargs.get('nome')
    sobrenomekw = kwargs.get('sobrenome')

    if nomekw is not None and sobrenomekw is not None:
        print(f'Existe nome e sobrenome: {nomekw}, {sobrenomekw}.')
    elif nomekw is not None:
        print(f'Existe apenas nome: {nomekw}.')
    elif sobrenomekw is not None:
        print(f'Existe apenas sobrenome: {sobrenomekw}')
    else:
        print('Não existe nome nem sobrenome.')
    print('--------------------------------------------------------')


lista1 = [1, 2, 3, 4, 5]
func(lista1, 6, nome='Italo', sobrenome='Fernadnes')

lista2 = [10, 20, 30, 40, 50]
func(*lista2, 60, nome='Italo', sobrenome='Fernadnes')

func(lista1, *lista2, nome='Italo')
func(*lista1, *lista2, sobrenome='Fernandes')
func(lista1, lista2)

