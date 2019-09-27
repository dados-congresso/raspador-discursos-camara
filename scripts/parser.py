#!/usr/bin/python3
__author__ = "Pedro espíndula"
__maintainer__ = "Pedro espíndula"
__email__ = "joaopedro.jpse@gmail.com"
__credits__ = [("Ivyna Santino", "ivyna.alves@ccc.ufcg.edu.br")]
__version__ = "1.0.1"

import re

def arquivoParaString(caminho):
    resultado = ""

    with open(caminho, 'r+') as arquivo:
        for linha in arquivo:
            resultado += linha

    return resultado

def escreveListaEmCSV(lista, caminho,separator = "|", headers = None):
    with open(caminho, "w+") as arquivo:
        if headers:
            arquivo.write(separator.join(headers) + "\n")
        for linhaCsv in lista:
            arquivo.write(separator.join(linhaCsv) + "\n")

def partidoEstadoFala(linha):
    regexInfo = "([aA-zZ]*\/?[aA-zZ]*)\s-\s([A-Z]{2}).*\)\s-\s(.*)"

    resultado = re.search(regexInfo, linha)

    if resultado:
        resultado = resultado.groups()
    else:
        print(linha)
        regexSecondTry = "\(([^()]+)\)\s-\s(.*)"
        resultado = re.search(regexSecondTry, linha)

        if resultado:
            resultado = ("N/A", "N/A", resultado.groups()[1]);

    return resultado


def falante(linha):
    regexFalante = "[AO]\sSRA?.\s(.*)"

    resultado = re.search(regexFalante, linha)

    if resultado:
        resultado = resultado.groups()[0].strip()
    elif linha == "(DO PODER EXECUTIVO)":
        resultado = "PODER EXECUTIVO"

    return resultado

def parteFala(linha):
    return not (
        linha.isupper() or
        linha.isdigit() or
        linha == "/" or
        linha.startswith("Sessão de:") or
        linha.startswith("Notas Taquigráficas"))



def parseSessao(sessao, presidente):
    resultado = []
    falanteAtual = ""
    fala = ""

    for linha in sessao.split("\n"):
        if falante(linha):
            if falanteAtual and fala:
                if falanteAtual == "PRESIDENTE":
                    falanteAtual = presidente.upper()

                infos = (falanteAtual.strip().replace(",", ""), partidoAtual.strip(), estadoAtual.strip(), fala.strip())
                fala = ""
                partidoAtual = "N/A"
                estadoAtual = "N/A"
                resultado.append(infos)

            falanteAtual = falante(linha)

        if falanteAtual:
            if partidoEstadoFala(linha):
                partidoAtual, estadoAtual, fala = partidoEstadoFala(linha)
            elif parteFala(linha):
                fala += " " + linha

    return resultado

def main():
    nome_documento = "Câmara dos Deputados - Reunião de Comissão - CCJC - [09-04-2019 20h10min].txt"
    caminho = "../data/txt/" + nome_documento
    presidente_sessao = "Felipe Francischini"
    sessao = arquivoParaString(caminho)
    parsed = parseSessao(sessao, presidente_sessao)
    escreveListaEmCSV(parsed, "../data/previdencia_ccjc_09-04-20h.csv", headers=["autor", "partido", "uf", "discurso"])

if __name__ == "__main__":
    main()