import random


class CharacterClass:
    name = ""
    life = 0
    numOfAtt = 0

    def __init__(self, name, life, numOfatt):
        self.name = name
        self.life = life
        self.numOfAtt = numOfatt

    def bossAtt(self):
        boss_attacks = ["Body Blast","Acid Blow","Laser Hands","Sin Purifier"]
        SelAtt = random.choice(boss_attacks)
        DmgNun = 0
        failed_attack = "Failed attack"
        failed_attack =  random.randint(0,100)
        
        if failed_attack <= 15:
            SelAtt = "Failed Attack"
            DmgNun = 5
        if SelAtt == "Body Blast":
            DmgNun = 25
        if SelAtt == "Acid Blow":
            DmgNun = 20
        if SelAtt == "Laser Hands":
            DmgNun = 25
        if SelAtt == "Sin Purifier":
            DmgNun = 24



        return("Blading Elephant attacked with: " + SelAtt + " Dmg: " + DmgNun)