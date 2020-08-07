# coding : utf-8

# IMPORT
import pygame
import math
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
background = pygame.image.load('asset/bg_quizz.png')
background = pygame.transform.scale(background, (1080, 720))

# LB essai d'ecriture pour mettre les questions
variable = "Quel est le meilleur support"
font = pygame.font.Font(None, 36)
text = font.render(variable, 1, (55,55,55))



# * HH import des boutons du menu
play_button = pygame.image.load('asset/new_game.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 4) - 50
play_button_rect.y = math.ceil(screen.get_height() / 2)

score_button = pygame.image.load('asset/score.png')
score_button_rect = play_button.get_rect()
score_button_rect.x = math.ceil(screen.get_width() / 4) * 2 + 50
score_button_rect.y = math.ceil(screen.get_height() / 2)

# * HH Charge la Favicon
icon_32x32 = pygame.image.load("asset/favicon.png").convert_alpha()
# * HH Applique la Favicon
pygame.display.set_icon(icon_32x32)

# CREATION DES VAR NESCESSAIRE
game = Game()
running = True

# LB tant que le running est égal True, la fenêtre s'affiche
while running :
    # * HH appliquer le background
    screen.blit(background, (0,0))
    
    if game.is_playing:
        pass
    else:
        # * HH ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(score_button, score_button_rect)

    for event in pygame.event.get() :
        # LB Si l'event généré par l'utilisateur est de quitter
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # * HH verifier que lors du click de la souris, on est bien sur les boutons
            if play_button_rect.collidepoint(event.pos):
                game.is_playing = True

            if score_button_rect.collidepoint(event.pos):
                print("lancer les scores")

    # LB afficher un texte
    # screen.blit(text,(500, 60))

    # * HH update le screen
    pygame.display.flip()

