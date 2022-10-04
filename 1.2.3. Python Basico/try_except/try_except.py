"""
Try - Except
"""

try:
    a = 1/0
except NameError as erro:
    print(f'Erro: {erro}')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou erro de chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    print('Seu codico foi executado com sucesso.')
    print(a)
finally:
    a = ''  # Posso usar o Finllay para criar um novo valor para a variavel para que não tenha erro.
    print('Finalmente.')

print(a)
print('Código continua...')  # mesmo que tenha um erro dentro de try, o programa continua.
