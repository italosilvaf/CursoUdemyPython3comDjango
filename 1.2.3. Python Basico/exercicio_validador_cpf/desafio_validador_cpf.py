"""
Validador de cpf
"""
while True:
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:9]
    decrescente = 10
    total = 0

    for indice in range(19):
        if indice > 8:
            indice -= 9

        total += int(novo_cpf[indice]) * decrescente
        decrescente -= 1

        if decrescente < 2:
            decrescente = 11

            digito = 11 - (total % 11)

            if digito > 9:
                digito = 0
            total = 0
            novo_cpf += str(digito)

    if cpf == novo_cpf:
        print('O CPF que você digitou é valido!!!')
    else:
        print('O CPF que você digitou não é valido!!!')
    break
