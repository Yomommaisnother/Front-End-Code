import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_game):
        """Initialize the ship and set its starting point."""
        super().__init__()
        self.screen=ai_game.screen
        self.settings= ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        #load the ship image and get its rect 
        self.image = pygame.image.load('images/ski.bmp')
        #start each new ship at the bottom center of the screen
        
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        self.x = float(self.rect.x)

        #Movement Flag
        self.moving_right=False
        self.moving_left=False
    
    def update(self):
        """Update the ship's posityion based on the movement's flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x=self.x


    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)





 