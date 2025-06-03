import importlib
import pygame

from slides.modulos.texto  import texto

pygame.init ()

largura, altura = 1280, 720
tela = pygame.display.set_mode ((largura, altura), pygame.RESIZABLE)
pygame.display.set_caption ("Apresentação em Python")
relogio = pygame.time.Clock ()
tela_cheia = False

class SlideFinal:
    def iniciar (self):
        pass

    def atualizar(self, tela, estado, progresso_transicao):
        tela.fill((0, 0, 0))
        texto(
            "fim da apresentação",
            cor=(255, 255, 255),
            tamanho=60,
            fonte="arial",
            x=tela.get_width() // 2,
            y=tela.get_height() // 2,
            alinhamento="centro",
            tela=tela,
            estado_transicao=estado.lower(),
            progresso_transicao=progresso_transicao
        )

    def evento (self, evento):
        if evento.type == pygame.KEYDOWN:
            if transicao_pendente is None:
                if evento.key == pygame.K_RETURN: # Pressionar ENTER no slide final finaliza a apresentação
                    pygame.quit ()

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

        slide_antigo.atualizar (superficie_antiga, "Saida")
        slide_novo.atualizar (superficie_nova, "Entrada")

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


transicao_pendente = None
tempo_inicio_transicao = 0
delay_transicao = 500  # em milissegundos (1 segundo)

while executando:
    for evento in pygame.event.get ():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.VIDEORESIZE and not tela_cheia:
            largura, altura = evento.size
            tela = pygame.display.set_mode ((largura, altura), pygame.RESIZABLE)
        elif evento.type == pygame.KEYDOWN:
            if transicao_pendente is None:
                if evento.key == pygame.K_RIGHT:
                    transicao_pendente = ("direita", indice_slide + 1)
                    tempo_inicio_transicao = pygame.time.get_ticks ()
                elif evento.key == pygame.K_LEFT:
                    transicao_pendente = ("esquerda", indice_slide - 1)
                    tempo_inicio_transicao = pygame.time.get_ticks ()

            if evento.key == pygame.K_F11:
                tela_cheia = not tela_cheia
                if tela_cheia:
                    tela = pygame.display.set_mode ((0, 0), pygame.FULLSCREEN)
                else:
                    tela = pygame.display.set_mode ((largura, altura), pygame.RESIZABLE)

        if slides:
            slides[indice_slide].evento (evento)

    tela.fill ((30, 30, 30))

    if slides:
        progresso_transicao = 1.0  # padrão

        if transicao_pendente is not None:
            agora = pygame.time.get_ticks()
            tempo_decorrido = agora - tempo_inicio_transicao
            if tempo_decorrido < delay_transicao:
                estado_slide = "Saida"
                progresso_transicao = tempo_decorrido / delay_transicao
            else:
                direcao, novo_indice = transicao_pendente
                trocarSlide(transicaoNenhuma, novo_indice)
                transicao_pendente = None
                estado_slide = "Entrada"
                tempo_inicio_transicao = pygame.time.get_ticks()
                progresso_transicao = 0.0
        else:
            agora = pygame.time.get_ticks()
            if tempo_inicio_transicao > 0:
                tempo_decorrido = agora - tempo_inicio_transicao
                if tempo_decorrido < delay_transicao:
                    estado_slide = "Entrada"
                    progresso_transicao = tempo_decorrido / delay_transicao
                else:
                    estado_slide = "Meio"
                    progresso_transicao = 1.0
            else:
                estado_slide = "Meio"
                progresso_transicao = 1.0

        slides[indice_slide].atualizar(tela, estado_slide, progresso_transicao)




        ### INDICE
        #if not isinstance (slides[indice_slide], SlideFinal):
        #    texto ( # Indice no slide
        #        f"{indice_slide + 1}", 
        #        "#FFFFFF", 24, "arial", largura - 10, altura - 10, "baixo_direita", tela,
        #        negrito=True,
        #        grossura_contorno=3,
        #        cor_contorno="#000000"
        #    )

    #if transicao_pendente is not None:
    #    agora = pygame.time.get_ticks ()
    #    if agora - tempo_inicio_transicao >= delay_transicao:
    #        direcao, novo_indice = transicao_pendente
    #        trocarSlide (transicaoNenhuma, novo_indice)
    #        transicao_pendente = None

    pygame.display.flip ()
    relogio.tick (60)

pygame.quit ()
