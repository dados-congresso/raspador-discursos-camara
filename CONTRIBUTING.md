# Contribuindo para o Raspador de discursos de deputados federais

Existem algumas maneiras de contribuir com este projeto. Você pode contribuir atualizando a documentação, sugerindo melhorias ou melhorando a base de códigos. 

Alguns exemplos: adicionar testes a base de códigos atual, alterar o README para incluir algo novo que você acha necessario ou sugerir uma melhoria que não se encontra no aplicativo.

## Código de conduta

Nós acreditamos e seguimos as regras dispostas em nosso código de conduta para garantir um ambiente em que todos se sintam bem-vindos. Ao participar do projeto, seja submetendo sugestoes ou melhorias, você concorda com o nosso [código de conduta](CODE_OF_CONDUCT.md). Recomendamos que você o leia antes de participar.

## Criando uma issue

O GitHub oferece uma ferramenta, dentre outras, para buscar confirmação de mudanças no projeto que você gostaria de propor através de um _pull request_. Uma forma elegante de iniciar uma conversa conosco antes de tocar na base de código ou documentação.

Se você encontrou algum bug ou quer adicionar uma nova funcionalidade, siga as seguintes instruções.

Se depois de verificar a lista das issues (abertas e fechadas), tem certeza de que se trata de algo novo ou não reportado anteriormente, crie uma nova issue no GitHub. Lembre-se de adicionar o máximo de informações relevantes o possível para que pelo menos sejamos capazes de reproduzi-lo. 

Em se tratando de uma nova funcionalidade, adicione informações relevantes sobre uma feature que você gostaria que estivesse no aplicativo.

## Contribuindo com a base de código

### Requisitos

- Conta do GitHub
- [Git](https://git-scm.com/downloads) instalado no seu computador.
- [Python 3.6](https://www.python.org/downloads/).

### Configurando o projeto local

1. Crie um fork do projeto
2. Clone o projeto:

```bash
git clone https://github.com/<SEU_USUARIO_GITHUB>/raspador-discursos-camara
```
ou
```bash
git clone https://github.com/<SEU_USUARIO_GITHUB>/raspador-discursos-camara.git
```

Dentro do diretório _raspador-discursos-camara_, se encontra o código fonte do projeto.

### Criando um branch e adicionando suas alterações

Assim que estiver satisfeito com suas alterações, crie um novo branch e as adicione.

```bash
git checkout -b nome-do-meu-branch
```
Com o branch criado, adicione as alterações com os comandos abaixo:

```bash
git add .
git commit -m "comentario sobre o que foi alterado"
```
Envie suas alterações executando:

```bash
git push origin nome-do-meu-branch
```
Pronto. As suas alterações foram enviadas para o seu fork do projeto.

### Criando um pull request

Como essa parte e mais visual, [siga as instruções](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork) para criar um pull request do seu fork para o branch master do nosso projeto.

Aguarde pela avaliação da pull request.