# Mesclador de PDFs com Python

Script que reúne vários arquivos PDF em um único documento,
automatizando uma tarefa de organização de arquivos.

## Tecnologias utilizadas

- Python
- PyPDF2

## Como executar

1. Baixe ou clone este repositório.
2. No terminal, dentro da pasta do projeto, instale a dependência:

   python -m pip install PyPDF2

3. Crie uma pasta chamada `arquivos` ao lado de `mesclador.py`.
4. Coloque os PDFs que deseja reunir dentro dessa pasta.
5. Execute:

   python mesclador.py

O resultado será salvo como `pdfs_mesclados.pdf` na pasta
de onde o comando foi executado.

## Ordem dos documentos

Os PDFs são adicionados em ordem alfabética pelo nome.

Para controlar a sequência, utilize nomes como:

- 01-introducao.pdf
- 02-conteudo.pdf
- 03-conclusao.pdf

## Limitações da versão atual

- A pasta `arquivos` precisa existir e conter os PDFs.
- Apenas arquivos com a extensão `.pdf` em letras minúsculas
  são selecionados.
- PDFs inválidos, protegidos ou problemas de acesso podem
  interromper a execução.
- Uma nova execução pode substituir o arquivo de saída anterior.

## Aprendizados

- Automação de tarefas com Python.
- Manipulação de arquivos e diretórios.
- Uso de uma biblioteca externa para trabalhar com PDFs.
- Ordenação de arquivos para controlar a montagem do documento.
