

def fala_oi():
    print('Oi')


variavel = fala_oi

variavel()
print(type(variavel))

print('-----------------------------------------------------')


def master():
    def slave():
        print('Olá')
    return slave


variavel = master()
variavel()
print(type(variavel))

print('-----------------------------------------------------')


def master(funcao):
    def slave():
        funcao()
    return slave


def fala_italo():
    print('Italo')


variavel = master(fala_italo)
variavel()
print(type(variavel))

print('-----------------------------------------------------')


def master(funcao):
    def slave():
        print('Agora estou decorada.')
        funcao()
    return slave


@master
def fala_italo():
    print('Italo')


fala_italo()

print('-----------------------------------------------------')


def master(funcao):
    def slave(*args, **kwargs):
        print('Agora estou decorada.')
        funcao(*args, **kwargs)
    return slave


@master
def outra_funcao(msg):
    print(msg)


outra_funcao('Olá, eu sou o Italo.')

print('-----------------------------------------------------')

from time import time, sleep


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultao = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\nA função {funcao.__name__} levou {tempo:.2f}ms para executar.')
    return interna


@velocidade
def demora():
    for x in range(1000):
        print(f'{x},', end='')


demora()
