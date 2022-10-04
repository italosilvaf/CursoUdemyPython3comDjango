"""
While / Else
contadores
acumuladores
"""

contador = int(input('Digite um número menor ou igual que 100, para ser contado apartir dele até 100: '))
acumulador = int(input('Digite um valor de acomulador: '))

while contador <= 100:
    print(contador, acumulador)
    contador += 1
    acumulador = acumulador + contador

    if contador > 100:
        print('Acabou.')
        break

else:
    print('Você deveria ter digitado um número menor ou igual a 100. ')
