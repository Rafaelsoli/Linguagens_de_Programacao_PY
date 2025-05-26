import importlib
import pygame
import os

from slides.modulos.texto  import texto

pygame.init ()

largura, altura = 800, 600
tela = pygame.display.set_mode ((largura, altura), pygame.RESIZABLE)
pygame.display.set_caption ("Apresentação em Python")
relogio = pygame.time.Clock ()
tela_cheia = False

class SlideFinal:
    def iniciar (self):
        pass

    def atualizar (self, tela):
        tela.fill ((0, 0, 0))
        fonte = pygame.font.SysFont (None, 60)
        texto = fonte.render ("fim da apresentação", True, (255, 255, 255))
        ret = texto.get_rect (center = tela.get_rect ().center)
        tela.blit (texto, ret)

    def evento (self, evento):
        pass

def carregarSlides ():
    slides = []
    i = 0
    while True:
        caminho = f"slides.s{i}"
        try:
            modulo = importlib.import_module (caminho)
            slides.append (modulo)
            i += 1
        except ModuleNotFoundError:
            break
    slides.append (SlideFinal ())
    return slides

slides = carregarSlides ()
indice_slide = 0

def trocarSlide (transicao, novo_indice):
    transicao (novo_indice)

def transicaoNenhuma (novo_indice):
    global indice_slide
    if novo_indice >= 0 and novo_indice < len (slides):
        indice_slide = novo_indice
        slides[indice_slide].iniciar ()

def animarTransicao (slide_antigo, slide_novo, direcao):
    if direcao in ["direita", "esquerda"]:
        max_deslocamento = largura
    else:
        max_deslocamento = altura

    for deslocamento in range (0, max_deslocamento + 1, 40):
        tela.fill ((30, 30, 30))

        if direcao == "direita":
            x_antigo = - deslocamento
            y_antigo = 0
            x_novo = largura - deslocamento
            y_novo = 0

        elif direcao == "esquerda":
            x_antigo = deslocamento
            y_antigo = 0
            x_novo = - largura + deslocamento
            y_novo = 0

        elif direcao == "acima":
            x_antigo = 0
            y_antigo = deslocamento
            x_novo = 0
            y_novo = - altura + deslocamento

        elif direcao == "abaixo":
            x_antigo = 0
            y_antigo = - deslocamento
            x_novo = 0
            y_novo = altura - deslocamento

        superficie_antiga = pygame.Surface ((largura, altura))
        superficie_nova = pygame.Surface ((largura, altura))

        slide_antigo.atualizar (superficie_antiga)
        slide_novo.atualizar (superficie_nova)

        tela.blit (superficie_antiga, (x_antigo, y_antigo))
        tela.blit (superficie_nova, (x_novo, y_novo))

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

def transicaoSwipe (novo_indice):
    global indice_slide

    if novo_indice < 0 or novo_indice >= len (slides):
        return

    direcao = "abaixo" if novo_indice > indice_slide else "acima"

    slide_antigo = slides[indice_slide]
    slides[novo_indice].iniciar ()
    animarTransicao (slide_antigo, slides[novo_indice], direcao)
    indice_slide = novo_indice


if slides:
    slides[indice_slide].iniciar ()

executando = True
while executando:
    for evento in pygame.event.get ():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.VIDEORESIZE and not tela_cheia:
            largura, altura = evento.size
            tela = pygame.display.set_mode ((largura, altura), pygame.RESIZABLE)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                trocarSlide (transicaoArrastar, indice_slide + 1)
            elif evento.key == pygame.K_LEFT:
                trocarSlide (transicaoArrastar, indice_slide - 1)
            elif evento.key == pygame.K_F11:
                tela_cheia = not tela_cheia
                if tela_cheia:
                    tela = pygame.display.set_mode ((0, 0), pygame.FULLSCREEN)
                else:
                    tela = pygame.display.set_mode ((largura, altura), pygame.RESIZABLE)


        if slides:
            slides[indice_slide].evento (evento)

    tela.fill ((30, 30, 30))

    if slides:
        slides[indice_slide].atualizar (tela)

        if not isinstance (slides[indice_slide], SlideFinal):
            texto ( # Indice no slide
                f"{indice_slide + 1}", 
                "#FFFFFF", 24, "arial", largura - 10, altura - 10, "baixo_direita", tela,
                negrito=True,
                grossura_contorno=3,
                cor_contorno="#000000"
            )


    pygame.display.flip ()
    relogio.tick (60)

pygame.quit ()
