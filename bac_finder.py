# Importar as bibliotecas
import sys
from PySide2.QtWidgets import QFileDialog, QMessageBox
from interface_grafica.interface_python import recursos
from interface_grafica.interface_python.interface import *

# Importar os módulos criados
from pdf_2_txt import conversor_pdf_txt
from extrair_bacterias import extrair_bacterias


class BacFinder(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, parent=None)

        # Carregar o arquivo da GUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Título do App
        self.setWindowTitle('BacFinder')

        # Deixar bloqueado os botões
        self.ui.botao_txt.setDisabled(True)
        self.ui.botao_salvar.setDisabled(True)
        self.ui.botao_excluir.setDisabled(True)
        self.ui.botao_executar.setDisabled(True)

        # Abrir o arquivo PDF
        self.ui.botao_pdf.clicked.connect(self.abrir_pdf)

        # Criar o arquivo TXT das bactérias
        self.ui.botao_txt.clicked.connect(self.criar_txt_bacterias)

        # Executar as funções
        self.ui.botao_executar.clicked.connect(self.executar)

        # Limpar tudo
        self.ui.botao_excluir.clicked.connect(self.excluir)

        # Salvar as bactérias no arquivo TXT
        self.ui.botao_salvar.clicked.connect(self.salvar)

    def abrir_pdf(self):
        """Função responsável por abrir o arquivo PDF."""

        # Abrir o arquivo PDF
        caminho = QFileDialog.getOpenFileName()[0]

        # Obter o caminho até antes do arquivo PDF
        caminho_split = caminho.split('/')[:-1]
        self.caminho_pdf = '/'.join(caminho_split)

        # Obter somente nome do arquivo
        self.arquivo_pdf = caminho.split('/')[-1]

        # Colocar o nome do arquivo na tela
        self.ui.linha_arquivo_pdf.setText(self.arquivo_pdf)

        # Se houver o nome na tela, liberar o botão para criar o arquivo TXT
        if self.arquivo_pdf != '':
            self.ui.botao_txt.setDisabled(False)

    def criar_txt_bacterias(self):
        """Função responsável por criar o arquivo TXT das bactérias."""

        # Criar o arquivo TXT
        caminho = QFileDialog.getSaveFileName()[0]

        # Obter o caminho até antes do arquivo PDF
        caminho_split = caminho.split('/')[:-1]
        self.caminho_txt = '/'.join(caminho_split)

        # Obter somente o nome do arquivo criado
        self.arquivo_txt = caminho.split('/')[-1]

        # Colocar o nome do arquivo na tela
        self.ui.linha_arquivo_bacterias.setText(f'{self.arquivo_txt}.txt')

        # Se houver o nome na tela, liberar o botão para executar as funções
        if self.arquivo_txt != '':
            self.ui.botao_executar.setDisabled(False)

    def executar(self):
        """Função responsável por executar as funções."""

        # Obter o nome das bactérias
        bacterias = self.ui.linha_bacterias.text().replace(' ', '').split(',')

        # Executar a conversão de PDF para TXT
        conversor_pdf_txt(self.caminho_pdf, self.arquivo_pdf)

        # Escrever quais foram as bactérias encontradas
        lista_bacterias = extrair_bacterias(bacterias)
        for bacteria in lista_bacterias:
            self.ui.lista_bacterias.appendPlainText(bacteria)

        # Liberar os botões de salvar e excluir
        self.ui.botao_salvar.setDisabled(False)
        self.ui.botao_excluir.setDisabled(False)

    def excluir(self):
        """Função responsável por limpar todos os campos
        caso não haja nenhuma bactéria encontrada."""

        # Limpar o campo de pesquisa do arquivo PDF
        self.ui.linha_arquivo_pdf.setText('')

        # Limpar o campo de criação do arquivo TXT
        self.ui.linha_arquivo_bacterias.setText('')

        # Limpar o campo de pesquisa das bactérias
        self.ui.linha_bacterias.setText('')

        # Limpar o campo onde são mostradas as bactérias
        self.ui.lista_bacterias.setPlainText('')

        # Bloquear os botões
        self.ui.botao_txt.setDisabled(True)
        self.ui.botao_salvar.setDisabled(True)
        self.ui.botao_excluir.setDisabled(True)
        self.ui.botao_executar.setDisabled(True)

    def salvar(self):
        """Função responsável por salvar tudo o que estiver no QPlainTextEdit."""

        # Obter as bactérias
        bacterias = self.ui.lista_bacterias.toPlainText()

        # Salvar as bactérias num arquivo TXT
        caminho = f'{self.caminho_txt}/{self.arquivo_txt}.txt'
        with open(caminho, 'w') as txt:
            txt.write(bacterias)

        # Limpar tudo depois de salvo as bactérias no arquivo TXT
        self.excluir()

        # Mensagem de que o arquivo foi criado com sucesso
        QMessageBox.information(self,
                                'Sucesso',
                                f'Arquivo {self.arquivo_txt}.txt criado com sucesso!')


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')
    bac = BacFinder()
    bac.show()
    sys.exit(app.exec_())
