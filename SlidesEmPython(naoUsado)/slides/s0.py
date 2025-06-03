import pygame
from slides.modulos.retangulo import retangulo
from slides.modulos.circulo   import circulo
from slides.modulos.imagem    import imagem
from slides.modulos.texto     import texto

# resolução de referência: ajuste se preferir
BASE_W, BASE_H = 1280, 720

def iniciar():
    pygame.init()
    pygame.display.set_caption("Capa")

def evento(ev):
    pass

def atualizar (tela, estado, progresso):
    w, h = tela.get_size()
    tela.fill((0xF1, 0xF1, 0xF1))

    # fator de escala (mantém proporção sem distorcer)
    scale = min(w / BASE_W, h / BASE_H)

    # ------------------ LOGOTIPO NO CANTO ------------------
    circulo((0xaa, 0xe3, 0xee), int(500 * scale), -100, -100, "centro", 180, tela, estado_transicao=estado, progresso_transicao=progresso, transicao_entrada="fadein", transicao_saida="fadeout")

    logo_size  = (int(1.2*127 * scale), int(1.2*110 * scale))
    imagem("puc_old.png",
           int(50 * scale), int(50 * scale),
           "top_esquerda", tela, logo_size, estado_transicao=estado, progresso_transicao=progresso, transicao_entrada="fadein")

    # --------------------- LINHA SOLTA ---------------------
    ret_x = int(350 * scale)
    ret_h = int(140 * scale)
    retangulo((0, 0, 0), ret_x, 2, w - ret_x, ret_h,
              "top_esquerda", 2, tela, estado_transicao=estado, progresso_transicao=progresso, transicao_entrada="sobe", transicao_saida="desce")

    # --------------------- TÍTULO --------------------------
    title_font_size = max(24, int(79 * scale))       # garante legibilidade
    texto("Python", "#000000",
          title_font_size, "arial",
          w // 2, h // 2 - int(0.03 * h),
          "centro", tela, negrito=True, estado_transicao=estado, progresso_transicao=progresso, transicao_entrada="fadein", transicao_saida="desce")

    # --------------- ÍCONE DO PYTHON -----------------------
    icon_size = int(200 * scale)
    imagem("python.png",
           w // 2 - icon_size - int(w * 0.03),  # um pouco à esquerda do texto
           h // 2 - int(0.03 * h),
           "centro", tela, (icon_size, icon_size), estado_transicao=estado, progresso_transicao=progresso, transicao_entrada="fadein", transicao_saida="fadeout")

    # -------------------- AUTORES --------------------------
    authors_font = max(12, int(26 * scale))
    autores = [
        "Bruno Rafael Santos Oliveira, Letícia da Silva Rocha, Matheus Eduardo",
        "Campos Soares, Rayssa Mell de Souza Silva, Thiago Pereira de Oliveira"
    ]
    texto(autores, "#000000",
          authors_font, "arial",
          w // 2, h - int(h * 0.08),
          "centro", tela, estado_transicao=estado, progresso_transicao=progresso, transicao_entrada="fadein", transicao_saida="desce")