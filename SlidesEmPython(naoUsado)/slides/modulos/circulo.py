import pygame

def circulo(
    cor,
    raio,
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

    # Calcula alpha e deslocamento Y
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

    centro_x = x
    centro_y = y + deslocamento_y

    if alinhamento == "top_esquerda":
        centro_x = x + raio
        centro_y = y + raio + deslocamento_y
    elif alinhamento == "top_direita":
        centro_x = x - raio
        centro_y = y + raio + deslocamento_y
    elif alinhamento == "baixo_direita":
        centro_x = x - raio
        centro_y = y - raio + deslocamento_y
    elif alinhamento == "baixo_esquerda":
        centro_x = x + raio
        centro_y = y - raio + deslocamento_y
    elif alinhamento == "esquerda":
        centro_x = x + raio
    elif alinhamento == "direita":
        centro_x = x - raio
    elif alinhamento == "top":
        centro_y = y + raio + deslocamento_y
    elif alinhamento == "baixo":
        centro_y = y - raio + deslocamento_y

    # Superfície temporária para alpha
    diametro = 2 * raio
    superficie_temp = pygame.Surface((diametro, diametro), pygame.SRCALPHA)
    cor_com_alpha = (*cor[:3], alfa)
    pygame.draw.circle(
        superficie_temp,
        cor_com_alpha,
        (raio, raio),
        raio,
        grossura
    )

    tela.blit(superficie_temp, (centro_x - raio, centro_y - raio))
