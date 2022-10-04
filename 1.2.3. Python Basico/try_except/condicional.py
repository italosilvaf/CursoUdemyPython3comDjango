"""
Condicional
"""


def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


numero = converte_numero(input('Digite um número: '))

if numero is not None:
    resultado = numero * 2
    print(f'{numero} * 2 = {resultado}')
else:
    print('Erro: Você não digitou um núemro.')
