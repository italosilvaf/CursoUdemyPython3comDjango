"""
Sobreposição de Membros
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__

    def falar(self):
        print(f'{self.nome_classe} falando.')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_classe} comprando.')

    def falar(self):
        print('Estou em Cliente')


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)  # ou Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        super().falar()  # ou Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')
        print(f'Estou em ClienteVip')

