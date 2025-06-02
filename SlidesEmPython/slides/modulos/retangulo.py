import pygame

def retangulo(
    cor,
    largura_ret,
    altura_ret,
    x,
    y,
    alinhamento,
    grossura,
    tela,
    estado_transicao="Visivel",
    progresso_transicao=1.0,
    transicao_entrada="fadein",  # "fadein", "desce", "sobe"
    transicao_saida="fadeout"    # "fadeout", "desce", "sobe"
):
    if isinstance(cor, str):
        cor = pygame.Color(cor)

    # Calcula alpha e deslocamento
    if estado_transicao == "Entrada":
        alfa = int(255 * progresso_transicao)
        deslocamento_y = 0
        if transicao_entrada == "desce":
            deslocamento_y = -50 * (1 - progresso_transicao)
        elif transicao_entrada == "sobe":
            deslocamento_y = 50 * (1 - progresso_transicao)

    elif estado_transicao == "Saida":
        alfa = int(255 * (1 - progresso_transicao))
        deslocamento_y = 0
        if transicao_saida == "desce":
            deslocamento_y = 50 * progresso_transicao
        elif transicao_saida == "sobe":
            deslocamento_y = -50 * progresso_transicao

    else:  # Visível
        alfa = 255
        deslocamento_y = 0

    y_animado = y + deslocamento_y

    ret = pygame.Rect(0, 0, largura_ret, altura_ret)

    if alinhamento == "centro":
        ret.center = (x, y_animado)
    elif alinhamento == "top_esquerda":
        ret.topleft = (x, y_animado)
    elif alinhamento == "top_direita":
        ret.topright = (x, y_animado)
    elif alinhamento == "baixo_direita":
        ret.bottomright = (x, y_animado)
    elif alinhamento == "baixo_esquerda":
        ret.bottomleft = (x, y_animado)
    elif alinhamento == "esquerda":
        ret.midleft = (x, y_animado)
    else:
        ret.topleft = (x, y_animado)

    # Superfície temporária para aplicar alpha
    superficie_temp = pygame.Surface((largura_ret, altura_ret), pygame.SRCALPHA)
    cor_com_alpha = (*cor[:3], alfa)
    pygame.draw.rect(superficie_temp, cor_com_alpha, superficie_temp.get_rect(), grossura)

    tela.blit(superficie_temp, ret.topleft)
