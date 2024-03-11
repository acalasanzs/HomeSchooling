import pygame, sys, random, time

pygame.init()

width = 800
height = 600
pygame.display.set_caption("Juego de la serpiente de Cairo")
pantalla = pygame.display.set_mode((width, height))
blanco = (255, 255, 255)
verde = (0, 255, 0)
serpiente = {
    "posicion": [100, 50],
    "cuerpo": [[100, 50], [90, 50], [80, 50]] 
}
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for pos in serpiente["cuerpo"]:
        pygame.draw.rect(pantalla, verde, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(pantalla, blanco, pygame.Rect(400, 300, 10, 10))
    pygame.display.update()
