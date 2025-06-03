## Código que calcula média da nota de alunos

# 1. Importações
import os
## Em C se usa #include, em java se usa import, mesmo que python

# 2. Constantes globais
## (Definidas foras de blocos de identação)
ARQUIVO_ENTRADA = "notas.txt"
ARQUIVO_SAIDA = "relatorio.txt"

# 3. Função que lê os dados do arquivo
def lerNotas (caminho):
    ## Tratamento de erro
    if not os.path.exists (caminho):
        return []
    
    with open (caminho, "r") as arquivo:
        linhas = arquivo.readlines ()

    dados = []
    for linha in linhas:
        partes = linha.strip ().split (",")

        ## Garante que existe o nome e ao menos uma nota
        if len (partes) < 2:
            continue
        nome = partes[0]

        ## Retorna os nomes, juntamente com as notas de todos
        notas = [float (n) for n in partes[1:] if n]
        dados.append ((nome, notas))

    return dados

# 4. Função que calcula a média das notas
def calcularMedia (notas):
    if len (notas) == 0:
        return 0
    return sum (notas) / len (notas)

# 5. Função que salva o relatório
def salvarRelatorio (dados, caminho_saida):
    with open (caminho_saida, "w") as arquivo:
        for nome, notas in dados:
            media = calcularMedia (notas)
            arquivo.write (f"{nome}: media = {media:.2f}\n")

# 6. Classe opcional para encapsular o processo
class GeradorRelatorio:
    ## Construtor
    def __init__ (self, caminho_entrada, caminho_saida):
        self.entrada = caminho_entrada
        self.saida = caminho_saida

    ## Função da classe
    def executar (self):
        dados = lerNotas (self.entrada)
        salvarRelatorio (dados, self.saida)

# 7. Bloco principal
if __name__ == "__main__":
    gerador = GeradorRelatorio (ARQUIVO_ENTRADA, ARQUIVO_SAIDA)
    gerador.executar ()
    print ("Relatório gerado com sucesso!")