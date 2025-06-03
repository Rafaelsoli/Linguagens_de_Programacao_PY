import pygame
import threading
import time
from flask import Flask, request
import random

app = Flask (__name__)

bola_posicao = 0.0
bola_velocidade = 300.0
rebateu = False
limite_tela = 600
jogo_ativo = True

mensagem = ""
tempo_mensagem = 0
cor_mensagem = (255, 255, 255)

@app.route ("/comando", methods=["POST"])
def receberComando ():
    global rebateu
    global bola_posicao
    global mensagem
    global tempo_mensagem
    global cor_mensagem

    comando = request.form.get ("acao")
    print ("Recebido comando:", comando)
    print ("Posição atual da bola:", bola_posicao)

    if comando == "pong":
        if 500 <= bola_posicao <= 600:
            rebateu = True
            mensagem = "ACERTOU!"
            cor_mensagem = (0, 255, 0)
            tempo_mensagem = time.time ()
            return "Rebatida registrada!", 200
        elif bola_posicao < 500:
            mensagem = "CEDO DEMAIS!"
            cor_mensagem = (0, 150, 255)
            tempo_mensagem = time.time ()
            pygame.mixer.Sound ("pong_cedo.wav").play ()
            return "Cedo demais!", 400
        else:
            mensagem = "ERROU!"
            cor_mensagem = (255, 0, 0)
            tempo_mensagem = time.time ()
            pygame.mixer.Sound ("pong_erro.wav").play ()
            return "Muito tarde!", 400
    else:
        return "Comando inválido", 400

def iniciarServidor ():
    app.run (host="0.0.0.0", port=5002)

def desenharFundo (tela):
    for y in range (600):
        r = min (int (y * 0.3), 255)
        g = min (int (y * 0.4), 255)
        b = min (int (y * 0.6), 255)
        pygame.draw.line (tela, (r, g, b), (0, y), (800, y))


def iniciarJogo ():
    global bola_posicao
    global rebateu
    global jogo_ativo
    global mensagem
    global tempo_mensagem
    global cor_mensagem

    pygame.init ()
    tela = pygame.display.set_mode ((800, 600))
    pygame.display.set_caption ("Pong POV")
    clock = pygame.time.Clock ()

    fonte = pygame.font.SysFont ("Courier New", 32, bold=True)
    fonte_mensagem = pygame.font.SysFont ("Courier New", 48, bold=True)

    som_rebate = pygame.mixer.Sound ("pong_rebate.wav")
    pygame.mixer.music.load ("fundo.mp3")
    pygame.mixer.music.play (-1)

    bola_posicao = 0.0

    while jogo_ativo:
        tempo = clock.tick (60) / 1000.0

        for evento in pygame.event.get ():
            if evento.type == pygame.QUIT:
                jogo_ativo = False

        if rebateu:
            som_rebate.play ()
            bola_posicao = 0.0
            rebateu = False
        else:
            bola_posicao += bola_velocidade * tempo

            if bola_posicao >= limite_tela:
                mensagem = "ERROU!"
                cor_mensagem = (255, 0, 0)
                tempo_mensagem = time.time ()
                pygame.mixer.Sound ("pong_erro.wav").play ()
                bola_posicao = 0.0

        desenharFundo (tela)

        raio = int (20 + bola_posicao / 30)
        sombra = pygame.Surface ((raio * 2, raio * 2), pygame.SRCALPHA)
        pygame.draw.circle (sombra, (0, 0, 0, 80), (raio, raio), raio)
        tela.blit (sombra, (400 - raio + 4, 300 - raio + 4))

        pygame.draw.circle (tela, (255, 255, 255), (400, 300), raio)

        texto = fonte.render (f"Distância: {int (limite_tela - bola_posicao)}", True, (255, 255, 255))
        tela.blit (texto, (10, 10))

        if time.time () - tempo_mensagem <= 0.7:
            render_msg = fonte_mensagem.render (mensagem, True, cor_mensagem)
            rect = render_msg.get_rect (center=(400, 50))
            tela.blit (render_msg, rect)

        pygame.display.flip ()

    pygame.quit ()

thread_servidor = threading.Thread (target=iniciarServidor)
thread_servidor.daemon = True
thread_servidor.start ()

iniciarJogo ()
