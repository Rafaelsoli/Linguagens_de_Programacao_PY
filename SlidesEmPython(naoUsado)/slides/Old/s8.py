import pygame
from slides.modulos.matrix import EfeitoMatrix

efeito = None

def iniciar ():
    global efeito
    largura, altura = 800, 600
    efeito = EfeitoMatrix (largura, altura)

def atualizar (tela):
    efeito.atualizar (tela)

def evento (evento):
    pass
