import random
from RPG_code import Uweapons

class PlayerClass:
    name = ""
    life = 0
    potions = 0
    weapon = 0

    def __init__(self, name, life, potions, weapon):
        self.name = name
        self.life = life
        self.potions = potions
        self.weapon = weapon

    def damage(self):
        pass
    
    def potion(self):
        pass
    
    def SelectWeapon(self):
        choice = input("")
        self.weapon = Uweapons(choice)