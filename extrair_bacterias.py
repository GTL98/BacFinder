# Importar as bibliotecas
import os
import re


def extrair_bacterias(bacterias: list):
    """Função responsável por extrair as bactérias com operação regex do arquivo TXT que
    contêm todas as linhas do arquivo PDF."""

    # Indicar os caminhos do arquivo TXT com as linhas e o TXT das bactérias
    caminho_completo = 'txt_temp/txt_temp.txt'

    # Lista com as bactérias encontradas
    lista_bacterias = []

    # Abrir o arquivo TXT com as informações do PDF
    with open(caminho_completo, 'r') as txt:
        conteudo = txt.readlines()
        for linha in conteudo:
            for bacteria in bacterias:
                bac_re = re.findall(fr'{bacteria}\s[a-z]+', linha)
                for bac in bac_re:
                    if bac not in lista_bacterias:
                        lista_bacterias.append(bac)

    # Com o documento das bactérias feito, excluir o arquivo temporário
    # TXT com as informações do PDF
    os.remove(caminho_completo)

    return lista_bacterias
