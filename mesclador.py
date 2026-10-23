# Antes de executar este script, crie uma pasta chamada "arquivos"
# e coloque nela os PDFs que deseja mesclar.
# Execute o programa pelo terminal dentro da pasta do projeto.

# Biblioteca para manipular PDFs.
import PyPDF2

# Biblioteca para manipular arquivos e diretórios.
import os

# Verifica se a pasta existe antes de listar os arquivos.
if not os.path.isdir("arquivos"):
    print('Crie uma pasta chamada "arquivos" e coloque os PDFs nela.')
    raise SystemExit

# Lista os arquivos da pasta e ordena pelo nome.
lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()

# Seleciona apenas arquivos PDF, ignorando pastas.
arquivos_pdf = []

for arquivo in lista_arquivos:
    if arquivo.lower().endswith(".pdf") and os.path.isfile(f"arquivos/{arquivo}"):
        arquivos_pdf.append(arquivo)

# Encerra se nenhum PDF foi encontrado.
if not arquivos_pdf:
    print('Nenhum PDF encontrado na pasta "arquivos".')
    raise SystemExit

# Evita substituir um resultado anterior.
if os.path.exists("pdfs_mesclados.pdf"):
    print('O arquivo "pdfs_mesclados.pdf" já existe.')
    print("Renomeie ou mova esse arquivo antes de executar novamente.")
    raise SystemExit

# Cria o mesclador após verificar os arquivos e o destino.
mesclador = PyPDF2.PdfMerger()

# Adiciona os PDFs selecionados ao mesclador.
for arquivo in arquivos_pdf:
    mesclador.append(f"arquivos/{arquivo}")

# Salva o resultado e libera os recursos do mesclador.
mesclador.write("pdfs_mesclados.pdf")
mesclador.close()

print(f"{len(arquivos_pdf)} PDFs mesclados com sucesso!")
print('Resultado salvo em "pdfs_mesclados.pdf".')
