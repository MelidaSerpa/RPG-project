import random
from PlayerClass import PlayerClass

class aiplayerclass(PlayerClass):
    name = ""
    life = 0
    shield = 0

    def __init__(self, name, life, shield):
        self.name = name
        self.life = life
        self.shield = shield
        
    def damage(self):
        pass
    
    def shield(self):
        pass