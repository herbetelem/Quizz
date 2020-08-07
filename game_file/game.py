# coding : utf-8

# * import des libs
import pygame

# créer la classe game
class Game:
    
    def __init__(self):
        # * definir si le jeu a commencer ou pas
        self.is_playing = False
        # * 
        self.background = pygame.image.load('asset/bg/bg_5.jpg')
        self.background = pygame.transform.scale(self.background, (1080, 720))