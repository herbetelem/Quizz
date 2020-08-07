# coding : utf-8

# * import des libs
import pygame
import math
from game_file.variable_load import Variable_load

# créer la classe game
class Game:
    
    def __init__(self, screen):

        # * definir si le jeu a commencer ou pas
        self.is_playing = False
        # * 
        self.background = pygame.image.load('asset/bg/bg_5.jpg')
        self.background = pygame.transform.scale(self.background, (1080, 720))
        # création de la class variable
        self.variable_load = Variable_load(screen)
    # update l'écran
    def update(self, screen):

        screen.blit(self.variable_load.lol, self.variable_load.lol_rect)
        screen.blit(self.variable_load.title, self.variable_load.title_rect)
        screen.blit(self.variable_load.validation, self.variable_load.validation_rect)
        
        #print les block réponse 4 fois 
        self.variable_load.block_rect.y = math.ceil(screen.get_height() / 35 + 215)
        for loop in range (4) :
            screen.blit(self.variable_load.block, self.variable_load.block_rect)
            self.variable_load.block_rect.y += 110 

        # Print les ronds réponse 4 fois
        self.variable_load.round_rect.y = math.ceil(screen.get_height() / 35 + 225)
        for loop in range (4) :
            screen.blit(self.variable_load.round, self.variable_load.round_rect)
            self.variable_load.round_rect.y += 110 