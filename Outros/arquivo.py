import heapq
import os
import tempfile

tamanho_bloco = 1000
arquivo_entrada = "numeros.txt"
arquivo_saida = "ordenado.txt"

# 1. Gera um arquivo grande com números aleatórios (só uma vez)
from random import randint
with open (arquivo_entrada, "w") as arq:
    for _ in range (5000):
        arq.write (str (randint (0, 9999)) + "\n")

# 1. Divide o arquivo em blocos menores ordenados
arquivos_temp = []
with open (arquivo_entrada, "r") as arq:
    while True:
        linhas = [arq.readline () for _ in range (tamanho_bloco)]
        linhas = [int (linha.strip ()) for linha in linhas if linha]
        if not linhas:
            break
        linhas.sort ()
        arq_temp = tempfile.NamedTemporaryFile (delete=False, mode="w")
        for numero in linhas:
            arq_temp.write (str (numero) + "\n")
        arq_temp.close ()
        arquivos_temp.append (arq_temp.name)

# 2. Merge dos arquivos usando heap
arquivos_abertos = [open (nome, "r") for nome in arquivos_temp]
heap = []

for i, arq in enumerate (arquivos_abertos):
    linha = arq.readline ()
    if linha:
        heapq.heappush (heap, (int (linha.strip ()), i))

with open (arquivo_saida, "w") as saida:
    while heap:
        menor, origem = heapq.heappop (heap)
        saida.write (str (menor) + "\n")
        linha = arquivos_abertos[origem].readline ()
        if linha:
            heapq.heappush (heap, (int (linha.strip ()), origem))

# Fecha e remove arquivos temporários
for arq in arquivos_abertos:
    arq.close ()
for nome in arquivos_temp:
    os.remove (nome)
