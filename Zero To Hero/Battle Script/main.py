from classes.Bcolors import Bcolors
from classes.Person import Person
from classes.Magic import Magic
from classes.Item import Item

print("\n\n")
print("NAME               HP                                     MP")

print("                    _________________________             __________")
print(Bcolors.BOLD + "Valos:      "
    + Bcolors.OKGREEN + "460/460|█████████████████████████|" + Bcolors.ENDC + "    "+ Bcolors.OKBLUE + "200/200|██████████|" + Bcolors.ENDC)

print("                    _________________________             __________")
print("Valos:    1200/1200|█████████████████████████|      65/65|██████████|")

#Create Black Magic
fire = Magic("Fire", 10, 100, "Black")
thunder = Magic("Thunder", 12, 124, "Black")
blizzard = Magic("Blizzard", 10, 100, "Black")
meteor = Magic("Meteor", 20, 200, "Black")
quake = Magic("Quake", 14, 140, "Black")

#Create White Magic
cure = Magic("Cure", 12, 120, "White")
cura = Magic("Cura", 18, 200, "White")

#Create Item
potion = Item("Potion", "potion", "Heals 50 hp", 50)
hiPotion = Item("Hi - Potion", "potion", "Heals 100 hp", 100)
superPotion = Item("Super Potion", "potion", "Heals 500 hp", 500)
elixer = Item("Elixer", "elixer", "Fully restores hp/mp of one party member", 9999)
hiElixier = Item("Hi - Elixer", "elixer", "Fully restores party's hp/mp", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

playerSpells = [fire, thunder, blizzard, meteor, cure, cura]
playerItems = [{"item" : potion, "quantity" : 5}, {"item" : hiPotion, "quantity" : 5}, 
               {"item" : superPotion, "quantity" : 5}, {"item" : elixer, "quantity" : 5}, 
               {"item" : hiElixier, "quantity" : 2}, {"item" : grenade, "quantity" : 5}]

#Instantiate People
player = Person(460, 200, 60, 34, playerSpells, playerItems)
enemy = Person(1200, 65, 45, 25, [], [])

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

        if indexMagic == -1:
            continue
        
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
    elif index == 2:
        player.chooseItem()
        itemChoice = input("Choose Item: ")
        indexItem = int(itemChoice) - 1

        if indexItem == -1:
            continue
            
        item = player.items[indexItem]

        if item["quantity"] <= 0:
            print(Bcolors.FAIL + "\n" + "None Left..." + Bcolors.ENDC)
            continue

        if item["item"].type == "potion":
            player.heal(item.prop)
            print(Bcolors.OKGREEN + "\n" + item["item"].name + " heals for " + str(item["item"].prop) + " hp" + Bcolors.ENDC)
        elif item["item"].type == "elixer":
            player.hp = player.maxHp
            player.mp = player.maxMp
            print(Bcolors.OKGREEN + "\nFully restores hp/mp" + Bcolors.ENDC)
        elif item["item"].type == "attack":
            enemy.takeDamage(item["item"].prop)
            print(Bcolors.OKBLUE + "\n" + str(item["item"].name) + " deals " + str(item["item"].prop) + " points of Damage " + Bcolors.ENDC)
         
        item["quantity"] -= 1


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