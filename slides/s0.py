import pygame

pos_circulo = 0

def iniciar ():
    global pos_circulo
    pos_circulo = 0

def atualizar (tela):
    global pos_circulo
    azul = (50, pos_circulo % 225, 255)
    pygame.draw.circle (tela, azul, (pos_circulo, 300), 40)
    pos_circulo += 2
    if pos_circulo > 800:
        pos_circulo = 0

def evento (evento):
    pass
