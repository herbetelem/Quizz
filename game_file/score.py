# coding : utf-8

# * import des libs
import pygame
from game_file.sql_function import SQL_request

# créer la classe game
class Score:
    
    def __init__(self):
        # * definir si le jeu a commencer ou pas
        self.score_look = False
        # * definir le background
        self.background = pygame.image.load('asset/bg/bg_score.jpg')
        self.background = pygame.transform.scale(self.background, (1080, 720))
        # * definir le logo
        self.logo = pygame.image.load('asset/button/LoL.png')
        # * definir l'objet sql
        self.sql_request = SQL_request()
        # * je créer mes 10 blocs d'image
        self.block_1 = pygame.image.load('asset/button/block.png')
        self.block_1 = pygame.transform.scale(self.block_1, (500, 50))
        self.block_2 = pygame.image.load('asset/button/block.png')
        self.block_2 = pygame.transform.scale(self.block_2, (500, 50))
        self.block_3 = pygame.image.load('asset/button/block.png')
        self.block_3 = pygame.transform.scale(self.block_3, (500, 50))
        self.block_4 = pygame.image.load('asset/button/block.png')
        self.block_4 = pygame.transform.scale(self.block_4, (500, 50))
        self.block_5 = pygame.image.load('asset/button/block.png')
        self.block_5 = pygame.transform.scale(self.block_5, (500, 50))
        self.block_6 = pygame.image.load('asset/button/block.png')
        self.block_6 = pygame.transform.scale(self.block_6, (500, 50))
        self.block_7 = pygame.image.load('asset/button/block.png')
        self.block_7 = pygame.transform.scale(self.block_7, (500, 50))
        self.block_8 = pygame.image.load('asset/button/block.png')
        self.block_8 = pygame.transform.scale(self.block_8, (500, 50))
        self.block_9 = pygame.image.load('asset/button/block.png')
        self.block_9 = pygame.transform.scale(self.block_9, (500, 50))
        self.block_10 = pygame.image.load('asset/button/block.png')
        self.block_10 = pygame.transform.scale(self.block_10, (500, 50))
        self.list_block = [self.block_1, self.block_2, self.block_3, self.block_4, self.block_5,
                        self.block_6, self.block_7, self.block_8, self.block_9, self.block_10]
        
    def update(self, screen):
        # * je fait les update de mes different items
        screen.blit(self.background, (0,0))
        screen.blit(self.logo, (30,30))
        self.sql_request.read_score()
        font = pygame.font.Font(None, 36)
        nb_vainqueur = len(self.sql_request.score_tmp)
        y_temp = 25
        for i in range(nb_vainqueur):
            phrase = f"{self.sql_request.score_tmp[i][1]} a obtenu le score de {self.sql_request.score_tmp[i][2]}/5"
            text = font.render(phrase, 1, (255,255,255))
            screen.blit(self.list_block[i],(450, y_temp - 15))
            screen.blit(text,(500, y_temp))
            y_temp += 70