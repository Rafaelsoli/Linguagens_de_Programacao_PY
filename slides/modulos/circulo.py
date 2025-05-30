import pygame

def circulo (cor, raio, x, y, alinhamento, grossura, tela):
    if isinstance (cor, str):
        cor = pygame.Color (cor)
     

    diametro = raio * 2
    centro_x = x
    centro_y = y

    if alinhamento == "top_esquerda":
        centro_x = x + raio
        centro_y = y + raio
     
    elif alinhamento == "top_direita":
        centro_x = x - raio
        centro_y = y + raio
     
    elif alinhamento == "baixo_direita":
        centro_x = x - raio
        centro_y = y - raio
     
    elif alinhamento == "baixo_esquerda":
        centro_x = x + raio
        centro_y = y - raio
     
    elif alinhamento == "esquerda":
        centro_x = x + raio
     
    elif alinhamento == "direita":
        centro_x = x - raio
     
    elif alinhamento == "top":
        centro_y = y + raio
     
    elif alinhamento == "baixo":
        centro_y = y - raio
     

    pygame.draw.circle (tela, cor, (centro_x, centro_y), raio, grossura)
 
