#bilbioteca pra manipular PDFs
import PyPDF2

#biblioteca para manipular arquivos
import os

#cria-se o mesclador
mesclador = PyPDF2.PdfMerger()

#cria-se o diretorio da lista de arquivos e organiza por ordem
lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()

#percorrre os arquivos da lista
for arquivo in lista_arquivos:
  #analisa se a extensao do arquivo é pdf
  if arquivo.endswith(".pdf"):
    #adiciona o arquivo no mesclador
    mesclador.append(f"arquivos/{arquivo}")

#escreve/cria um novo arquivo com os PDSs mesclados
mesclador.write("pdfs_mesclados.pdf")

#encerra o processo
mesclador.close()