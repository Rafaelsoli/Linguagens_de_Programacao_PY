import pygame
import fitz
import threading
from flask import Flask, request

app = Flask (__name__)
comando_recebido = None

def carregarPaginas (caminho_pdf):
    documento = fitz.open (caminho_pdf)
    paginas = []

    for indice in range (len (documento)):
        pagina = documento.load_page (indice)
        imagem = pagina.get_pixmap ()
        modo = "RGB" if imagem.alpha == 0 else "RGBA"
        dados = pygame.image.frombuffer (imagem.samples, (imagem.width, imagem.height), modo)
        paginas.append (dados)

    return paginas

def redimensionarCentralizar (imagem_original, tamanho_janela):
    largura_janela, altura_janela = tamanho_janela
    largura_img, altura_img = imagem_original.get_size ()

    proporcao = min (largura_janela / largura_img, altura_janela / altura_img)
    nova_largura = int (largura_img * proporcao)
    nova_altura = int (altura_img * proporcao)

    imagem_redimensionada = pygame.transform.smoothscale (imagem_original, (nova_largura, nova_altura))
    superficie = pygame.Surface (tamanho_janela)
    superficie.fill ((0, 0, 0))

    pos_x = (largura_janela - nova_largura) // 2
    pos_y = (altura_janela - nova_altura) // 2

    superficie.blit (imagem_redimensionada, (pos_x, pos_y))

    return superficie

def iniciarServidor ():
    app.run (host="0.0.0.0", port=5000)

@app.route ("/comando", methods=["POST"])
def receberComando ():
    global comando_recebido
    comando = request.form.get ("acao")

    if comando in ["left", "right"]:
        comando_recebido = comando
        print ("Recebido comando:", comando)

    return "OK"

def exibirSlides (paginas):
    global comando_recebido

    pygame.init ()
    tamanho_janela = (800, 600)
    modo_tela = pygame.RESIZABLE
    tela = pygame.display.set_mode (tamanho_janela, modo_tela)
    pygame.display.set_caption ("Visualizador de PDF")

    indice_atual = 0
    relogio = pygame.time.Clock ()
    rodando = True

    imagem = redimensionarCentralizar (paginas[indice_atual], tamanho_janela)
    tela.blit (imagem, (0, 0))
    pygame.display.flip ()

    while rodando:
        for evento in pygame.event.get ():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    comando_recebido = "right"
                elif evento.key == pygame.K_LEFT:
                    comando_recebido = "left"
                elif evento.key == pygame.K_F11:
                    if modo_tela == pygame.FULLSCREEN:
                        modo_tela = pygame.RESIZABLE
                        tela = pygame.display.set_mode (tamanho_janela, modo_tela)
                    else:
                        modo_tela = pygame.FULLSCREEN
                        tamanho_janela = pygame.display.get_desktop_sizes ()[0]
                        tela = pygame.display.set_mode (tamanho_janela, modo_tela)

            elif evento.type == pygame.VIDEORESIZE and modo_tela != pygame.FULLSCREEN:
                tamanho_janela = evento.size
                tela = pygame.display.set_mode (tamanho_janela, modo_tela)

        if (comando_recebido == "right" and indice_atual < len (paginas) - 1) or (comando_recebido == "left" and indice_atual > 0):
            if comando_recebido == "right":
                indice_atual += 1
            elif comando_recebido == "left":
                indice_atual -= 1

            comando_recebido = None

        imagem = redimensionarCentralizar (paginas[indice_atual], tela.get_size ())
        tela.blit (imagem, (0, 0))
        pygame.display.flip ()

        relogio.tick (60)

    pygame.quit ()

if __name__ == "__main__":
    caminho = "slides.pdf"
    paginas_carregadas = carregarPaginas (caminho)

    servidor_thread = threading.Thread (target=iniciarServidor)
    servidor_thread.daemon = True
    servidor_thread.start ()

    exibirSlides (paginas_carregadas)
