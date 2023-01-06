from calculadora import soma0, soma1

print("\n----------------------------------------------------------\n")

print(soma0(10, 20))
print(soma0(-10, 20))
print(soma0(10, -20))
print(soma0(1.5, 2.5))

print("\n----------------------------------------------------------\n")

try:
    print(soma0('15', 15))
except TypeError as e:
    print('Conta inválida:')
    print(e)

print("\n----------------------------------------------------------\n")

try:
    print(soma1('15', 15))
except AssertionError as e:
    print('Conta inválida:')
    print(e)

print("\n----------------------------------------------------------\n")

try:
    print(soma1(15, '15'))
except AssertionError as e:
    print('Conta inválida:')
    print(e)

print("\n----------------------------------------------------------\n")
