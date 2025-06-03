import os
import pygame

# Caminho da logo
LOGO_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "imagens", "logo.png")
LOGO_PATH = os.path.abspath(LOGO_PATH)

# Cor de fundo padrão
FUNDO_BRANCO = (255, 255, 255)

# Superfície da logo (carregada uma única vez)
_logo_surface = None

def carregar_logo():
    global _logo_surface
    if _logo_surface is None:
        _logo_surface = pygame.image.load(LOGO_PATH).convert_alpha()
    return _logo_surface

def desenhar_logo(tela, margem=10):
    logo = carregar_logo()
    rect = logo.get_rect()
    rect.topright = (tela.get_width() - margem, margem)
    tela.blit(logo, rect)
