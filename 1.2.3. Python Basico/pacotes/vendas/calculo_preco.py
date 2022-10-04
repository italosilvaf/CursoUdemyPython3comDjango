"""
Calcilos em preços
"""
from pacotes.vendas.formata.preco import real


def aumeta_preco(preco, porcentagem, formata_preco=False):
    preco_aumentado = preco + (preco * porcentagem / 100)

    if formata_preco:
        preco_aumentado_formatado = real(preco_aumentado)
        return preco_aumentado_formatado
    else:
        return preco_aumentado


def reduz_preco(preco, porcentagem, formata_preco=False):
    preco_reduzido = preco - (preco * porcentagem / 100)

    if formata_preco:
        preco_reduzido_formatado = real(preco_reduzido)
        return preco_reduzido_formatado
    else:
        return preco_reduzido
