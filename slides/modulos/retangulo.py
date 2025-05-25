import pygame

def retangulo (cor, largura_ret, altura_ret, x, y, alinhamento, grossura, tela):
    if isinstance (cor, str):
        cor = pygame.Color (cor)

    ret = pygame.Rect (0, 0, largura_ret, altura_ret)

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

    pygame.draw.rect (tela, cor, ret, grossura)
