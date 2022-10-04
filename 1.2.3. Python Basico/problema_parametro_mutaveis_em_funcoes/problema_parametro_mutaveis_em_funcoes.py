"""
Mutavél: Listas, dicionarios
Imutável: Tuplas, strings, números, True, False, None
"""


def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes1 = ['Hermelindo']
clientes1 = lista_de_clientes(['Italo', 'Silva', 'Fernandes'], lista_clientes1)
clientes2 = lista_de_clientes(['Giovanna', 'Martins', 'Oliveira'])
clientes3 = lista_de_clientes(['Violeta'])

print(clientes1)
print(clientes2)
print(clientes3)
