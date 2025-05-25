import pygame

# Função de geração de texto (com suporte a lista, itálico, negrito, sublinhado e espaçamento)
def texto (
    conteudo,
    cor,
    tamanho,
    fonte,
    x,
    y,
    alinhamento,
    tela,
    negrito = False,
    italico = False,
    sublinhado = False,
    espacamento = None
):
    if isinstance (cor, str):
        cor = pygame.Color (cor)

    fonte_pygame = pygame.font.SysFont (fonte, tamanho, bold = negrito, italic = italico)
    fonte_pygame.set_underline (sublinhado)

    if isinstance (conteudo, str):
        conteudo = [conteudo]

    if espacamento is None:
        espacamento = tamanho

    for i in range (len (conteudo)):
        superficie = fonte_pygame.render (conteudo[i], True, cor)
        ret = superficie.get_rect ()

        y_linha = y + i * espacamento

        if alinhamento == "centro":
            ret.center = (x, y_linha)
        elif alinhamento == "top_esquerda":
            ret.topleft = (x, y_linha)
        elif alinhamento == "top_direita":
            ret.topright = (x, y_linha)
        elif alinhamento == "baixo_direita":
            ret.bottomright = (x, y_linha)
        elif alinhamento == "baixo_esquerda":
            ret.bottomleft = (x, y_linha)
        elif alinhamento == "esquerda":
            ret.midleft = (x, y_linha)
        else:
            ret.topleft = (x, y_linha)

        tela.blit (superficie, ret)
