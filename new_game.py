import pygame
import math

pygame.init()

from game_file.game import Game

# INITIALISATION DE PYGAME
pygame.init()

# CREATION DE LA FENETRE
# LB Changer le titre de la fenêtre
pygame.display.set_caption("Quizz League of Legends")
# LB Dimensionner la fenêtre
screen = pygame.display.set_mode((1080, 720))



# CREATION DU MENU
# * HH importer et charger le background
background = pygame.image.load('asset/bg/bg_4.jpg')
background = pygame.transform.scale(background, (1080, 720))

# LB essai d'ecriture pour mettre les questions
variable = "Quel est le meilleur support"
font = pygame.font.Font(None, 36)
text = font.render(variable, 1, (55,55,55))


# CREATION DES VAR NESCESSAIRE
game = Game()
running = True

# Print le logo
lol = pygame.image.load('asset/button/LoL.png')
lol_rect = lol.get_rect()
lol_rect.x = 10
lol_rect.y = 10

# print le cadre du titre 
title = pygame.image.load('asset/button/title.png')
title = pygame.transform.scale(title, (700, 125))
title_rect = title.get_rect()
title_rect.x = lol.get_width() + 50
title_rect.y = math.ceil(screen.get_height() / 40)


# Print block basique sans validation
block = pygame.image.load('asset/button/block.png')
block_rect = block.get_rect()
block_rect.x = lol.get_width() + 50
block_rect.y = math.ceil(screen.get_height() / 35 + 250)


# Print block pour la bonne réponse
block_right = pygame.image.load('asset/button/block_right.png')
block_right_rect = block_right.get_rect()
block_right_rect.x = lol.get_width() + 50
block_right_rect.y = 0

# Print block pour mauvaise réponse
block_wrong = pygame.image.load('asset/button/block_wrong.png')
block_wrong_rect = block_wrong.get_rect()
block_wrong_rect.x = 0
block_wrong_rect.y = 0

# Print rond a cocher
round = pygame.image.load('asset/button/round.png')
round_rect = round.get_rect()
round_rect.x = lol.get_width()
round_rect.y = math.ceil(screen.get_height() / 35 + 256)

# Print rond coché
round_selected = pygame.image.load('asset/button/round_selected.png')
round_selected_rect = round_selected.get_rect()
round_selected_rect.x = 0
round_selected_rect.y = 0

# Print rectangle pour passer a la question suivante 
next = pygame.image.load('asset/button/next.png')
next_rect = next.get_rect()
next_rect.x = 0
next_rect.y = 0

# Print la case validation de la réponse
validation = pygame.image.load('asset/button/validation.png')
validation_rect = validation.get_rect()
validation_rect.x = screen.get_width() - 300
validation_rect.y = screen.get_height() - 140



running = True
# LB tant que le running est égal True, la fenêtre s'affiche

while running :
    # * HH appliquer le background
    screen.blit(background, (0,0))
    screen.blit(lol, lol_rect)
    screen.blit(title, title_rect)
    screen.blit(validation, validation_rect)
    
    #print les block réponse 4 fois 
    block_rect.y = math.ceil(screen.get_height() / 35 + 250)
    for loop in range (4) :
        screen.blit(block, block_rect)
        block_rect.y += 90 

    # Print les ronds réponse 4 fois
    round_rect.y = math.ceil(screen.get_height() / 35 + 256)
    for loop in range (4) :
        screen.blit(round, round_rect)
        round_rect.y += 90 


    



    
    for event in pygame.event.get() :
        # LB Si l'event généré par l'utilisateur est de quitter
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()


    # LB afficher un texte
    # screen.blit(text,(500, 60))

    # * HH update le screen
    pygame.display.flip()



