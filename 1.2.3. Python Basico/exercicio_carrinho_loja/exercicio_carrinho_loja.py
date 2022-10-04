"""
Carrinho de loja online
"""
carrinho = []
print(carrinho)

carrinho.append(('Produto 1', 20.00))
carrinho.append(('Produto 2', 30.00))
carrinho.append(('Produto 3', 50.00))

print(carrinho)

total = sum([preco for produto, preco in carrinho])
print(f'O total a se pagar é R${total}')
