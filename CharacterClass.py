import random


class CharacterClass:
    name = ""
    life = 0
    numOfAtt = 0

    def __init__(self, name, life, numOfatt):
        self.name = name
        self.life = life
        self.numOfAtt = numOfatt

    def bossAttFase1(self):
        boss_attacks = ["Body Blast","Acid Blow","Laser Hands","Sin Purifier"]
        SelAtt = random.choice(boss_attacks)
        DmgNun = 0
        failed_attack =  random.randint(0,100)
        
        if failed_attack >= 95:
            SelAtt = "Failed Attack"
            DmgNun = 0
        if SelAtt == "Body Blast":
            DmgNun = 25
        if SelAtt == "Acid Blow":
            DmgNun = 20
        if SelAtt == "Laser Hands":
            DmgNun = 15
        if SelAtt == "Sin Purifier":
            DmgNun = 12
        return("Blading Elephant attacked with: " + SelAtt + " Dmg: " + str(DmgNun))

    def bossAttFase2(self):
        boss_attacks = ["Body Blast","Acid Blow","Laser Hands","Sin Purifier"]
        SelAtt = random.choice(boss_attacks)
        DmgNun = 0
        failed_attack = "Failed attack"
        failed_attack =  random.randint(0,100)
        
        if failed_attack <= 15:
            SelAtt = "Failed Attack"
            DmgNun = 5
        if SelAtt == "Body Blast":
            DmgNun = 40
        if SelAtt == "Acid Blow":
            DmgNun = 30
        if SelAtt == "Laser Hands":
            DmgNun = 25
        if SelAtt == "Sin Purifier":
            DmgNun = 24
        return("Blading Elephant attacked with: " + SelAtt + " Dmg: " + str(DmgNun))
