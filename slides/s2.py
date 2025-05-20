import pygame

texto_piscando = None
texto_deslizando = None
texto_aumentando = None
texto_arrastavel = None

opacidade = 255
direcao_opacidade = -5

x_deslizante = -300

tamanho_fonte_animada = 20
subindo = True

pos_texto_arrastavel = [300, 400]
arrastando = False
offset = (0, 0)

def iniciar ():
    global texto_piscando, texto_deslizando, texto_aumentando, texto_arrastavel
    texto_piscando = pygame.font.SysFont ("arial", 36).render ("Texto que pisca", True, (255, 255, 255))
    texto_deslizando = pygame.font.SysFont ("arial", 36).render ("Texto que desliza", True, (100, 200, 255))
    texto_arrastavel = pygame.font.SysFont ("arial", 36).render ("Arraste este texto", True, (255, 180, 100))

def atualizar (tela):
    global opacidade, direcao_opacidade
    global x_deslizante
    global tamanho_fonte_animada, subindo

    tela.fill ((15, 15, 25))
    largura, altura = tela.get_size ()

    # Texto piscando
    superficie_pisca = texto_piscando.copy ()
    opacidade += direcao_opacidade
    if opacidade <= 50 or opacidade >= 255:
        direcao_opacidade *= -1
    superficie_pisca.set_alpha (opacidade)
    tela.blit (superficie_pisca, (50, 80))

    # Texto deslizando
    x_deslizante += 2
    if x_deslizante > largura:
        x_deslizante = -texto_deslizando.get_width ()
    tela.blit (texto_deslizando, (x_deslizante, 150))

    # Texto com tamanho animado
    if subindo:
        tamanho_fonte_animada += 1
        if tamanho_fonte_animada > 48:
            subindo = False
    else:
        tamanho_fonte_animada -= 1
        if tamanho_fonte_animada < 24:
            subindo = True

    fonte_animada = pygame.font.SysFont ("arial", tamanho_fonte_animada)
    texto_animado = fonte_animada.render ("Texto pulsante", True, (180, 255, 180))
    tela.blit (texto_animado, (50, 250))

    # Texto arrastável
    tela.blit (texto_arrastavel, pos_texto_arrastavel)

def evento (evento):
    global arrastando, offset, pos_texto_arrastavel

    if evento.type == pygame.MOUSEBUTTONDOWN:
        ret = pygame.Rect (*pos_texto_arrastavel, texto_arrastavel.get_width (), texto_arrastavel.get_height ())
        if ret.collidepoint (evento.pos):
            arrastando = True
            offset = (evento.pos[0] - pos_texto_arrastavel[0], evento.pos[1] - pos_texto_arrastavel[1])

    elif evento.type == pygame.MOUSEBUTTONUP:
        arrastando = False

    elif evento.type == pygame.MOUSEMOTION and arrastando:
        pos_texto_arrastavel = [evento.pos[0] - offset[0], evento.pos[1] - offset[1]]
