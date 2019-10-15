## Raspador de discursos de deputados federais

Scripts que fazem a raspagem dos textos dispostos nas notas taquigráficas de discursos de parlamentares na Câmara em sessões políticas.

#### Executando
O repositório contém um exemplo do pdf em ``files/exemplo_previdencia.pdf``. Para executar o código basta executar os seguintes comandos:

```bash
$ git clone https://github.com/https://github.com/dados-congresso/raspador-discursos-camara.git

$ cd raspador-discursos-camara

$ python3.6 scripts/raspador.py 
```

Como resultado, será gerado um ``exemplo.csv`` com as seguintes colunas:

* nome: nome do parlamentar
* partido: sigla do partido do parlamentar
* uf: sigla do estado do parlamentar
* discurso: texto taquigrafado

Vale ressaltar que cada linha da base de dados gerada é a sequência de discursos da sessão, seja ela plenário ou comissão de uma determinada proposição. Como exemplo, baixei das notas taquigráficas uma sessão pertencente a CCJC referente a PEC 06/2019 ou mais conhecida como Nova reforma da previdência.

#### Estrutura
```bash
scripts/
   |_ raspador.py 
   |_ extract_texto.py
   |_ parser.py
   
files/
  |_ exemplo_previdencia.pdf
  
data/
  |_ arquivo_parseado.csv
  |_ txt/
      |_ texto_previdencia.txt
```

#### Como contribuir?

Caso você deseje contribuir com o nosso projeto, leia o [CONTRIBUTING.md](CONTRIBUTING.md).
