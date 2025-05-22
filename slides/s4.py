import os
import pygame

# --- Configurações do conteúdo ------------------------------------------------
TITULO = "Título do Slide"
CORPO  = (
    "Corpo do slide – escreva o quanto quiser.\n"
    "Use \\n para quebrar linhas.\n"
    "Vale misturar maiúsculas, negrito, etc."
)
LOGO_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "imagens", "logo.png")


# --- Cores --------------------------------------------------------------------
BRANCO = (255, 255, 255)
PRETO  = (0, 0, 0)

# --- Variáveis de estado internas --------------------------------------------
fonte_titulo = fonte_corpo = None
logo_surface = None

# ------------------------------------------------------------------------------
def iniciar():
    """Chamado uma vez quando o slide entra na tela."""
    global fonte_titulo, fonte_corpo, logo_surface

    pygame.font.init()
    # Troque a fonte/tamanho se preferir
    fonte_titulo = pygame.font.SysFont(None, 64, bold=True)
    fonte_corpo  = pygame.font.SysFont(None, 32)
    logo_surface = pygame.image.load(LOGO_PATH).convert_alpha()

# ------------------------------------------------------------------------------
def atualizar(tela):
    """Chamado a cada quadro para desenhar o slide."""
    tela.fill(BRANCO)

    # --- Logo no canto superior direito
    logo_rect = logo_surface.get_rect()
    logo_rect.topright = (tela.get_width() - 20, 20)
    tela.blit(logo_surface, logo_rect)

    # --- Título centralizado
    titulo_surf = fonte_titulo.render(TITULO, True, PRETO)
    titulo_rect = titulo_surf.get_rect(center=(tela.get_width() // 2, 120))
    tela.blit(titulo_surf, titulo_rect)

    # --- Corpo (quebra de linha automática)
    y = 200
    for linha in CORPO.split("\n"):
        corpo_surf = fonte_corpo.render(linha, True, PRETO)
        corpo_rect = corpo_surf.get_rect(center=(tela.get_width() // 2, y))
        tela.blit(corpo_surf, corpo_rect)
        y += fonte_corpo.get_height() + 10

# ------------------------------------------------------------------------------
def evento(evento):
    """Receba e trate eventos se precisar (ex.: teclas para avançar)."""
    pass
