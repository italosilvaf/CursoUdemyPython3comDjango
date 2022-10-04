#        Índice
#        0123456789..........20
frase = 'o rato roeu a roupa do rei de roma.'  # Íteravel
tamanho = len(frase)
contador = 0
montandofrase = ''

letrausuario = input('Digite a letra que se deseja colocar maiúscula: ')

#  Iteração <- Iterar
while contador < tamanho:

    letra = frase[contador]
    if letra == letrausuario:
        montandofrase += letrausuario.upper()
    else:
        montandofrase += letra
    contador += 1

print(montandofrase)
