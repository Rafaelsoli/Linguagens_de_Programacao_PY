import pygame

# Função de geração de texto
def texto (conteudo, cor, tamanho, fonte, x, y, alinhamento, tela):
    fonte_pygame = pygame.font.SysFont (fonte, tamanho)

    if isinstance (cor, str):
        cor = pygame.Color (cor)

    superficie = fonte_pygame.render (conteudo, True, cor)
    ret = superficie.get_rect ()

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

    tela.blit (superficie, ret)