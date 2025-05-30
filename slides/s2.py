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

    texto ("3. Paradigmas", "#000000", 79, "arial", 100, 50, "top_esquerda", tela, negrito=True)
    retangulo ((0x00, 0x00, 0x00), 350, 2, 80, 140, "top_esquerda", 2, tela)

    imagem ("detalhe.png", largura, 0, "top_direita", tela, (300, 300))

    texto (
        ["Python é uma linguagem multiparadigma, ou seja, permite programar de diferentes formas de acordo com a",
         "necessidade do projeto. Essa flexibilidade torna a linguagem mais versátil e poderosa para resolver variados",
         "tipos de problemas."
         ],
           "#000000", 26, "arial", 100, 160, "top_esquerda", tela, espacamento=37
    )

    texto (
        ["● Paradigma Procedural", 
         "● Paradigma Orientado a Objetos (POO)", 
         "● Paradigma Funcional"
         ],
           "#000000", 26, "arial", 130, 300, "top_esquerda", tela, negrito=True, espacamento=70
    )


    texto (
        ["O desenvolvedor pode escolher o estilo mais adequado ao problema, ou até combinar paradigmas no mesmo",
         "projeto."
         ],
           "#000000", 26, "arial", 100, 500, "top_esquerda", tela, espacamento=37
    )