import pygame

def iniciar ():
    pass

def atualizar (tela):
    tela.fill ((20, 20, 30))

    largura, altura = tela.get_size ()
    cx, cy = largura // 2, altura // 2

    fonte_titulo = pygame.font.SysFont ("arial", 48, bold = True)
    fonte_corpo = pygame.font.SysFont ("consolas", 28)
    fonte_destaque = pygame.font.SysFont ("consolas", 28, italic = True)

    # Título
    titulo = fonte_titulo.render ("Tratamento de Texto em Slides", True, (255, 255, 255))
    ret_titulo = titulo.get_rect (center = (cx, 70))
    tela.blit (titulo, ret_titulo)

    # Bloco de dicas
    dicas = [
        ("1. Use fontes com bom contraste", (200, 200, 200)),
        ("2. Centralize ou alinhe bem o texto", (200, 200, 200)),
        ("3. Use negrito e itálico para destaque", (255, 180, 120)),
        ("4. Cuidado com fontes grandes demais", (180, 255, 180)),
        ("5. Você pode usar diferentes fontes", (180, 180, 255)),
        ("6. Pode posicionar livremente", (255, 180, 255))
    ]

    y = 150
    for texto, cor in dicas:
        bloco = fonte_corpo.render (texto, True, cor)
        tela.blit (bloco, (80, y))
        y += 40

    # Exemplo de itálico
    exemplo = fonte_destaque.render ("Exemplo em itálico", True, (255, 255, 100))
    tela.blit (exemplo, (largura - 280, altura - 60))

def evento (evento):
    pass
