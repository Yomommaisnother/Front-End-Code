import pygame
import sys
from rocket import Rocket
class Blue_Sky:
    def __init__(self):
       
        pygame.init()
        pygame.display.set_caption("Blue Sky")
        self.bg_color=(0,0,255)
        self.screen=pygame.display.set_mode((1200,800))
       
        self.rocket_speed=1
        
        self.rocket= Rocket(self)
        self.x=self.rocket.rect.x
        self.y=self.rocket.rect.y
        
        
      
       
    def run_game(self):
        clock = pygame.time.Clock()
        while True:
            self.screen.fill(self.bg_color)
            
            self._check_events()
            self._update_rocket()
            self._update_screen()
            clock.tick(60)

            
            
             
        
    def _check_events(self):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
            self.keys= pygame.key.get_pressed()
            if self.keys[pygame.K_w] and self.rocket.rect.top > 0:
                self.y -= 1
            if self.keys[pygame.K_s] and self.rocket.rect.bottom < self.rocket.screen_rect.bottom:
                self.y += 1
            if self.keys[pygame.K_d] and self.rocket.rect.right < self.rocket.screen_rect.right:
                self.x += 1
            if self.keys[pygame.K_a] and self.rocket.rect.left > 0:
                self.x -= 1

    def _update_rocket(self):
        self.rocket.rect.x = int(self.x)
        self.rocket.rect.y = int(self.y)
    
    def _update_screen(self):
        self.rocket.blitme()
        pygame.display.flip()


            
            
            

           
            
if __name__ == '__main__':
    bs=Blue_Sky()
    bs.run_game()



