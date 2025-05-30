import pygame
from slides.modulos.matrix import EfeitoMatrix
from slides.modulos.imagem import imagem

efeito = None

def iniciar ():
    global efeito
    largura, altura = 800, 600
    efeito = EfeitoMatrix (largura, altura)

def evento (evento):
    pass

def atualizar (tela):
    largura, altura = tela.get_size ()
    cx, cy = largura // 2, altura // 2
    
    efeito.atualizar (tela)
    imagem (
        "1.png", largura/2, altura/2, "centro", tela, 
        (largura/1.3, largura/2) if altura > largura/2 else (altura/1.3, altura/2)
    )

