"""
add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetruc)differebce ^ (Elementos que estão nos dois sets, mas não em ambos)
"""

set1 = set()
set1. add(1)
set1. add(2)  # adiciona um item no set
print(set1)

###################################################################################

set1.discard(2)  # discarta o elemento do set
print(set1)

###################################################################################

set1.update('Python')  # adiciona cada item iterado da String
print(set1)

###################################################################################

set2 = set()
set2.update([1, 2, 3, 4, 5], [4, 5])  # Não adiciona itens duplicados
print(set2)

###################################################################################

lista1 = [1, 2, 3, 2, 5, 4, 6, 3, 5, 4, 1, 2, 3, 5, 4, 6, 5, 6]
lista1 = set(lista1)
lista1 = list(lista1)  # podemos usar os sets para tirar itens repedidos de listas

print(lista1)

###################################################################################

set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6}

set5 = set3 | set4  # unindo os dois sets
print(set5)

###################################################################################

set6 = {1, 2, 3, 4, 5}
set7 = {4, 5, 6}

set8 = set6 & set7  # set8 tem todos os itens que exixte nos 2 sets
print(set8)

###################################################################################

set9 = {1, 2, 3, 4, 5, 7}
set10 = {1, 2, 3, 4, 5, 6}

set11 = set9 - set10  # Teremos apenas os elementos dos set da esquerda menos os elementos da direita
print(set11)

set12 = set10 - set9
print(set12)

###################################################################################

sets1 = {1, 2, 3, 4, 5, 7}
sets2 = {1, 2, 3, 4, 5, 6}

sets3 = sets2 ^ sets1  # São sadicionados elementos que estão diferentes nos dois sets
print(sets3)

###################################################################################
