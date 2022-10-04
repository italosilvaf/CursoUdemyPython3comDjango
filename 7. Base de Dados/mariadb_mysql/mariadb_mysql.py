
import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        print('Conexão fechada')
        conexao.close()


# with conecta() as conexao:  # adicionando um valor na base de dados
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#         cursor.execute(sql, ('Italo', 'Fernandes', '20', '72'))
#         conexao.commit()

# with conecta() as conexao:  # adicionando varios valores na base de dados
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#
#         dados = [
#             ('MURIEL', 'SILVA', '19', '55'),
#             ('ROSE', 'SILVA', '19', '55'),
#             ('JOSE', 'SILVA', '19', '55'),
#         ]
#
#         cursor.executemany(sql, dados)
#         conexao.commit()

# with conecta() as conexao:  # deletando um valor da base de dados
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         conexao.commit()

# with conecta() as conexao:  # deletando varios valores da base de dados
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()

# with conecta() as conexao:  # deletando varios valores da base de dados entre um range (dos que tem id entre 10 e 12)
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10, 12))
#         conexao.commit()

# with conecta() as conexao:  # Editando um valor na base de dados
#     with conexao.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('Italo', 5))
#         conexao.commit()

with conecta() as conexao:  # Seleciona os dados da base de dados
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
