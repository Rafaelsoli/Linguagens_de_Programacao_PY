import os
import pygame
from slides.modulos.texto import texto  # <- ajuste conforme onde você salvou sua função
from slides.modulos.estilo import FUNDO_BRANCO, desenhar_logo

# Caminho da logo (pasta imagens ao lado do main.py)
LOGO_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "imagens", "logo.png")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Conteúdo do slide
TITULO = "Slide 4 - Exemplo com função texto"
CORPO = [
    "Este slide demonstra como usar",
    "uma função padrão para desenhar texto.",
    "",
    "Use as setas ← e → para navegar."
]

logo_surface = None

def iniciar():
    pass  # Nenhuma inicialização necessária agora

def atualizar(tela):
    tela.fill(FUNDO_BRANCO)

    desenhar_logo(tela)

    texto(TITULO, "black", 48, None, tela.get_width() // 2, 100, "centro", tela)

    y = 180
    for linha in CORPO:
        texto(linha, "black", 28, None, tela.get_width() // 2, y, "centro", tela)
        y += 40

def evento(evento):
    pass
