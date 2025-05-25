class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initizalize the game's settings"""
        #Screen settings 
        self.screen_width=1080
        self.screen_height=900
        self.bg_color=(230,230,230)
        #ship's setting
       
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed=3
       
        
        self.fleet_drop_speed=100
        self.ship_limit=3
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        

    def initialize_dynamic_settings(self):
         self.ship_speed = 1.0
         self.bullet_speed = 1.0
         self.alien_speed=0.5
         self.fleet_direction=1
         self.alien_points = 50
    def increase_speed(self):
         self.ship_speed *= self.speedup_scale
         self.bullet_speed *= self.speedup_scale
         self.alien_speed *= self.speedup_scale
         new_score=int(self.alien_points * self.score_scale)
         self.alien_points= new_score
         print(self.alien_points)


