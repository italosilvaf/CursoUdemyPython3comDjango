import json

with open('texto.json', 'r') as file:
    dicionario_json = file.read()
    dicionario_json = json.loads(dicionario_json)

for key, valor in dicionario_json.items():
    print(key, valor)
    for key1, valor1 in valor.items():
        print(key1, valor1)
