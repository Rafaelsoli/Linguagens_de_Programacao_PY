import pygame
from slides.modulos.retangulo import retangulo
from slides.modulos.imagem   import imagem
from slides.modulos.texto    import texto
from slides.modulos.circulo  import circulo

BASE_W, BASE_H = 1280, 720  # resolução base de referência

def iniciar():
    pygame.init()
    pygame.display.set_caption("Índice")

def evento(ev):
    pass  # pode adicionar interações aqui

def atualizar(tela, estado, progresso):
    tela.fill((0xF1, 0xF1, 0xF1))
    w, h = tela.get_size()
    scale = min(w / BASE_W, h / BASE_H)

    # ------------------ TÍTULO ------------------
    title_font = max(26, int(79 * scale))
    texto("Índice", "#000000", title_font, "arial",
          int(100 * scale), int(50 * scale), "top_esquerda", tela, negrito=True,
          estado_transicao=estado, progresso_transicao=progresso, transicao_entrada="fadein", transicao_saida="fadeout"
        )

    # ----------------- LINHA --------------------
    ret_x = int(350 * scale)
    ret_y = int(2 * scale)
    ret_w = int(80 * scale)
    ret_h = int(140 * scale)
    retangulo((0, 0, 0), ret_x, ret_y, ret_w, ret_h,
              "top_esquerda", 2, tela, estado_transicao=estado, progresso_transicao=progresso, transicao_entrada="sobe", transicao_saida="desce")

    # --------------- NUMERAÇÃO ------------------
    num_font = max(12, int(26 * scale))
    espacamento = int(37 * scale)
    texto(
        ["01", "02", "03", "04", "05", "06", "07", "08", "09"],
        "#000000", num_font, "arial",
        int(100 * scale), int(160 * scale),
        "top_esquerda", tela, negrito=True, espacamento=espacamento, estado_transicao=estado, progresso_transicao=progresso, transicao_entrada="fadein", transicao_saida="fadeout"
    )

    # ---------- TÍTULOS DAS SEÇÕES --------------
    texto(
        [
            "INTRODUÇÃO",
            "HISTÓRICO DA LINGUAGEM",
            "PARADIGMAS",
            "CARACTERÍSTICAS MARCANTES",
            "APLICAÇÕES",
            "LINGUAGENS RELACIONADAS",
            "EXEMPLOS",
            "CONSIDERAÇÕES FINAIS",
            "BIBLIOGRAFIA"
        ],
        "#000000", num_font, "arial",
        int(160 * scale), int(160 * scale),
        "top_esquerda", tela, espacamento=espacamento, estado_transicao=estado, progresso_transicao=progresso, transicao_entrada="fadein", transicao_saida="fadeout"
    )

    # ------------------ IMAGEM ------------------
    img_w = int(h / 3)
    img_h = int(h / 2)
    imagem("lupa.png", w, 0, "top_direita", tela, (img_w, img_h), estado_transicao=estado, progresso_transicao=progresso)

    # ------------------ CÍRCULOS -----------------
    circulo((0, 0, 0), int(200 * scale), int(200 * scale), h + int(100 * scale), "centro", 8, tela, estado_transicao=estado, progresso_transicao=progresso, transicao_entrada="fadein", transicao_saida="fadeout")
    circulo((0, 0, 0), int(150 * scale), int(200 * scale), h + int(100 * scale), "centro", 8, tela, estado_transicao=estado, progresso_transicao=progresso, transicao_entrada="fadein", transicao_saida="fadeout")
