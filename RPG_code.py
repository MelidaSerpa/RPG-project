import math
import random
from CharacterClass import CharacterClass
from ANSI import ANSI

kermit = CharacterClass("Kermit The Warrior", 150, 1)
elephant = CharacterClass("Blading Elephant", 500, 1)


def Info():
    print("Blading Elephant stats: \n" + "Hp: " + str(elephant.life) + "\n")
    print("Kermit stats: \n" + "Hp: " + str(kermit.life) + "\n" + "Actions Count :" + str(kermit.numOfAtt))
    return("")

def UserAtt(SelAtt, DmgNun):
    if SelAtt == "A":
        SelAtt = "Ak 47"
        DmgNun = 30
    if SelAtt == "B":
         SelAtt = "Slap"
         DmgNun = 22
    if SelAtt == "C":
        SelAtt = "Rubber Hen"
        DmgNun = 45
    return("You attacked with: " + SelAtt + " Dmg: " + str(DmgNun))

def bossAttFase1():
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

#Title color
ANSI = ANSI.background(0) + ANSI.color_text(49) + ANSI.style_text(31) + "Kermit The Warrior in Northland"

#Kermit dialogue when receiving and giving attack
kDG = ["Come on with the come on!", "Let's go!,", "Mf tough", ":o", "Messi 🤢", "stay focused, stay committed 🧐👹", "Entomuymal 🤮", "Mf is getting horny 🤢"]
kDGS = random.choice(kDG)
kDR = ["Agh!", "Auchi", ">:/", "ah! 😳", "Ughh 🐡", "Damm hommie, calm the fuck down >:/"]
kDRS = random.choice(kDR)

EDR = ["uh! :excited:", "Ricooo", "More papi", "stronger!!"]
EDRS = random.choice(EDR)

#Potions given to kermit when "turn4" times
turn4 = 3
i = 0

print(title)
print("")
input("Press Enter to Start \n")
print("Guten Tag Kermit!, \n Another day in northland, another coin. Since last night you spent all your money in beer and h*es,")
print("there's no money to survive the week, so get up warrior!, it's time to work.\n")
input("Press Enter to continue \n")
print("There are a some posters on the town board with missions,")
print("maybe you can take a look on them and see what's good.\n")
input("Press Enter to see posters \n")
print("Mutant elephant - wanted - reward: 50 gold coins \n")
print("Kermit: \"Uhhhh this loot be juicy 😏\"\n")
input("Press Enter to start mission \n")
print("")
print("Kermit1: \"Let's go hommie, we got a mf Elephant to kill\"\n")
print("...")
print("...")
print("...\n")
input("Press Enter to continue \n")
print("Kermit: Alright, here's the mf \n")
print("Elephant *serious stare*")
print("...")
print("Kermit: It looks like we got him taking a dump.... such a shameful way to start a battle 😟\n")

print("Kermit : \"Let's initiate with an attack\" \n")
print(Info())


while elephant.life >= 0 or kermit.life >= 0:
    SelAtt = ""
    DmgNun = 0
    print("\"Ak 47\"- Dmg 30 → A")
    print("\"Slap\"- Dmg 22 → B ")
    print("\"Rubber Hen\" - Dmg 45 → C\n")
    SelAtt = input("Type the related letter to the attack (A, B or C): ")
    SelAtt = SelAtt.upper()
    print("\n")
    print("Blading Elephant: " + EDRS + "\n")
    print(UserAtt(SelAtt, DmgNun) + "\n")
    elephant.life - DmgNun
    print(Info())
    print("Blading Elephant turn: \n")
    print(bossAttFase1())



#Boss atributtes

#boss_life = 250

#failed_attack = "Failed attack"
#failed_attack =  random.radint(0,100)

#Kermit atributtes
#kermit_attacks = ["Ak 47","Slap","Machine gun"]
#Kermit_life = 150
#especial_attack = random.randint(0,100)

#3 life potions
#life_potion = 25

#especial_attack = "Sexy smirk"
#especial_attack = random.radint(0,100)




































