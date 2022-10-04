
import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')

    # agenda.inserir('Italo', '(34) 99212-7233')  # Inserindo valores na base de dados
    # agenda.inserir('Giovanna', '(34) 98412-1851')
    # agenda.inserir('Hermelindo', '(34) 3823-2167')
    # agenda.inserir('Violeta', '(34) 91234-1234')
    agenda.inserir('João', '(34) 91234-4567')
    agenda.inserir('João Paulo', '(35) 91234-4567')
    agenda.inserir('João Vitor', '(36) 91234-4567')
    agenda.inserir('Maria João', '(37) 91234-4567')
    agenda.inserir('Joãozinho', '(38) 91234-4567')
    agenda.inserir('Italo João Calazans', '(39) 91234-4567')

    # agenda.editar('Joãozinho', '(34) 3823-2329', 20)  # Editando um valor na base de dados

    # agenda.excluir(20)  # Excluindo valor na base de dados

    agenda.listar()

    print('\n----------------------------------------------------------------------------------------\n')
    agenda.buscar('João')  # Buscando no banco de dados determinado valor
    print('\n----------------------------------------------------------------------------------------\n')



