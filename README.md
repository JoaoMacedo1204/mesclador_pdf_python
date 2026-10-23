# Mesclador de PDFs com Python

Script em Python que reúne vários arquivos PDF em um único
documento, automatizando a organização de documentos.

## Funcionalidades

- Mesclagem dos PDFs em ordem pelo nome dos arquivos.
- Reconhecimento de extensões como `.pdf`, `.PDF` e `.Pdf`.
- Verificação da existência da pasta de entrada.
- Aviso quando nenhum PDF é encontrado.
- Verificação para evitar substituir um resultado anterior.
- Mensagem com a quantidade de PDFs mesclados.

## Tecnologias utilizadas

- Python 3
- PyPDF2
- Módulo `os` da biblioteca padrão do Python

## Como executar

### 1. Baixe o projeto

Baixe os arquivos ou clone o repositório:

```bash
git clone https://github.com/JoaoMacedo1204/mesclador_pdf_python.git
cd mesclador_pdf_python
```

### 2. Instale a dependência

```bash
python -m pip install PyPDF2==3.0.1
```

O script utiliza `PdfMerger`, disponível nessa versão da biblioteca.

### 3. Prepare os documentos

Crie uma pasta chamada `arquivos` dentro da pasta do projeto
e coloque nela os PDFs que deseja mesclar.

Exemplo de organização:

```text
mesclador_pdf_python/
├── arquivos/
│   ├── 01-introducao.pdf
│   ├── 02-conteudo.pdf
│   └── 03-conclusao.pdf
├── mesclador.py
└── README.md
```

### 4. Execute o script

No terminal, dentro da pasta do projeto, execute:

```bash
python mesclador.py
```

O resultado será salvo como `pdfs_mesclados.pdf` nessa mesma pasta.

Exemplo de mensagem:

```text
3 PDFs mesclados com sucesso!
Resultado salvo em "pdfs_mesclados.pdf".
```

## Ordem dos documentos

O script ordena os PDFs pelo nome antes de mesclá-los.

Para controlar a sequência, utilize prefixos numéricos
com a mesma quantidade de dígitos:

- `01-introducao.pdf`
- `02-conteudo.pdf`
- `03-conclusao.pdf`

Arquivos com outras extensões e subpastas são ignorados.
O script não procura PDFs dentro das subpastas.

## Verificações

O programa encerra com uma mensagem quando:

- A pasta `arquivos` não existe.
- Nenhum arquivo com extensão PDF é encontrado.
- Já existe um arquivo ou pasta chamado `pdfs_mesclados.pdf`
  no destino.

Para gerar outro resultado, renomeie ou mova o arquivo de saída
anterior antes de executar novamente.

## Limitações atuais

- O programa deve ser executado dentro da pasta do projeto.
- A seleção verifica a extensão dos arquivos, não a validade
  de seu conteúdo.
- PDFs corrompidos, protegidos por senha ou problemas de permissão
  podem interromper a execução.

## Aprendizados

- Automação de tarefas com Python.
- Manipulação de arquivos e diretórios.
- Uso de bibliotecas externas.
- Filtragem e ordenação de arquivos.
- Validações antes do processamento.
- Exibição de mensagens para orientar o usuário.
