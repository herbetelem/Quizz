# coding : utf-8

# * import des libs
import pygame
import math
from game_file.variable_load import Variable_load
from game_file.sql_function import SQL_request
from game_file.model_button import Model_button


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
        # Choisir la question
        self.question = 1
        # Validation pour savoir si on peut passer a la question suivante
        self.round_check = False
        # * choix du joueur
        self.choice_player = 0
        self.player_validated = False
        # définir le nombre de bonne réponse du joueur
        self.round1 = False
        self.round2 = False
        self.round3 = False
        self.round4 = False
        self.score = 0
        self.player_name = "Alain"
        self.list_bloc = []
        self.list_round = [self.round1, self.round2, self.round3, self.round4]
        # * son
        self.sound_win = pygame.mixer.Sound("asset/music/true.ogg")
        self.sound_loose = pygame.mixer.Sound("asset/music/wrong.ogg")
        
        # * appeller la fonction pour creer les blocs
        self.create_bloc(screen)
        self.player = True


    # update l'écran
    def update(self, screen):
        
        if self.player:
            # * afficher le background de la question
            self.background = pygame.image.load(self.list_background[self.question])
            self.background = pygame.transform.scale(self.background, (1080, 720))

            # afficher le logo, le bloc de la question et les bloc reponse et next
            screen.blit(self.variable_load.lol, self.variable_load.lol_rect)
            screen.blit(self.variable_load.title, self.variable_load.title_rect)
            if self.choice_player > 0 and self.player_validated == False:
                screen.blit(self.variable_load.validation, self.variable_load.validation_rect)
            if self.player_validated:
                screen.blit(self.variable_load.next, self.variable_load.next_rect)
            
            # * afficher les bloc
            for bloc in self.list_bloc:
                screen.blit(bloc.image, bloc.rect)

            #print les block réponse 4 fois 
            # self.variable_load.block_rect.y = math.ceil(screen.get_height() / 35 + 215)
            # for loop in range (4) :
            #     screen.blit(self.variable_load.block, self.variable_load.block_rect)
            #     self.variable_load.block_rect.y += 110

            #print les ronds 4 fois
            self.variable_load.round1_rect.y = math.ceil(screen.get_height() / 35 + 225)
            for round in range (4) :

                if self.list_round[round] == False :
                    screen.blit(self.variable_load.round1, self.variable_load.round1_rect)
                else :
                    screen.blit(self.variable_load.round_selected, self.variable_load.round1_rect)
                self.variable_load.round1_rect.y += 110

            # Pour changer la question
            if self.list_round[0] == True or self.list_round[1] == True or self.list_round[2] == True or self.list_round[3] == True:
                self.round_check = True
            
            self.update_question(screen)
        else:
            self.champ_select(screen)

    def update_question(self, screen):

        # importer la question 
        self.sql_request.read_question(self.question)
        variable = self.sql_request.question_tmp[1]
        self.correct_answer = self.sql_request.question_tmp[2]
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
        
        # afficher les texte des question
        for text in range (4) :
            text = font.render(variable[counter][2], 1, (255,255,255))
            screen.blit(text, text_rect)
            text_rect.y += 110           
            counter += 1


    def create_bloc(self, screen):
        y = math.ceil(screen.get_height() / 35 + 215)
        x = self.variable_load.lol.get_width() + 50
        for bloc in range (4) :
            bloc = Model_button(x, y)
            self.list_bloc.append(bloc)
            y += 110


    # * fonction qui verifie la reponse du joueur
    def check_answer(self):
        # * je dit que le joueur a bien entrer une reponse
        self.player_validated = True
        # * je check que la reponse et celle du joueur soit identiques
        if self.choice_player == self.correct_answer:
            self.result_turn = True
            # * je lance la musique
            self.launch_music("asset/music/true.ogg")
            self.score += 1
        else :
            self.result_turn = False
            # * je lance la musique
            self.launch_music("asset/music/wrong.ogg")
        self.change_bloc(self.correct_answer)
        
        
    # * changer l'attribut image des bloc en fonction des bonnes reponse
    def change_bloc(self, index):
        index -= 1
        for index_bloc in range(4):
            if index_bloc == index:
                self.list_bloc[index_bloc].image = pygame.image.load('asset/button/block_right.png')
            else:
                self.list_bloc[index_bloc].image = pygame.image.load('asset/button/block_wrong.png')

    def change_round(self, index):
        
        for round in range(4):
            if round == index - 1 :
                self.list_round[round] = True 
            else :
                self.list_round[round] = False
    
    # * lancer la musique et gerer le volume
    def launch_music(self, music_path):
        pygame.mixer.init()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.05)
        
    def next_question(self):
        self.question += 1
        self.choice_player = 0
        self.round_check = False
        for round in range((len(self.list_round)) - 1) :
            self.list_round[round] = False
        print(self.list_round)
        self.player_validated = False
        for bloc in self.list_bloc:
            bloc.image = pygame.image.load('asset/button/block.png')

    def champ_select(self, screen):
            self.background = pygame.image.load('asset/bg/Fichier 1.png')
            self.background = pygame.transform.scale(self.background, (1080, 720))










