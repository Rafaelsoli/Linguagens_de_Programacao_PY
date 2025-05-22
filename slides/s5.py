import pygame
from slides.modulos.texto  import texto
from slides.modulos.imagem import imagem

def iniciar ():
    pass

def evento (evento):
    pass

def atualizar (tela):
    tela.fill ((20, 20, 30))
    largura, altura = tela.get_size ()
    cx, cy = largura // 2, altura // 2

    texto ("Tratamento de Texto em Slides", "#FFFFFF", 48, "arial", cx, 70, "centro", tela)

    texto ("Exemplo em itálico", "#FFFF64", 28, "consolas", largura - 280, altura - 60, "top_esquerda", tela)

    texto ("Bom dia!", "#ABCDEF", 37, "arial", 0, 0, "top_esquerda", tela)

    imagem ("bola.png", -70, 1.2*altura, "baixo_esquerda", tela, (largura/2, altura/2))


