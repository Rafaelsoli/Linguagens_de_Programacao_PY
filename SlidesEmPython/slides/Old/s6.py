import pygame
import random

# Configurações
colunas_fundo = []
velocidades_fundo = []

colunas_meio = []
velocidades_meio = []

colunas_frente = []
velocidades_frente = []

largura_coluna = 20
altura_linha = 20
# caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" # Sistema original de caracteres
caracteres = "01010101010101010101010101010101012" # Sistema alternativo (Adicionei um dois muito raro pelo meme)

def iniciar():
    global colunas_fundo, velocidades_fundo
    global colunas_meio, velocidades_meio
    global colunas_frente, velocidades_frente

    colunas_fundo.clear()
    velocidades_fundo.clear()
    colunas_meio.clear()
    velocidades_meio.clear()
    colunas_frente.clear()
    velocidades_frente.clear()

    largura, altura = 800, 600
    num_colunas = largura // largura_coluna

    for i in range(num_colunas):
        colunas_fundo.append(random.randint(-altura * 2, -altura))
        velocidades_fundo.append(random.randint(1, 2))

        colunas_meio.append(random.randint(-altura * 2, -altura))
        velocidades_meio.append(random.randint(2, 4))

        colunas_frente.append(random.randint(-altura * 2, -altura))
        velocidades_frente.append(random.randint(3, 6))

def atualizar (tela):
    largura, altura = tela.get_size ()
    num_colunas = largura // largura_coluna

    while len(colunas_fundo) < num_colunas:
        colunas_fundo.append(random.randint(-altura * 2, -altura))
        velocidades_fundo.append(random.randint(1, 2))

        colunas_meio.append(random.randint(-altura * 2, -altura))
        velocidades_meio.append(random.randint(2, 4))

        colunas_frente.append(random.randint(-altura * 2, -altura))
        velocidades_frente.append(random.randint(3, 6))

    while len(colunas_fundo) > num_colunas:
        colunas_fundo.pop()
        velocidades_fundo.pop()
        colunas_meio.pop()
        velocidades_meio.pop()
        colunas_frente.pop()
        velocidades_frente.pop()

    tela.fill((0, 0, 0))

    fonte_fundo = pygame.font.SysFont("consolas", 14)
    fonte_meio = pygame.font.SysFont("consolas", 18)
    fonte_frente = pygame.font.SysFont("consolas", 20)

    cor_fundo = (0, 80, 20)
    cor_meio = (0, 150, 50)
    cor_frente = (0, 255, 70)

    for i in range(num_colunas):
        x = i * largura_coluna

        y_fundo = colunas_fundo[i]
        for j in range(0, altura, altura_linha):
            pos_y = y_fundo + j
            if pos_y >= 0:
                char = random.choice(caracteres)
                texto = fonte_fundo.render(char, True, cor_fundo)
                tela.blit(texto, (x, pos_y))
        colunas_fundo[i] += velocidades_fundo[i]
        if colunas_fundo[i] > altura:
            colunas_fundo[i] = random.randint(-altura * 2, -altura)
            velocidades_fundo[i] = random.randint(1, 2)

        y_meio = colunas_meio[i]
        for j in range(0, altura, altura_linha):
            pos_y = y_meio + j
            if pos_y >= 0:
                char = random.choice(caracteres)
                texto = fonte_meio.render(char, True, cor_meio)
                tela.blit(texto, (x, pos_y))
        colunas_meio[i] += velocidades_meio[i]
        if colunas_meio[i] > altura:
            colunas_meio[i] = random.randint(-altura * 2, -altura)
            velocidades_meio[i] = random.randint(2, 4)

        y_frente = colunas_frente[i]
        for j in range(0, altura, altura_linha * 2):  # menor densidade
            pos_y = y_frente + j
            if pos_y >= 0:
                char = random.choice(caracteres)
                texto = fonte_frente.render(char, True, cor_frente)
                tela.blit(texto, (x, pos_y))
        colunas_frente[i] += velocidades_frente[i]
        if colunas_frente[i] > altura:
            colunas_frente[i] = random.randint(-altura * 2, -altura)
            velocidades_frente[i] = random.randint(3, 6)

def evento (evento):
    pass
