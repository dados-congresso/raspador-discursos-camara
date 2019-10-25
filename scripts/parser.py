#!/usr/bin/python3
__author__ = "Pedro Espíndula"
__maintainer__ = "Pedro Espíndula"
__email__ = "joaopedro.jpse@gmail.com"
__credits__ = [("Ivyna Santino", "ivyna.alves@ccc.ufcg.edu.br")]
__version__ = "1.0.1"

import re

PARTIDO_ESTADO_DISCURSO = "([aA-zZ]*\/?[aA-zZ]*)\s-\s([A-Z]{2}).*\)\s-\s(.*)"
PARTIDO_ESTADO_DISCURSO_ALTERNATIVO = "\(([^()]+)\)\s-\s(.*)"
ORADOR = "[AO]\sSRA?.\s(.*)"
QUEBRA_LINHA = "\n"

def converte_arquivo_para_string(caminho):
    resultado = ""
    with open(caminho, 'r+') as arquivo:
        for linha in arquivo:
            resultado += linha

    return resultado

def escreve_lista_em_csv(lista, caminho, separador = "|", cabecalho = None):
    with open(caminho, "w+") as arquivo:
        if (cabecalho):
            arquivo.write(separador.join(cabecalho) + QUEBRA_LINHA)
        for linha_csv in lista:
            arquivo.write(separador.join(linha_csv) + QUEBRA_LINHA)

def define_partido_estado_discurso(linha):
    resultado = re.search(PARTIDO_ESTADO_DISCURSO, linha)

    if (resultado):
        resultado = resultado.groups()
    else:
        resultado = re.search(PARTIDO_ESTADO_DISCURSO_ALTERNATIVO, linha)
        if (resultado):
            resultado = ("N/A", "N/A", resultado.groups()[1])

    return resultado

def define_orador(linha):
    resultado = re.search(ORADOR, linha)

    if (resultado):
        resultado = resultado.groups()[0].strip()
    elif (linha == "(DO PODER EXECUTIVO)"):
        resultado = "PODER EXECUTIVO"

    return resultado

def identifica_cabecalho(linha):
    return (
        linha.isupper() or
        linha.isdigit() or
        (linha == "/") or
        linha.startswith("Sessão de:") or
        linha.startswith("Notas Taquigráficas")
    )

def identifica_presidente_sessao(orador_atual, presidente_sessao):
    orador = orador_atual
    if (orador_atual == "PRESIDENTE"):
        orador = presidente_sessao.upper()
        
    return orador

def parse_sessao(sessao, presidente_sessao):
    orador_atual, discurso, partido_atual, estado_atual = "", "", "", ""
    resultado = []

    for linha in sessao.split(QUEBRA_LINHA):
        if (orador_atual):
            if (define_partido_estado_discurso(linha)):
                partido_atual, estado_atual, discurso = define_partido_estado_discurso(linha)
            elif (not identifica_cabecalho(linha)):
                discurso += " " + linha

        if (define_orador(linha)):
            if (orador_atual and discurso):
                orador_atual = identifica_presidente_sessao(orador_atual, presidente_sessao)
                infos = (orador_atual.strip().replace(",", ""), partido_atual.strip(), estado_atual.strip(), discurso.strip())
                partido_atual, estado_atual, discurso = "N/A", "N/A", ""
                resultado.append(infos)

            orador_atual = define_orador(linha)

    return resultado

def main():
    nome_documento = "Câmara dos Deputados - Reunião de Comissão - CCJC - [09-04-2019 20h10min].txt"
    caminho = "../data/txt/" + nome_documento
    presidente_sessao_sessao = "Felipe Francischini"
    print("============================")
    print("Iniciando parser")
    print("============================")
    sessao = converte_arquivo_para_string(caminho)
    parsed = parse_sessao(sessao, presidente_sessao_sessao)
    escreve_lista_em_csv(parsed, "../data/previdencia_ccjc_09-04-20h.csv", cabecalho=["autor", "partido", "uf", "discurso"])
    print("O parser foi realizado com sucesso!")

if __name__ == "__main__":
    main()