import pygame
import random

class EfeitoMatrix:

    def __init__ (self, largura, altura):
        self.largura_coluna = 20
        self.altura_linha = 20
        self.largura = largura
        self.altura = altura

        self.caracteres = "01010101010101010101010101010101012"

        self.colunas_fundo = []
        self.velocidades_fundo = []

        self.colunas_meio = []
        self.velocidades_meio = []

        self.colunas_frente = []
        self.velocidades_frente = []

        self.atualizarTamanho (largura, altura)

    def atualizarTamanho (self, largura, altura):
        self.largura = largura
        self.altura = altura

        num_colunas = self.largura // self.largura_coluna

        # Ajusta tamanho das listas para cobrir toda a largura
        while len (self.colunas_fundo) < num_colunas:
            self.colunas_fundo.append (random.randint (-self.altura * 2, -self.altura))
            self.velocidades_fundo.append (random.randint (1, 2))

            self.colunas_meio.append (random.randint (-self.altura * 2, -self.altura))
            self.velocidades_meio.append (random.randint (2, 4))

            self.colunas_frente.append (random.randint (-self.altura * 2, -self.altura))
            self.velocidades_frente.append (random.randint (3, 6))

        while len (self.colunas_fundo) > num_colunas:
            self.colunas_fundo.pop ()
            self.velocidades_fundo.pop ()

            self.colunas_meio.pop ()
            self.velocidades_meio.pop ()

            self.colunas_frente.pop ()
            self.velocidades_frente.pop ()

    def iniciar (self):
        self.colunas_fundo = [random.randint (-self.altura * 2, -self.altura) for _ in range (self.largura // self.largura_coluna)]
        self.velocidades_fundo = [random.randint (1, 2) for _ in range (self.largura // self.largura_coluna)]

        self.colunas_meio = [random.randint (-self.altura * 2, -self.altura) for _ in range (self.largura // self.largura_coluna)]
        self.velocidades_meio = [random.randint (2, 4) for _ in range (self.largura // self.largura_coluna)]

        self.colunas_frente = [random.randint (-self.altura * 2, -self.altura) for _ in range (self.largura // self.largura_coluna)]
        self.velocidades_frente = [random.randint (3, 6) for _ in range (self.largura // self.largura_coluna)]

    def atualizar (self, tela):
        self.atualizarTamanho (tela.get_width (), tela.get_height ())

        num_colunas = self.largura // self.largura_coluna
        tela.fill ((0, 0, 0))

        fonte_fundo = pygame.font.SysFont ("consolas", 14)
        fonte_meio = pygame.font.SysFont ("consolas", 18)
        fonte_frente = pygame.font.SysFont ("consolas", 20)

        cor_fundo = (0, 80, 20)
        cor_meio = (0, 150, 50)
        cor_frente = (0, 255, 70)

        for i in range (num_colunas):
            x = i * self.largura_coluna

            y_fundo = self.colunas_fundo[i]
            for j in range (0, self.altura, self.altura_linha):
                pos_y = y_fundo + j
                if pos_y >= 0:
                    char = random.choice (self.caracteres)
                    texto = fonte_fundo.render (char, True, cor_fundo)
                    tela.blit (texto, (x, pos_y))

            self.colunas_fundo[i] += self.velocidades_fundo[i]

            if self.colunas_fundo[i] > self.altura:
                self.colunas_fundo[i] = random.randint (-self.altura * 2, -self.altura)
                self.velocidades_fundo[i] = random.randint (1, 2)

            y_meio = self.colunas_meio[i]
            for j in range (0, self.altura, self.altura_linha):
                pos_y = y_meio + j
                if pos_y >= 0:
                    char = random.choice (self.caracteres)
                    texto = fonte_meio.render (char, True, cor_meio)
                    tela.blit (texto, (x, pos_y))

            self.colunas_meio[i] += self.velocidades_meio[i]

            if self.colunas_meio[i] > self.altura:
                self.colunas_meio[i] = random.randint (-self.altura * 2, -self.altura)
                self.velocidades_meio[i] = random.randint (2, 4)

            y_frente = self.colunas_frente[i]
            for j in range (0, self.altura, self.altura_linha * 2):
                pos_y = y_frente + j
                if pos_y >= 0:
                    char = random.choice (self.caracteres)
                    texto = fonte_frente.render (char, True, cor_frente)
                    tela.blit (texto, (x, pos_y))

            self.colunas_frente[i] += self.velocidades_frente[i]

            if self.colunas_frente[i] > self.altura:
                self.colunas_frente[i] = random.randint (-self.altura * 2, -self.altura)
                self.velocidades_frente[i] = random.randint (3, 6)
