import pygame
import os

def imagem(
    nome_arquivo,
    x,
    y,
    alinhamento,
    tela,
    escala=None,
    estado_transicao="Visivel",
    progresso_transicao=1.0,
    transicao_entrada=None,  # "fadein", "desce", "sobe"
    transicao_saida=None    # "fadeout", "desce", "sobe"
):
    # Caminho base: um nível acima de slides (pasta raiz do projeto)
    pasta_base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    caminho_completo = os.path.join(pasta_base, "imagens", nome_arquivo)

    imagem_carregada = pygame.image.load(caminho_completo).convert_alpha()
    
    if escala:
        imagem_carregada = pygame.transform.scale(imagem_carregada, escala)

    # Calcula alpha e deslocamento
    if estado_transicao == "Entrada" and transicao_entrada is not None:
        alfa = int(255 * progresso_transicao)
        deslocamento_y = 0
        if transicao_entrada == "desce":
            deslocamento_y = -50 * (1 - progresso_transicao)
        elif transicao_entrada == "sobe":
            deslocamento_y = 50 * (1 - progresso_transicao)

    elif estado_transicao == "Saida" and transicao_saida is not None:
        alfa = int(255 * (1 - progresso_transicao))
        deslocamento_y = 0
        if transicao_saida == "desce":
            deslocamento_y = 50 * progresso_transicao
        elif transicao_saida == "sobe":
            deslocamento_y = -50 * progresso_transicao

    else:  # visível
        alfa = 255
        deslocamento_y = 0

    imagem_carregada.set_alpha(alfa)
    ret = imagem_carregada.get_rect()

    y_animado = y + deslocamento_y

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
        ret.topleft = (x, y_animado)  # padrão

    tela.blit(imagem_carregada, ret)
