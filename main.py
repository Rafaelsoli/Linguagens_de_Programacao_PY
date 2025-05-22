import importlib
import pygame
import os

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

    pygame.display.flip ()
    relogio.tick (60)

pygame.quit ()
