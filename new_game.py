import pygame
import math

pygame.init()

background = pygame.image.load('asset/bg_quizz.png')
background = pygame.transform.scale(background, (1080, 720))

pygame.display.set_caption("Quizz League of Legends")
# LB Dimensionner la fenêtre
screen = pygame.display.set_mode((1080, 720))

lol = pygame.image.load('asset/LoL.png')
lol_rect = lol.get_rect()
# lol_rect.x = math.ceil(screen.)

running = True

while running :
    # * HH appliquer le background
    screen.blit(background, (0,0))
    

    for event in pygame.event.get() :
        # LB Si l'event généré par l'utilisateur est de quitter
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()

        screen.blit(lol, lol_rect)

