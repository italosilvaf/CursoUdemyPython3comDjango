"""
Gerador de CNPJ
"""

from time import sleep
import cnpj

while True:
    novo_cnpj = cnpj.gera()
    formatado = cnpj.formata(novo_cnpj)
    print(formatado)
    sleep(1)
