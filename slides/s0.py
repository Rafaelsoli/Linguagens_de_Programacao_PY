##################################################
# Bibliotecas usadas

import pygame

##################################################
# Bibliotecas próprias usadas

from slides.modulos.texto  import texto
from slides.modulos.imagem import imagem
from slides.modulos.retangulo import retangulo

##################################################
# Iniciando o Slide

def iniciar ():
    pass

def evento (evento):
    pass

##################################################
# Função que roda em todos os ticks

def atualizar (tela):

    # Iniciando variáveis úteis
    largura, altura = tela.get_size ()
    cx, cy = largura // 2, altura // 2
    tela.fill ((0x00, 0x3A, 0x52)) # Colore o plano de fundo

    ### DESENHANDO NA TELA
    cor_frame = (0x39, 0x9B, 0xC9)
    gr_fr = 3 # Grossura do frame
    ta_fr = 40 # tamanho dos frames de dentro do quadrado da direita
    di_po = 20 # Distância entre os pontos e a barra da esquerda
    di_p2 = 70 # Distância entre os pontos e a barra de cima

    # Desenhando o quadrado maior de fora
    x0_qm = 10 # Posição X do primeiro ponto do quadrado maior
    y0_qm = 10 # Posição Y do primeiro ponto
    x1_qm = largura - 10  # Posição X do segundo
    y1_qm = altura  - 10  # Posição Y
    retangulo (cor_frame, x1_qm - x0_qm, y1_qm - y0_qm, x0_qm, y0_qm, "top_esquerda", gr_fr, tela)

    # Desenhando o segundo maior
    di_q2 = 50 # Distância entre os 2
    x0_q2 = x0_qm 
    y0_q2 = y0_qm + di_q2
    x1_q2 = x1_qm 
    y1_q2 = y1_qm - di_q2
    retangulo (cor_frame, x1_q2 - x0_q2, y1_q2 - y0_q2, x0_q2, y0_q2, "top_esquerda", gr_fr, tela)

    # Desenhando o detalhe na parte de cima
    x0_qc = largura/3
    y0_qc = y0_qm
    x1_qc = 2*largura/3
    y1_qc = y0_q2 + gr_fr
    retangulo (cor_frame, x1_qc - x0_qc, y1_qc - y0_qc, x0_qc, y0_qc, "top_esquerda", gr_fr, tela)

    # Desenhando o detalhe na parte de baixo
    x0_qb = x0_qc
    y0_qb = y1_q2 - gr_fr
    x1_qb = x1_qc
    y1_qb = y1_qm
    retangulo (cor_frame, x1_qb - x0_qb, y1_qb - y0_qb, x0_qb, y0_qb, "top_esquerda", gr_fr, tela)

    # Quadrado da direita
    x0_qd = largura/2
    y0_qd = y0_q2
    x1_qd = x1_q2
    y1_qd = y1_q2
    retangulo (cor_frame, x1_qd - x0_qd, y1_qd - y0_qd, x0_qd, y0_qd, "top_esquerda", gr_fr, tela)

    # Frame de cima
    x0_fc = x0_qd
    y0_fc = y0_qd
    x1_fc = x1_qd
    y1_fc = y0_qd + ta_fr
    retangulo (cor_frame, x1_fc - x0_fc, y1_fc - y0_fc, x0_fc, y0_fc, "top_esquerda", gr_fr, tela)

    # Frame de baixo
    x0_fb = x0_qd
    y0_fb = (y0_qd + y1_qd)/2
    x1_fb = x1_qd
    y1_fb = y0_fb + ta_fr
    retangulo (cor_frame, x1_fb - x0_fb, y1_fb - y0_fb, x0_fb, y0_fb, "top_esquerda", gr_fr, tela)
 
    ### ESCREVENDO TEXTOS
    
    # Sobre nós
    x_t1 = (x0_fc + x1_fc)/2
    y_t1 = (y1_fc + y0_fb)/2
    t_t1 = int ((largura if largura < altura else altura)/13)
    texto ("SOBRE NÓS", (0xF4, 0x8D, 0x6A), t_t1, "arial", x_t1, y_t1, "centro", tela, negrito=True)

    # Pontos
    x_t2 = x0_q2 + di_po
    y_t2 = y0_q2 + di_p2
    t_t2 = int ((largura if largura < altura else altura)/30)

    texto (
        [
            "• Destaca-se no mercado", 
            "• Recursos inovadores",
            "• Fornece uma solução original",
            "• Vantagem sobre a concorrência",
            "• Design com foco no usuário",
            "• Prioriza a experiência do usuário"
        ], 
        (255, 255, 255), t_t2, "arial", x_t2, y_t2, "top_esquerda", tela, espacamento=(t_t2/20)*60
    )