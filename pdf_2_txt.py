# Importar as bibliotecas
import os
import PyPDF2


def conversor_pdf_txt(pasta: str, arquivo: str):
    """Função responsável por extrair as linhas do arquivo PDF e escrevê-las num arquivo TXT."""

    # Selecionar o arquivo infomado
    # arquivo_usado = ''
    # for doc in os.listdir(pasta):
    #     if doc == f'{arquivo}':
    #         arquivo_usado = doc

    # Indicar os caminhos do arquivo TXT e do caminho do PDF
    caminho_saida = 'txt_temp/txt_temp.txt'
    caminho_completo = f'{pasta}/{arquivo}'

    # Abrir o PDF
    pdf = open(caminho_completo, 'rb')

    # Ler o PDF
    leitor_pdf = PyPDF2.PdfReader(pdf)

    # Número de páginas do arquivo PDF
    paginas = len(leitor_pdf.pages)

    # Escrever as linhas do arquivo PDF no arquivo TXT
    for pagina in range(paginas):
        obj = leitor_pdf.pages[pagina]
        texto = obj.extract_text().split('  ')
        with open(caminho_saida, 'a') as txt:
            for linha in range(len(texto)):
                txt.write(str(texto[linha].encode('utf-8')))

    # Fechar o PDF
    pdf.close()
