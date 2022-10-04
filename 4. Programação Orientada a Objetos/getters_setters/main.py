from produto import Produto

produto1 = Produto('CAMISETA', 50)
produto1.desconto(10)
print(produto1.nome, produto1.preco)

produto2 = Produto('CaNeCa', 'R$15,00')
produto2.desconto(10)
print(produto2.nome, produto2.preco)

produto3 = Produto('bermuda', 40.00)
produto3.desconto(10)
print(produto3.nome, produto3.preco)

produto4 = Produto('Calça', '100,00')
produto4.desconto(10)
print(produto4.nome, produto4.preco)

produto5 = Produto('TEnis', 'R$250')
produto5.desconto(10)
print(produto5.nome, produto5.preco)

produto6 = Produto('bLusa', 'R$120.00')
produto6.desconto(10)
print(produto6.nome, produto6.preco)
