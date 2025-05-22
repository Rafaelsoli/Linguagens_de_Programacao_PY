import pygame
import os

def imagem(nome_arquivo, x, y, alinhamento, tela, escala=None):
    # Caminho base: um nível acima de slides (pasta raiz do projeto)
    pasta_base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    caminho_completo = os.path.join(pasta_base, "imagens", nome_arquivo)

    imagem_carregada = pygame.image.load(caminho_completo).convert_alpha()
    
    if escala:
        imagem_carregada = pygame.transform.scale(imagem_carregada, escala)

    ret = imagem_carregada.get_rect()

    if alinhamento == "centro":
        ret.center = (x, y)
    elif alinhamento == "top_esquerda":
        ret.topleft = (x, y)
    elif alinhamento == "top_direita":
        ret.topright = (x, y)
    elif alinhamento == "baixo_direita":
        ret.bottomright = (x, y)
    elif alinhamento == "baixo_esquerda":
        ret.bottomleft = (x, y)
    elif alinhamento == "esquerda":
        ret.midleft = (x, y)
    else:
        ret.topleft = (x, y)  # padrão

    tela.blit(imagem_carregada, ret)
