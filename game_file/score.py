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
        
    def update(self, screen):
        screen.blit(self.background, (0,0))
        screen.blit(self.logo, (30,30))
        self.sql_request.read_score()
        font = pygame.font.Font(None, 36)
        nb_vainqueur = len(self.sql_request.score_tmp)
        y_temp = 60
        for i in range(nb_vainqueur):
            phrase = f"{self.sql_request.score_tmp[i][1]} a obtenu le score de {self.sql_request.score_tmp[i][2]}/5"
            text = font.render(phrase, 1, (0,0,0))
            screen.blit(text,(500, y_temp))
            y_temp += 60