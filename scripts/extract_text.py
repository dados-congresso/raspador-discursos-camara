#coding: utf-8
#!/usr/bin/python3
__author__ = "Ivyna Santino"
__maintainer__ = "Ivyna Santino"
__email__ = "ivyna.alves@ccc.ufcg.edu.br"
__version__ = "1.1.0"

import PyPDF2
import sys
import re

TXT = ".txt"
PDF = ".pdf"

def calcula_numero_paginas(leitor_pdf):
	return leitor_pdf.getNumPages()

def extrai_texto_pdf(leitor_pdf, numero_paginas, arquivo_destino):
	for pagina in range(numero_paginas):
		texto_pagina = leitor_pdf.getPage(pagina).extractText()
		escreve_arquivo(arquivo_destino, texto_pagina)

def escreve_arquivo(arquivo_destino, texto_pagina):
	arquivo_destino.write(texto_pagina)

def main():
	nome_documento = "Câmara dos Deputados - Reunião de Comissão - CCJC - [09-04-2019 20h10min]"
	caminho = "../files/" + nome_documento + PDF
	obj = open(caminho, "rb")
	leitor_pdf = PyPDF2.PdfFileReader(obj, strict=False)
	
	numero_paginas = calcula_numero_paginas(leitor_pdf)
	print('Número total de páginas do documento: %d' % numero_paginas)
	print("========================================")
	
	arquivo_destino = open("../data/txt/" + nome_documento + TXT, 'w')
	extrai_texto_pdf(leitor_pdf, numero_paginas, arquivo_destino)

	print('O texto do arquivo foi extraído com sucesso!')

	arquivo_destino.close()
	obj.close()
		
if __name__ == "__main__":
    main()
