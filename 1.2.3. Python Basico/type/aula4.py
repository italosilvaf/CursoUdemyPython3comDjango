"""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - intreiro - 123456 10 20 -100 -150000 89456123
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/False 10 == 10
"""
print(type('Italo'))

num = str('7')
print(num, type(num))

print("------------------------------------------------------------------")

print(7, type(7))
print(0.7, type(0.7))

print("------------------------------------------------------------------")

print(10 == 10, type(10 == 10))
print('Italo' == 'Italo', type('Italo' == 'Italo'))
print(bool())
print(bool(0))
print(bool(1))

print("------------------------------------------------------------------")

"""
Exercício
"""

# String: Nome
print('Italo', type('Italo'))

# Idade: int
print(20, type(20))

# Altura: float
print(1.83, type(1.83))

# É maior de idade: bool
print(20 >= 18, type(20 >= 18))
