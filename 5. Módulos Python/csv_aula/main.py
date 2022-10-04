"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv

with open('clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)
    next(dados)

    for dado in dados:
        print(dado)

print('\n----------------------------------------------------------------------------------------------------------\n')

with open('clientes.csv', 'r') as arquivo:
    dados = csv.DictReader(arquivo)

    for dado in dados:
        print(f"{dado['Nome']} {dado['Sobrenome']} E-mail: {dado['E-mail']} Telefone: {dado['Telefone']}")

print('\n----------------------------------------------------------------------------------------------------------\n')

with open('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]

with open('clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3],
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
