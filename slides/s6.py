import pygame
import random

# Configurações
colunas = []
velocidades = []
largura_coluna = 20
altura_linha = 20
caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def iniciar():
    global colunas, velocidades
    colunas.clear()
    velocidades.clear()

    largura, altura = 800, 600  # valor padrão; será atualizado em `atualizar`
    num_colunas = largura // largura_coluna

    for i in range(num_colunas):
        y_inicial = random.randint(-500, 0)
        colunas.append(y_inicial)
        velocidades.append(random.randint(3, 7))

def atualizar (tela):
    largura, altura = tela.get_size ()
    num_colunas = largura // largura_coluna

    while len(colunas) < num_colunas:
        colunas.append(random.randint(-500, 0))
        velocidades.append(random.randint(3, 7))

    while len(colunas) > num_colunas:
        colunas.pop()
        velocidades.pop()

    tela.fill((0, 0, 0))
    fonte = pygame.font.SysFont("consolas", 20)
    cor_matrix = (0, 255, 70)

    for i in range(num_colunas):
        x = i * largura_coluna
        y = colunas[i]

        for j in range(0, altura, altura_linha):
            if y + j < 0:
                continue

            char = random.choice(caracteres)
            texto = fonte.render(char, True, cor_matrix)
            tela.blit(texto, (x, y + j))

        colunas[i] += velocidades[i]

        if colunas[i] > altura:
            colunas[i] = random.randint(-500, -50)
            velocidades[i] = random.randint(3, 7)


def evento(evento):
    pass
