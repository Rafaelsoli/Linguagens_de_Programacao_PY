import threading
from flask import Flask, request
import pygame

app = Flask(__name__)
comando_recebido = None

@app.route("/comando", methods=["POST"])
def receber_comando():
    global comando_recebido
    comando = request.form.get("acao")
    print(f"Comando recebido: {comando}")
    comando_recebido = comando
    return "OK"

def iniciar_flask():
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)

def iniciar_pygame():
    global comando_recebido

    pygame.init()
    tela = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    largura, altura = tela.get_size()

    clock = pygame.time.Clock()

    def novo_jogo():
        return [["" for _ in range(3)] for _ in range(3)], "X", [0, 0], False, None

    tabuleiro, jogador, cursor, fim_de_jogo, vencedor = novo_jogo()
    fonte = pygame.font.SysFont(None, altura // 6)

    def desenhar_tabuleiro():
        tela.fill((255, 255, 255))
        cell_w = largura // 3
        cell_h = altura // 3

        for i in range(1, 3):
            pygame.draw.line(tela, (0, 0, 0), (0, i * cell_h), (largura, i * cell_h), 5)
            pygame.draw.line(tela, (0, 0, 0), (i * cell_w, 0), (i * cell_w, altura), 5)

        for linha in range(3):
            for col in range(3):
                if tabuleiro[linha][col]:
                    texto = fonte.render(tabuleiro[linha][col], True, (0, 0, 0))
                    rect = texto.get_rect(center=((col + 0.5) * cell_w, (linha + 0.5) * cell_h))
                    tela.blit(texto, rect)

        if not fim_de_jogo:
            pygame.draw.rect(tela, (255, 0, 0), (cursor[1] * cell_w, cursor[0] * cell_h, cell_w, cell_h), 5)

        if fim_de_jogo:
            cor = (0, 128, 0) if vencedor else (128, 0, 0)
            msg = f"{vencedor} venceu!" if vencedor else "Empate!"
            texto = fonte.render(msg, True, cor)
            rect = texto.get_rect(center=(largura // 2, altura // 2))
            tela.blit(texto, rect)

        pygame.display.flip()

    def verificar_vitoria():
        for i in range(3):
            if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != "":
                return tabuleiro[i][0]
            if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != "":
                return tabuleiro[0][i]
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
            return tabuleiro[0][0]
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
            return tabuleiro[0][2]
        return None

    def jogo_cheio():
        return all(tabuleiro[i][j] != "" for i in range(3) for j in range(3))

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                rodando = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN and fim_de_jogo:
                # Reinicia o jogo
                tabuleiro, jogador, cursor, fim_de_jogo, vencedor = novo_jogo()

        if comando_recebido:
            cmd = comando_recebido
            comando_recebido = None

            if not fim_de_jogo:
                if cmd == "acima":
                    cursor[0] = (cursor[0] - 1) % 3
                elif cmd == "abaixo":
                    cursor[0] = (cursor[0] + 1) % 3
                elif cmd == "esquerda":
                    cursor[1] = (cursor[1] - 1) % 3
                elif cmd == "direita":
                    cursor[1] = (cursor[1] + 1) % 3
                elif cmd == "aqui":
                    l, c = cursor
                    if tabuleiro[l][c] == "":
                        tabuleiro[l][c] = jogador
                        vencedor = verificar_vitoria()
                        if vencedor or jogo_cheio():
                            fim_de_jogo = True
                        else:
                            jogador = "O" if jogador == "X" else "X"

        desenhar_tabuleiro()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    threading.Thread(target=iniciar_flask, daemon=True).start()
    iniciar_pygame()
