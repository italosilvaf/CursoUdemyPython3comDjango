"""
while_calculadora em Python
utilizado para realizar ações enquanto
uma consição for verdadeira.
"""
resposta1 = input('Vamos fazer uma operação matemática ? ')

if 's' in resposta1:

    while True:

        num1 = input('Digite o primeiro número: ')
        num2 = input('Digite o segundo número: ')
        operador = input('Escolha o tipo de operação: ')

        if num1.isnumeric() and num2.isnumeric():

            num1 = int(num1)
            num2 = int(num2)

            if operador == '+':
                resultado = num1 + num2
                print(f'{num1} + {num2} = {resultado}\n')

                resposta3 = input('Deseja fazer outra operação? ')
                if 's' in resposta3:
                    continue
                elif 'n' in resposta3:
                    print('Ok, obrigado. ')
                    break
                else:
                    print('Não conpreendi.')

            elif operador == '-':
                resultado = num1 - num2
                print(f'{num1} - {num2} = {resultado}\n')

                resposta3 = input('Deseja fazer outra operação? ')
                if 's' in resposta3:
                    continue
                elif 'n' in resposta3:
                    print('Ok, obrigado. ')
                    break
                else:
                    print('Não conpreendi.')

            elif operador == '*':
                resultado = num1 * num2
                print(f'{num1} * {num2} = {resultado}\n')

                resposta3 = input('Deseja fazer outra operação? ')
                if 's' in resposta3:
                    continue
                elif 'n' in resposta3:
                    print('Ok, obrigado. ')
                    break
                else:
                    print('Não conpreendi.')

            elif operador == '/':
                resultado = num1 / num2
                print(f'{num1} / {num2} = {resultado}\n')

                resposta3 = input('Deseja fazer outra operação? ')
                if 's' in resposta3:
                    continue
                elif 'n' in resposta3:
                    print('Ok, obrigado. ')
                    break
                else:
                    print('Não conpreendi.')

            else:
                print('Operador inválido.')

                resposta3 = input('Deseja fazer outra operação? ')
                if 's' in resposta3:
                    continue
                elif 'n' in resposta3:
                    print('Ok, obrigado. ')
                    break
                else:
                    print('Não conpreendi.')

        else:
            print('Você precisa digitar numero! \n')

            resposta3 = input('Deseja fazer outra operação? ')
            if 's' in resposta3:
                continue
            elif 'n' in resposta3:
                print('Ok, obrigado. ')
                break
            else:
                print('Não conpreendi.')

elif 'n' in resposta1:
    print('Ok, obrigado. ')

else:
    print('Não conpreendi.')
