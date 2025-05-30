import pygame
from slides.modulos.retangulo import retangulo
from slides.modulos.imagem   import imagem
from slides.modulos.texto    import texto

# resolução de referência: ajuste se preferir
BASE_W, BASE_H = 1280, 720

def iniciar():
    """Inicialize a janela como redimensionável."""
    pygame.init()
    pygame.display.set_caption("Capa")

def atualizar(tela):
    w, h = tela.get_size()
    tela.fill((0xF1, 0xF1, 0xF1))

    # fator de escala (mantém proporção sem distorcer)
    scale = min(w / BASE_W, h / BASE_H)

    # ------------------ LOGOTIPO NO CANTO ------------------
    logo_size  = (int(127 * scale), int(110 * scale))
    imagem("puc_old.png",
           int(20 * scale), int(20 * scale),
           "top_esquerda", tela, logo_size)

    # --------------------- MOLDURA -------------------------
    margin_x = int(w * 0.05)
    top_y    = int(h * 0.10)
    rect_w   = w - 2 * margin_x
    rect_h   = int(h * 0.18)
    retangulo((0, 0, 0),
              margin_x, top_y, rect_w, rect_h,
              "top_esquerda", 2, tela)

    # --------------------- TÍTULO --------------------------
    title_font_size = max(24, int(79 * scale))       # garante legibilidade
    texto("Python", "#000000",
          title_font_size, "arial",
          w // 2, h // 2 - int(0.03 * h),
          "centro", tela, negrito=True)

    # --------------- ÍCONE DO PYTHON -----------------------
    icon_size = int(200 * scale)
    imagem("python.png",
           w // 2 - icon_size - int(w * 0.03),  # um pouco à esquerda do texto
           h // 2 - int(0.03 * h),
           "centro", tela, (icon_size, icon_size))

    # -------------------- AUTORES --------------------------
    authors_font = max(12, int(26 * scale))
    autores = [
        "Bruno Rafael Santos Oliveira, Letícia da Silva Rocha, Matheus Eduardo",
        "Campos Soares, Rayssa Mell de Souza Silva, Thiago Pereira de Oliveira"
    ]
    texto(autores, "#000000",
          authors_font, "arial",
          w // 2, h - int(h * 0.08),
          "centro", tela)

def evento(ev):
    """Você pode interceptar outros eventos aqui se precisar."""
    pass

# ---------- LOOP PRINCIPAL DE EXEMPLO ----------
if __name__ == "__main__":
    tela = iniciar()
    clock = pygame.time.Clock()

    rodando = True
    while rodando:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                rodando = False
            elif ev.type == pygame.VIDEORESIZE:
                # adapta a tela ao novo tamanho
                tela = pygame.display.set_mode(ev.size, pygame.RESIZABLE)
            evento(ev)

        atualizar(tela)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
