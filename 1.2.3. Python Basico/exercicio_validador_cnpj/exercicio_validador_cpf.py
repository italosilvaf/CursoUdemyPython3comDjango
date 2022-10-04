"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito

CNPJs válidos:
    04252011000110
    40688134000161
    71506168000111
    12544992000105
"""

while True:

    input_usuario1 = input('Digite um CNPJ para validarmos: ')

    def remover_caracteres(cnpj):
        cnpj = cnpj.replace('.', '')
        cnpj = cnpj.replace('-', '')
        cnpj = cnpj.replace('/', '')
        return cnpj

    input_cnpj_caracteres_removidos = remover_caracteres(input_usuario1)
    input_usuario1_lista = list(input_cnpj_caracteres_removidos)
    cnpj_digitado = []

    if input_cnpj_caracteres_removidos.isnumeric():

        for numero_str in input_usuario1_lista:
            numero_int = int(numero_str)
            cnpj_digitado.append(numero_int)

        cnpj_calculado = cnpj_digitado[:12]
        primeiro_calculo = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        segundo_calculo = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        lista_primeiro_calculo = list(zip(cnpj_calculado, primeiro_calculo))
        cnpj_primeiro_calculo_feito = [x * y for x, y in lista_primeiro_calculo]

        primeira_soma = sum(cnpj_primeiro_calculo_feito)
        formula_1 = 11 - (primeira_soma % 11)

        if formula_1 > 9:
            primeiro_digito = 0
        else:
            primeiro_digito = formula_1

        cnpj_calculado.append(primeiro_digito)

        lista_segundo_calculo = list(zip(cnpj_calculado, segundo_calculo))
        cnpj_segundo_calculo_feito = [x * y for x, y in lista_segundo_calculo]

        segunda_soma = sum(cnpj_segundo_calculo_feito)
        formula_2 = 11 - (segunda_soma % 11)

        if formula_2 > 9:
            segundo_digito = 0
        else:
            segundo_digito = formula_2

        cnpj_calculado.append(segundo_digito)

        if len(input_usuario1_lista) != 14:
            print('CNPJ inválido.')
        else:
            if cnpj_calculado == cnpj_digitado:
                print('CNPJ válido.')
            else:
                print('CNPJ inválido.')

        input_usuario2 = input('Deseja fazer outra validação? \nDigite "s" para sim e "n" para não: ')

        if 's' == input_usuario2:
            print()
            continue
        elif 'n' == input_usuario2:
            print()
            print('Programa finalizado.')
            break
        else:
            print()
            print('Não entendi seu comando.')
            print('Programa finalizado.')
            break

    else:
        print()
        print('CNPJ não contem letras.')
        print('Programa finalizado.')
        break
