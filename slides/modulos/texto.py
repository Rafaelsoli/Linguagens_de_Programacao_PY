import pygame

# Função de geração de texto com suporte a lista, itálico, negrito, sublinhado, espaçamento e contorno
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
    espacamento = None,
    grossura_contorno = None,
    cor_contorno = None
):
    if isinstance (cor, str):
        cor = pygame.Color (cor)

    if grossura_contorno is not None and cor_contorno is None:
        cor_contorno = (0, 0, 0)
    if cor_contorno is not None and grossura_contorno is None:
        grossura_contorno = 1
    if isinstance (cor_contorno, str):
        cor_contorno = pygame.Color (cor_contorno)

    fonte_pygame = pygame.font.SysFont (fonte, tamanho, bold = negrito, italic = italico)
    fonte_pygame.set_underline (sublinhado)

    if isinstance (conteudo, str):
        conteudo = [conteudo]

    if espacamento is None:
        espacamento = tamanho

    for i in range (len (conteudo)):
        texto_original = conteudo[i]
        superficie_principal = fonte_pygame.render (texto_original, True, cor)
        ret = superficie_principal.get_rect ()

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

        if grossura_contorno:
            for dx in range (-grossura_contorno, grossura_contorno + 1):
                for dy in range (-grossura_contorno, grossura_contorno + 1):
                    if dx == 0 and dy == 0:
                        continue
                    sombra = fonte_pygame.render (texto_original, True, cor_contorno)
                    tela.blit (sombra, (ret.x + dx, ret.y + dy))

        tela.blit (superficie_principal, ret)
