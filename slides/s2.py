import pygame
from slides.modulos.retangulo import retangulo
from slides.modulos.imagem   import imagem
from slides.modulos.texto    import texto

BASE_W, BASE_H = 1280, 720  # resolução de referência

def iniciar():
    pygame.init()
    pygame.display.set_caption("Paradigmas")

def evento(ev):
    pass

def atualizar(tela):
    tela.fill((0xF1, 0xF1, 0xF1))
    w, h = tela.get_size()
    scale = min(w / BASE_W, h / BASE_H)

    # ------------------ TÍTULO ------------------
    title_font = max(26, int(79 * scale))
    texto("3. Paradigmas", "#000000", title_font, "arial",
          int(100 * scale), int(50 * scale), "top_esquerda", tela, negrito=True)

    # ------------------ RETÂNGULO ----------------
    retangulo((0, 0, 0),
              int(350 * scale), int(2 * scale),
              int(80 * scale), int(140 * scale),
              "top_esquerda", 2, tela)

    # ------------------- IMAGEM ------------------
    img_size = int(300 * scale)
    imagem("detalhe.png", w, 0, "top_direita", tela, (img_size, img_size))

    # ------------------ PARÁGRAFO 1 ------------------
    text_font = max(14, int(26 * scale))
    espacamento_1 = int(37 * scale)
    texto(
        [
            "Python é uma linguagem multiparadigma, ou seja, permite programar de diferentes formas de acordo com a",
            "necessidade do projeto. Essa flexibilidade torna a linguagem mais versátil e poderosa para resolver variados",
            "tipos de problemas."
        ],
        "#000000", text_font, "arial",
        int(100 * scale), int(160 * scale),
        "top_esquerda", tela, espacamento=espacamento_1
    )

    # --------------- LISTA DE PARADIGMAS ----------------
    espacamento_lista = int(70 * scale)
    texto(
        [
            "● Paradigma Procedural",
            "● Paradigma Orientado a Objetos (POO)", 
            "● Paradigma Funcional"
        ],
        "#000000", text_font, "arial",
        int(130 * scale), int(300 * scale),
        "top_esquerda", tela, negrito=True, espacamento=espacamento_lista
    )

    # ---------------- PARÁGRAFO FINAL ------------------
    texto(
        [
            "O desenvolvedor pode escolher o estilo mais adequado ao problema, ou até combinar paradigmas no mesmo",
            "projeto."
        ],
        "#000000", text_font, "arial",
        int(100 * scale), int(500 * scale),
        "top_esquerda", tela, espacamento=espacamento_1
    )