"""
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamenre em cada tipo.
"""
# positivos  [01234567]
texto   =    'Italo SF'
# negativos -[87654321]

print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])
print(texto[4])
print(texto[5])
print(texto[6])
print(texto[7])

print('\n------------------------------------------------------------------\n')

print(texto[-1])
print(texto[-2])
print(texto[-3])
print(texto[-4])
print(texto[-5])
print(texto[-6])
print(texto[-7])
print(texto[-8])

print('\n------------------------------------------------------------------\n')

novo_texto0 = texto[1:5]
print(novo_texto0)

novo_texto1 = texto[-8:-3]
print(novo_texto1)

print('\n------------------------------------------------------------------\n')

# Passos

novo_texto2 = texto[0:8:2]
print(novo_texto2)

novo_texto3 = texto[-8:-1:3]
print(novo_texto3)

print('\n------------------------------------------------------------------\n')

print(len(texto))
