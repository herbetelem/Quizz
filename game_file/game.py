# coding : utf-8

# * import des libs
import pygame
import math
from game_file.variable_load import Variable_load
from game_file.sql_function import SQL_request

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
        # création de la class SQL
        self.sql_request = SQL_request()

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

        self.update_question(screen)

    def update_question(self, screen):

        # importer la question 
        counter = 1
        self.sql_request.read_question(counter)
        variable = self.sql_request.question_tmp[1]
        # print la question
        font = pygame.font.Font(None, 35)
        text = font.render(variable, 1, (255,255,255))
        text_rect = text.get_rect()
        # Positionner la question
        text_rect.x = self.variable_load.lol.get_width() + 70
        text_rect.y = math.ceil((screen.get_height() / 40) + (self.variable_load.title.get_height() / 2) - 15 )

        # importer les questions 
        self.sql_request.read_answer(counter)
        variable = self.sql_request.question_tmp


        



        screen.blit(text, text_rect)