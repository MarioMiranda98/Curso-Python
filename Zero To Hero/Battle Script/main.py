from classes.Bcolors import Bcolors
from classes.Person import Person
from classes.Magic import Magic

#Create Black Magic
fire = Magic("Fire", 10, 100, "Black")
thunder = Magic("Thunder", 12, 124, "Black")
blizzard = Magic("Blizzard", 10, 100, "Black")
meteor = Magic("Meteor", 20, 200, "Black")
quake = Magic("Quake", 14, 140, "Black")

#Create White Magic
cure = Magic("Cure", 12, 120, "White")
cura = Magic("Cura", 18, 200, "White")

#Instantiate People
player = Person(460, 200, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)

while running:
    print("====================")
    player.chooseAction()
    choice = input("Chose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generateDamage()
        enemy.takeDamage(dmg)
        
        print("You attack for " + str(dmg) + " points of damage. Enemy Hp: " + str(enemy.getHp()))
    elif index == 1:
        player.chooseMagic()
        magicChoice = input("Choose Magic: ")
        indexMagic = int(magicChoice) - 1
        
        magicDamage = player.magic[indexMagic].generateDamage()
        spell = player.magic[indexMagic].name
        cost = player.magic[indexMagic].cost

        currentMp = player.getMp()
        
        if(cost > currentMp):
            print(Bcolors.FAIL + "\nNot Enough Mp" + Bcolors.ENDC)
            continue

        if player.magic[indexMagic].type == "White":
            player.heal(magicDamage)
            print(Bcolors.OKBLUE + "\n" + str(player.magic[indexMagic].name) + " heals for " + str(magicDamage) + Bcolors.ENDC)
        elif player.magic[indexMagic].type == "Black":
            enemy.takeDamage(magicDamage)
            print(Bcolors.OKBLUE + "\n" + spell + " deals " + str(magicDamage) + " points of Damage " + Bcolors.ENDC)

        player.reduceMp(cost)
        print("Enemy Hp: " + str(enemy.getHp()))



    enemyChoice = 1
    enemyDmg = enemy.generateDamage()
    player.takeDamage(enemyDmg)
    print("Enemy attacks for " + str(enemyDmg))

    print("______________________________")
    print("Enemy Hp: " + Bcolors.FAIL + str(enemy.getHp()) + "/" + str(enemy.getMaxHp()) + Bcolors.ENDC)
    print("")

    print("Your Hp: " + Bcolors.OKGREEN + str(player.getHp()) + "/" + str(player.getMaxHp()) + Bcolors.ENDC)
    print("Your Mp: " + Bcolors.OKBLUE + str(player.getMp()) + "/" + str(player.getMaxMp()) + Bcolors.ENDC)
    print("")

    if enemy.getHp() == 0:
        print(Bcolors.OKGREEN + "You Win" + Bcolors.ENDC)
        running = False
    elif player.getHp() == 0:
        print(Bcolors.FAIL + "Your enemy has defeat you!!" + Bcolors.ENDC)
        running = False