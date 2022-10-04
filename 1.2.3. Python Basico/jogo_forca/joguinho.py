"""
JOGO DA FORCA:
"""

print('JOGO DA FORCA\n')

while True:

    palavra = input('Digite uma palavra para ser adivinhada: ').lower()
    chances = 7
    digitadas = []
    digitadas_erradas = []
    print('\n' * 1000)

    while True:

        if chances <= 0:
            print('Você Perdeu !!! :( ')
            print(f'A palavra a ser adivinhada era "{palavra}".')
            break
        letra = input('\nDigite uma letra: ')

        if len(letra) > 1:
            print('Só é permitido digitar uma letras por vez!!! ')
            continue

        digitadas.append(letra)

        if letra in palavra:
            print(f'\nPARABENS, a letras "{letra}" existe na palavra a ser adivinhada.')
        else:
            print(f'\nAFFFFFFF a letras "{letra}" não existe na palavra a ser adivinhada.')

        palavra_temporaria = ''
        for letra_secreta in palavra:
            if letra_secreta in digitadas:
                palavra_temporaria += letra_secreta
            else:
                palavra_temporaria += '*'

        if palavra_temporaria == palavra:
            print(f'Que legal, VOCÊ GANHOU!!! A palavra a ser adivinhada era "{palavra}". :)')
            break
        else:
            print(f'A palavra a ser adivinhada está assim: {palavra_temporaria}')

        if letra not in palavra:
            chances -= 1

            if letra not in digitadas_erradas:
                digitadas_erradas += letra

        print(f'As letras digitadas erradas são: {digitadas_erradas}')

        if chances > 0:
            print(f'Você ainda tem {chances} chances.')

    denovo = input('\nVocê deseja jogar novamente? ')

    if 's' in denovo:
        print('\nENTÃO VAMOS COMEÇAR NOVAMENTE: \n')
        continue
    elif 'n' in denovo:
        print('Obrigado por jogar!!!')
        break
    else:
        print('Não conpreendi.')
        break
