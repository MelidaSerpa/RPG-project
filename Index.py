from random import randint
import sys
from ANSI import ANSI
import random

hero = {'name' : 'Kermit The Warrior',
        'lvl' : 1,
        'xp' : 0,
        'lvlNext' : 25,
        'stats' : {'hp' : 150,
                   'attacks' : [30, 45]
                          }
}

boss = {'name' : 'Blading Elephant',
        'lvl' : 1,
        'xp' : 0,
        'lvlNext' : 25,
        'stats' : {'hp' : 250,
                   'attacks' : [15, 22]
                          }
}

#Title
Title = ANSI.background(0) + ANSI.color_text(49) + ANSI.style_text(31) + "Kermit The Warrior in Northland"

#Kermit dialogue when receiving and giving attack
kDG = ["Come on with the come on!", "Let's go!,", "Mf tough", ":o", "Messi 🤢", "stay focused, stay committed 🧐👹", "Entomuymal 🤮", "Mf is getting horny 🤢"]
kDGS = random.choice(kDG)
kDR = ["Agh!", "Auchi", ">:/", "ah! 😳", "Ughh 🐡", "Damm hommie, calm the fuck down >:/"]
kDRS = random.choice(kDR)

EDR = ["uh! :excited:", "Ricooo", "More papi", "stronger!!"]
EDRS = random.choice(EDR)

def takeDmg(attacker, defender):
    dmg = randint(attacker['stats']['attacks'][0], attacker['stats']['attacks'][1])
    defender['stats']['hp'] = defender['stats']['hp'] - dmg
    
    if defender['stats']['hp'] <= 0:
        print('{} has been slain'.format(defender['name']))
        input('Press any key to quit.')
        sys.exit(0)
    else:
        print('{} takes {} damage!'.format(defender['name'], dmg))
        
def commands(player, enemy):
    while True:
        print('------------------------')
        cmd = input('Do you want to attack? Yes/No: ').lower()
        if 'yes' in cmd:
            print(player['name'], ': ', kDGS, '\n')
            print(enemy['name'],': ', EDRS, '\n')
            takeDmg(player, enemy)
        elif 'no' in cmd:
            print('{} takes opportunity to attack!'.format(enemy['name']))
            print(player['name'], ': ', kDRS, '\n')
            takeDmg(enemy, player)
        else:
            pass
        
print(Title)
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
print()


commands(hero, boss)