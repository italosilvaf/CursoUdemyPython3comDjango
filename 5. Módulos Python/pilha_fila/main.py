"""
Pilha e Fila
Pilha (stack) - LIFO - last in, first out.
    Exemplo: Pilha de livros que são adicionados um sobre o outro.
Fila (queue) - FIFO - first in, first out.
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitor colaterais em desempenho, porque a cada item
alterado, todos os índices serão modificados
"""

"""
Pilha
"""
pilha_de_livros = list()

pilha_de_livros.append('Livro 1')  # 1
pilha_de_livros.append('Livro 2')  # 2
pilha_de_livros.append('Livro 3')  # 3
pilha_de_livros.append('Livro 4')  # 4
pilha_de_livros.append('Livro 5')  # 5

livro_removido = pilha_de_livros.pop()  # 5
print(pilha_de_livros, livro_removido)

livro_removido = pilha_de_livros.pop()  # 4
print(pilha_de_livros, livro_removido)

livro_removido = pilha_de_livros.pop()  # 3
print(pilha_de_livros, livro_removido)

livro_removido = pilha_de_livros.pop()  # 2
print(pilha_de_livros, livro_removido)

livro_removido = pilha_de_livros.pop()  # 1
print(pilha_de_livros, livro_removido)

print('\n------------------------------------------------------------------------------------------------\n')
"""
Fila
"""
from collections import deque
fila1 = deque()

fila1.append('Italo')
fila1.append('Giovanna')
fila1.append('João')
fila1.append('Maria')
fila1.append('José')
fila1.append('Josefa')

print(fila1)

pessoa_removida = fila1.popleft()
print(f'{fila1} -> Chegou a vez de {pessoa_removida}.')

pessoa_removida = fila1.popleft()
print(f'{fila1} -> Chegou a vez de {pessoa_removida}.')

pessoa_removida = fila1.popleft()
print(f'{fila1} -> Chegou a vez de {pessoa_removida}.')

pessoa_removida = fila1.popleft()
print(f'{fila1} -> Chegou a vez de {pessoa_removida}.')

pessoa_removida = fila1.popleft()
print(f'{fila1} -> Chegou a vez de {pessoa_removida}.')

pessoa_removida = fila1.popleft()
print(f'{fila1} -> Está sem fila.')

print('\n------------------------------------------------------------------------------------------------\n')
"""
Fila com número máximo
"""
from time import sleep

fila2 = deque(maxlen=10)

for item in range(100):
    fila2.append(item)
    sleep(0.5)
    print(fila2)

print('\n------------------------------------------------------------------------------------------------\n')







