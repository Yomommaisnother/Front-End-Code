import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        pygame.init()
        
        self.screen=ai_game.screen
        self.image= pygame.image.load("images/evilski.bmp")
    
        self.image=pygame.transform.scale(self.image,(100,101))
        self.rect= self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.settings=ai_game.settings
        self.x =float(self.rect.x)
        self.y =float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed*self.settings.fleet_direction)
        self.rect.x=self.x
        

    
    
        
 
