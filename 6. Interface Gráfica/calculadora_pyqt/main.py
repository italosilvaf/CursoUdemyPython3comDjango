
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora do ItaloSF')
        self.setFixedSize(400, 400)  # Esse comando serve para travar o tamanho da janlinha.
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        """
        Display
        """
        self.display = QLineEdit()  # Criando um display
        self.grid.addWidget(self.display, 0, 0, 1, 5)  # serve tamanho e lugar onde o display vai ficar
        self.display.setDisabled(True)  # Comando para não poder digitar no display
        self.display.setStyleSheet(
            '* {background: white; color: #000; font-size: 30px;}'  # Mudando o design da janelinha
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # Display aumenta para o tamnho vazio

        """
        Botões
        """
        # Linha 1
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)  # Adicionei o botão '7'
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)  # Adicionei o botão '8'
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)  # Adicionei o botão '9'
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)  # Adicionei o botão '+'
        self.add_btn(QPushButton('C'), 1, 4, 1, 1,
                     lambda: self.display.setText(''),  # Comando de Limpar o display
                     '* {background: #FF6347; color: #fff; font-weight: 7000}'  # Design da botão clear (cor em html)
                     )  # Adicionei o botão 'Clear = Limpar'

        # Linha 2
        self.add_btn(QPushButton('4'), 2, 0, 1, 1)  # Adicionei o botão '4'
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)  # Adicionei o botão '5'
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)  # Adicionei o botão '6'
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)  # Adicionei o botão '-'
        self.add_btn(QPushButton('←'), 2, 4, 1, 1,
                     lambda: self.display.setText(self.display.text()[:-1]),  # Comando de Apagar no display
                     '* {background: #2E8B57; color: #fff; font-weight: 7000}'  # Design da botão apagar (cor em html)
                     )  # Adicionei o botão 'Apagar'

        # Linha 3
        self.add_btn(QPushButton('1'), 3, 0, 1, 1)  # Adicionei o botão '1'
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)  # Adicionei o botão '2'
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)  # Adicionei o botão '3'
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)  # Adicionei o botão '/'
        self.add_btn(QPushButton('='), 3, 4, 2, 1,
                     self.eval_igual,  # Setando que metodo o botão vai executar
                     '* {background: #4682B4; color: #fff; font-weight: 7000}'  # Design da botão igual (cor em html)
                     )  # Adicionei o botão '='

        # Linha 4
        self.add_btn(QPushButton('.'), 4, 0, 1, 1)  # Adicionei o botão '.'
        self.add_btn(QPushButton('0'), 4, 1, 1, 2)  # Adicionei o botão '0'
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)  # Adicionei o botão '*'

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):  # Método que adiciona botão
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # Botão aumenta para o tamnho vazio

    def eval_igual(self):  # Método de igual
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta Inválida.')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()


