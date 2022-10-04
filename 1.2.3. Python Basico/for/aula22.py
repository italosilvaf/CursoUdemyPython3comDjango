"""
For in em python
Iterando strings com for
Função range(start=0, stop, step=1)
"""
texto = 'Italo Silva Fernandes'

for letra in texto:
    print(letra)

print('\n-------------------------------------------------------------------\n')

for numero in range(2, 15, 2):
    print(numero)

print('\n-------------------------------------------------------------------\n')

texto = 'o rato roeu a roupa do rei de roma'
print(texto)
letrausuario = input('escolha uma letra para ser maiuscula: ')
novotexto = ''

for letra in texto:
    if letra == letrausuario:
        novotexto = novotexto + letra.upper()
    else:
        novotexto += letra
print(novotexto)

print('\n-------------------------------------------------------------------\n')

texto = 'o rato roeu a roupa do rei de roma'
print(texto)
letrausuario = input('escolha uma letra para sumir: ')
novotexto = ''

for letra in texto:
    if letra == letrausuario:
        continue
    else:
        novotexto += letra
print(novotexto)

print('\n-------------------------------------------------------------------\n')

texto = 'o rato roeu a roupa do rei de roma'
print(texto)
letrausuario = input('escolha a letra que se deseja parar a frase: ')
novotexto = ''

for letra in texto:
    if letra == letrausuario:
        break
    else:
        novotexto += letra
print(novotexto)
