from classes import Cliente

cliente1 = Cliente('Italo', 20)
cliente1.insere_endereco('Patos de Minas', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Giovanna', 21)
cliente2.insere_endereco('Salvador', 'BA')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Hermelindo', 80)
cliente3.insere_endereco('São paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()

print('##############################################')
