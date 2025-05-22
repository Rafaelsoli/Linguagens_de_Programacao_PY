import pygame

def transicaoNenhuma (novo_indice):
    global indice_slide
    if novo_indice >= 0 and novo_indice < len (slides):
        indice_slide = novo_indice
        slides[indice_slide].iniciar ()

def animarTransicao (slide_antigo, slide_novo, direcao):
    for deslocamento in range (0, largura + 1, 40):
        tela.fill ((30, 30, 30))

        if direcao == "direita":
            pos_antigo = - deslocamento
            pos_novo = largura - deslocamento
        else:
            pos_antigo = deslocamento
            pos_novo = - largura + deslocamento

        superficie_antiga = pygame.Surface ((largura, altura))
        superficie_nova = pygame.Surface ((largura, altura))

        slide_antigo.atualizar (superficie_antiga)
        slide_novo.atualizar (superficie_nova)

        tela.blit (superficie_antiga, (pos_antigo, 0))
        tela.blit (superficie_nova, (pos_novo, 0))

        pygame.display.flip ()
        relogio.tick (60)

def transicaoArrastar (novo_indice):
    global indice_slide

    if novo_indice < 0 or novo_indice >= len (slides):
        return

    direcao = "direita" if novo_indice > indice_slide else "esquerda"

    slide_antigo = slides[indice_slide]
    slides[novo_indice].iniciar ()
    animarTransicao (slide_antigo, slides[novo_indice], direcao)
    indice_slide = novo_indice