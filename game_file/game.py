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
        self.list_background = ['asset/bg/bg_quizz.png', 'asset/bg/bg_1.jpg', 'asset/bg/bg_2.jpg', 'asset/bg/bg_3.jpg', 'asset/bg/bg_4.jpg', 'asset/bg/bg_5.jpg','asset/bg/bg_5.jpg']
        self.background = pygame.image.load(self.list_background[0])
        self.background = pygame.transform.scale(self.background, (1080, 720))
        # création de la class variable
        self.variable_load = Variable_load(screen)
        # création de la class SQL
        self.sql_request = SQL_request()
        # Savoir sur quel rond l'utilisateur a cliqué
        self.round1 = False
        self.round2 = False
        self.round3 = False
        self.round4 = False
        # Choisir la question
        self.question = 5
        # Validation pour savoir si on peut passer a la question suivante
        self.round_check = False

    # update l'écran
    def update(self, screen):
        
        # * afficher le background de la question
        self.background = pygame.image.load(self.list_background[self.question])
        self.background = pygame.transform.scale(self.background, (1080, 720))

        screen.blit(self.variable_load.lol, self.variable_load.lol_rect)
        screen.blit(self.variable_load.title, self.variable_load.title_rect)
        screen.blit(self.variable_load.validation, self.variable_load.validation_rect)
        
        #print les block réponse 4 fois 
        self.variable_load.block_rect.y = math.ceil(screen.get_height() / 35 + 215)
        for loop in range (4) :
            screen.blit(self.variable_load.block, self.variable_load.block_rect)
            self.variable_load.block_rect.y += 110 

        #print les ronds 4 fois
        if self.round1 == False :
            screen.blit(self.variable_load.round1, self.variable_load.round1_rect)
        else :
            screen.blit(self.variable_load.round_selected, self.variable_load.round1_rect)

        if self.round2 == False :
            screen.blit(self.variable_load.round2, self.variable_load.round2_rect)
        else :
            screen.blit(self.variable_load.round_selected, self.variable_load.round2_rect)

        if self.round3 == False :
            screen.blit(self.variable_load.round3, self.variable_load.round3_rect)
        else :
            screen.blit(self.variable_load.round_selected, self.variable_load.round3_rect)

        if self.round4 == False :
            screen.blit(self.variable_load.round4, self.variable_load.round4_rect)
        else :
            screen.blit(self.variable_load.round_selected, self.variable_load.round4_rect)
            
        # Pour changer la question
        if self.round1 == True or self.round2 == True or self.round3 == True or self.round4 == True:
            self.round_check = True
        
        self.update_question(screen)

    def update_question(self, screen):

        # importer la question 
        
        self.sql_request.read_question(self.question)
        variable = self.sql_request.question_tmp[1]
        # print la question
        font = pygame.font.Font(None, 35)
        text = font.render(variable, 1, (255,255,255))
        text_rect = text.get_rect()
        # Positionner la question
        text_rect.x = self.variable_load.lol.get_width() + 70
        text_rect.y = math.ceil((screen.get_height() / 40) + (self.variable_load.title.get_height() / 2) - 15 )
        screen.blit(text, text_rect)

        # importer les questions 
        counter = 0
        self.sql_request.read_answer(self.question)
        variable = self.sql_request.anwser_tmp
        text = font.render(variable[counter][2], 1, (255,255,255))
        text_rect.x = self.variable_load.lol.get_width() + 100
        text_rect.y = math.ceil(screen.get_height() / 35 + 237)
        

        for loop in range (4) :

            text = font.render(variable[counter][2], 1, (255,255,255))
            screen.blit(text, text_rect)
            text_rect.y += 110           
            counter += 1


        

        



    