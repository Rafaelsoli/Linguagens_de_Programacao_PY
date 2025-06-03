import random
import pygame
import numpy as np

lista = []
indice = 0
som_ativo = False
som = None

def gerar_tom (frequencia, duracao_ms = 100, volume = 0.2):
    taxa_amostragem = 44100
    t = np.linspace (0, duracao_ms / 1000, int (taxa_amostragem * duracao_ms / 1000), False)
    onda = 0.5 * np.sin (2 * np.pi * frequencia * t)  # onda senoidal
    onda_int = np.int16 (onda * 32767)
    onda_stereo = np.column_stack ((onda_int, onda_int))  # 2 canais idênticos
    som_pygame = pygame.sndarray.make_sound (onda_stereo)
    som_pygame.set_volume (volume)
    return som_pygame


def iniciar ():
    global lista, indice, som_ativo, som
    lista = [random.randint (10, 500) for _ in range (100)]
    indice = 0
    som_ativo = False
    som = None

def atualizar (tela):
    global lista, indice, som_ativo, som
    tela.fill ((10, 10, 10))
    largura_tela, altura_tela = tela.get_size ()
    largura_barra = largura_tela // len (lista)

    # Desenha todas as barras
    for i, valor in enumerate (lista):
        cor = (255, 0, 0) if i == indice else (255, 255, 255)
        pygame.draw.rect (
            tela,
            cor,
            (i * largura_barra, altura_tela - valor, largura_barra - 1, valor)
        )

    # Executa um passo do Gnome Sort por frame
    if indice < len (lista):
        if indice == 0 or lista[indice] >= lista[indice - 1]:
            indice += 1
        else:
            lista[indice], lista[indice - 1] = lista[indice - 1], lista[indice]
            indice -= 1

        # Toca som com frequência proporcional à altura da barra no índice
        freq_base = 200  # frequência mínima (Hz)
        freq_max = 1000  # frequência máxima (Hz)
        altura_normalizada = lista[indice] / 500  # 0 a 1
        frequencia_tom = freq_base + (freq_max - freq_base) * altura_normalizada

        if som_ativo:
            som.stop ()
        som = gerar_tom (frequencia_tom, duracao_ms = 80, volume = 0.15)
        som.play ()
        som_ativo = True

def evento (evento):
    pass
