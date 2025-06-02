import pygame

def texto (
    conteudo,
    cor,
    tamanho,
    fonte,
    x,
    y,
    alinhamento,
    tela,
    estado_transicao,       # "entrada", "visivel", "saida"
    progresso_transicao,    # float de 0 a 1
    transicao_entrada = None,  # "fadein", "desce", "sobe"
    transicao_saida = None,   # "fadeout", "desce", "sobe"
    negrito = False,
    italico = False,
    sublinhado = False,
    espacamento = None,
    grossura_contorno = None,
    cor_contorno = None,
):
    if isinstance(cor, str):
        cor = pygame.Color(cor)

    if grossura_contorno is not None and cor_contorno is None:
        cor_contorno = (0, 0, 0)
    if cor_contorno is not None and grossura_contorno is None:
        grossura_contorno = 1
    if isinstance(cor_contorno, str):
        cor_contorno = pygame.Color(cor_contorno)

    fonte_pygame = pygame.font.SysFont(fonte, tamanho, bold=negrito, italic=italico)
    fonte_pygame.set_underline(sublinhado)

    if isinstance(conteudo, str):
        conteudo = [conteudo]

    if espacamento is None:
        espacamento = tamanho

    # Decide o alpha e deslocamento com base no estado e tipo de transição
    if estado_transicao == "Entrada" and transicao_entrada is not None:
        alfa = int(255 * progresso_transicao)
        deslocamento_y = 0
        if transicao_entrada == "desce":
            deslocamento_y = -50 * (1 - progresso_transicao)
        elif transicao_entrada == "sobe":
            deslocamento_y = 50 * (1 - progresso_transicao)
        elif transicao_entrada == "fadein":
            deslocamento_y = 0
        else:  # Visível ou transição desativada
            alfa = 255
            deslocamento_y = 0


    elif estado_transicao == "Saida" and transicao_saida is not None:
        alfa = int(255 * (1 - progresso_transicao))
        deslocamento_y = 0
        if transicao_saida == "desce":
            deslocamento_y = 50 * progresso_transicao
        elif transicao_saida == "sobe":
            deslocamento_y = -50 * progresso_transicao
        elif transicao_saida == "fadeout":
            deslocamento_y = 0
        else:  # Visível ou transição desativada
            alfa = 255
            deslocamento_y = 0


    else:  # visível
        alfa = 255
        deslocamento_y = 0

    for i in range(len(conteudo)):
        texto_original = conteudo[i]
        superficie_principal = fonte_pygame.render(texto_original, True, cor)
        superficie_principal.set_alpha(alfa)
        ret = superficie_principal.get_rect()

        y_linha = y + i * espacamento + deslocamento_y

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

        # Desenha contorno se necessário
        if grossura_contorno:
            for dx in range(-grossura_contorno, grossura_contorno + 1):
                for dy in range(-grossura_contorno, grossura_contorno + 1):
                    if dx == 0 and dy == 0:
                        continue
                    sombra = fonte_pygame.render(texto_original, True, cor_contorno)
                    sombra.set_alpha(alfa)
                    tela.blit(sombra, (ret.x + dx, ret.y + dy))

        # Desenha o texto principal
        tela.blit(superficie_principal, (ret.x, ret.y))
