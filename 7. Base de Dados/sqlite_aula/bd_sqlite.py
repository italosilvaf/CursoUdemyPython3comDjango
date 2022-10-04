
import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('  # Criando Tabela
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Giovanna', 70))  # Inserindo um registro na tabela
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'Giovanna', 'peso': 70})
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'Hermelindo', 'peso': 65})
# conexao.commit()  # Inserindo os valores na bases de dados

# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',  # Atualizando um dos dados
#                {'nome': 'Violeta', 'id': 5}
#                )
# conexao.commit() # Inserindo os valores na bases de dados

# cursor.execute('DELETE FROM clientes WHERE id=:id',  # Deletando um dos dados
#                {'id': 5}
#                )
# conexao.commit() # Inserindo os valores na bases de dados

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    identificador, nome, peso = linha

    print(identificador, nome, peso)

print('\n--------------------------------------------------------------------------------------------------------\n')

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',  # Selecionando parte específica da base de dados
               {'peso': 60})

for linha in cursor.fetchall():
    nome, peso = linha

    print(nome, peso)

cursor.close()
conexao.close()
