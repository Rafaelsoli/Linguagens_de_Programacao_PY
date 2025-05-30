import pygame
from slides.modulos.retangulo import retangulo
from slides.modulos.imagem import imagem
from slides.modulos.texto  import texto
from slides.modulos.circulo  import circulo

def iniciar ():
    pass

def evento (evento):
    pass

def atualizar (tela):
    tela.fill ((0xf1, 0xf1, 0xf1))
    largura, altura = tela.get_size ()
    cx, cy = largura // 2, altura // 2

    texto ("Índice", "#000000", 79, "arial", 100, 50, "top_esquerda", tela, negrito=True)
    retangulo ((0x00, 0x00, 0x00), 350, 2, 80, 140, "top_esquerda", 2, tela)

    texto (
        ["01", 
         "02", 
         "03", 
         "04", 
         "05", 
         "06", 
         "07", 
         "08", 
         "09",
         ],
           "#000000", 26, "arial", 100, 160, "top_esquerda", tela, negrito=True, espacamento=37
    )

    texto (
        ["INTRODUÇÃO",
         "HISTÓRICO DA LINGUAGEM",
         "PARADIGMAS",
         "CARACTERÍSTICAS MARCANTES",
         "APLICAÇÕES",
         "LINGUAGENS RELACIONADAS",
         "EXEMPLOS",
         "CONSIDERAÇÕES FINAIS",
         "BIBLIOGRAFIA"
         ],
           "#000000", 26, "arial", 160, 160, "top_esquerda", tela, espacamento=37
    )
    
    imagem ("lupa.png", largura, 0, "top_direita", tela, (altura/3, altura/2))

    circulo ((0x00, 0x00, 0x00), 200, 200, altura + 100, "centro", 8, tela)
    circulo ((0x00, 0x00, 0x00), 150, 200, altura + 100, "centro", 8, tela)