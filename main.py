import pygame
pygame.init()

# Changer le titre de la fenêtre
pygame.display.set_caption("Quizz League of Legends")
# Dimensionner la fenêtre
screen = pygame.display.set_mode((1080, 720))

running = True

# tant que le running est égal True, la fenêtre s'affiche
while running :
    screen

    for event in pygame.event.get() :
        # Si l'event généré par l'utilisateur est de quitter
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()

