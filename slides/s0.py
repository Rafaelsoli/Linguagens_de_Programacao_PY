import pygame
from slides.modulos.retangulo import retangulo
from slides.modulos.imagem import imagem
from slides.modulos.texto  import texto

def iniciar ():
    pass

def evento (evento):
    pass

def atualizar (tela):
    tela.fill ((0xf1, 0xf1, 0xf1))
    largura, altura = tela.get_size ()
    cx, cy = largura // 2, altura // 2

    imagem ("puc_old.png", 20, 20, "top_esquerda", tela, (127, 110))
    retangulo ((0x00, 0x00, 0x00), largura/3 -100, 2, 2*largura/3+100, 130, "top_esquerda", 2, tela)

    texto ("Python", "#000000", 79, "arial", cx, cy - 20, "centro", tela, negrito=True)
    imagem ("python.png", cx - 200 - cx*0.1, cy - 20, "centro", tela, (200, 200))

    texto (
        ["Bruno Rafael Santos Oliveira, Letícia da Silva Rocha, Matheus Eduardo", 
         "Campos Soares, Rayssa Mell de Souza Silva, Thiago Pereira de Oliveira"],
           "#000000", 26, "arial", cx, altura - 150, "centro", tela
    )



