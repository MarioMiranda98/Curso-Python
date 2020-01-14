from .Bcolors import Bcolors
import random 

class Game():
    def __init__(self, players, enemies):
        self.players = players
        self.enemies = enemies
        self.running = True

    def play(self):
        indexAttack = 0
        while self.running:
            print("====================")
            for player in self.players:
                print("NAME                   HP                                    MP")
                player.getStats()

            for enemy in self.enemies:
                print("NAME                   HP                                    MP")
                enemy.getEnemyStats()

            for player in self.players:
                player.chooseAction()
                choice = input("Chose action: ")
                index = int(choice) - 1

                if index == 0:
                    showEnemies(self.enemies)
                    attack = input("Chose enemy: ")
                    indexAttack = int(attack) - 1
                    dmg = player.generateDamage()
                    self.enemies[indexAttack].takeDamage(dmg)

                    print("You attack for " + str(dmg) +
                        " points of damage. enemies Hp: " + str(self.enemies[indexAttack].getHp()))
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
                        print(Bcolors.OKBLUE + "\n" +
                            str(player.magic[indexMagic].name) + " heals for " + str(magicDamage) + Bcolors.ENDC)
                    elif player.magic[indexMagic].type == "Black":
                        showEnemies(self.enemies)
                        attack = input("Chose enemy: ")
                        indexAttack = int(attack) - 1
                        self.enemies[indexAttack].takeDamage(magicDamage)
                        print(Bcolors.OKBLUE + "\n" + spell + " deals " +
                            str(magicDamage) + " points of Damage " + Bcolors.ENDC)

                        player.reduceMp(cost)
                    print("enemies Hp: " + str(self.enemies[indexAttack].getHp()))

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
                        player.heal(item["item"].prop)
                        print(Bcolors.OKGREEN + "\n" + item["item"].name + " heals for " + str(
                            item["item"].prop) + " hp" + Bcolors.ENDC)
                    elif item["item"].type == "elixer":
                        player.hp = player.maxHp
                        player.mp = player.maxMp
                        print(Bcolors.OKGREEN + "\nFully restores hp/mp" + Bcolors.ENDC)
                    elif item["item"].type == "attack":
                        showEnemies(self.enemies)
                        attack = input("Chose enemy: ")
                        indexAttack = int(attack) - 1
                        self.enemies[indexAttack].takeDamage(item["item"].prop)
                        print(Bcolors.OKBLUE + "\n" + str(item["item"].name) + " deals " + str(
                            item["item"].prop) + " points of Damage " + Bcolors.ENDC)

                    item["quantity"] -= 1

                for enemy in self.enemies:
                    enemiesDmg = enemy.generateDamage()
                    
                    if(len(self.players) > 1):
                        who = random.randrange(0, len(self.players) - 1)
                    else:
                        who = 0

                    self.players[who].takeDamage(enemiesDmg)
                    print("enemy " + enemy.name + " attacks for " + str(enemiesDmg) 
                        + " to " + str(self.players[who].name))

            deleteCharacter(self.players)
            deleteCharacter(self.enemies)
            self.running = isGameOnPlay(self.players, self.enemies)

    def announcement(self):
        print(Bcolors.FAIL + Bcolors.BOLD + "AN enemies ATTACKS!" + Bcolors.ENDC)

    
def isGameOnPlay(players, enemies):
    if len(players) <= 0:
        print(Bcolors.FAIL + "The enemy has defeat you" + Bcolors.ENDC) 
        return False 
    elif len(enemies) <= 0:
        print(Bcolors.OKGREEN + "You Win" + Bcolors.ENDC)
        return False
    else:
        return True

def deleteCharacter(list):
    cont = 0
    if len(list) <= 0:
        return 

    for i in list:
        if i.getHp() <= 0:
            print(i.name)
            list.pop(cont)
            cont += 1

def showEnemies(enemies):
    pos = 1
    for i in enemies:
        print(str(pos) + ".- " + str(i.name))
        pos += 1