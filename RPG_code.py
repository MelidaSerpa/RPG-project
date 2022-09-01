import math
import random
from CharacterClass import CharacterClass

kermit = CharacterClass("Kermit The Warrior", 150, 1)
elephant = CharacterClass("Blading Elephant", 500, 1)


def Info():
    print("Blading Elephant stats: \n" + "Hp: " + str(elephant.life) + "\n")
    print("Kermit stats: \n" + "Hp: " + str(kermit.life) + "\n" + "Actions Count :" + str(kermit.numOfAtt))
    return("")

#Kermit dialogue when receiving and giving attack
kDG = ["Come on with the come on!", "Let's go!,", "Mf tough", ":o", "Messi 🤢", "stay focused, stay committed 🧐👹", "Entomuymal 🤮"]
kDGS = random.choice(kDG)
kDR = ["Agh!", "Auchi", ">:/", "ah! 😳", "Ughh 🐡", "Damm hommie, calm the fuck down >:/", "Ha!, jokes on you I'm into that shit!"]
kDRS = random.choice(kDR)

#Potions given to kermit when "turn4" times
turn4 = 3
i = 0

print("NORTHLAND \n")
print("")
input("Press Enter to Start \n")
print("Guten Tag Kermit!, \n Another day in northland, another coin. Since last night you spent all your money in beer and h*es,")
print("there's no money to survive the week, so get up warrior!, it's time to work.\n")
input("Press Enter to continue \n")
print("There are a some posters on the town board with missions,")
print("maybe you can take a look on them and see what's good.\n")
input("Press Enter to see posters \n")
print("Mutant elephant - wanted - reward: 50 gold coins \n")
print("Kermit: \"Uhhhh this loot be juicy 7u7\"\n")
input("Press Enter to start mission \n")
print("")
print("Kermit1: \"Let's go hommie, we got a mf Elephant to kill\" \n")
print("...")
print("...")
print("...")
input("Press Enter to continue \n")
print("Kermit: Alright, here's the mf \n")
print("Elephant *serious stare*\n")
print("...")
print("Kermit: It looks like we got him taking a dump.... such a shameful way to start a battle :Worried-face:")

print("Kermit : \"Let's initiate with an attack\"")



while elephant.life <= 0 or kermit.life <= 0:
    SelAtt = ""
    print("\"Ak 47\"- Dmg 30 → A\n")
    print("\"Slap\"- Dmg 22 → B \n")
    print("\"Rubber Hen\" - Dmg 45 → C\n")
    SelAtt = input("Type the related letter to the attack (A, B or C): \n")
    SelAtt = SelAtt.upper()
    print(UserAtt() + "\n")


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




































