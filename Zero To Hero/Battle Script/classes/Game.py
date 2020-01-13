from .Bcolors import Bcolors
class Game():
    def __init__(self, players, enemy):
        self.players = players
        self.enemy = enemy
        self.running = True

    def play(self):
        while self.running:
            print("====================")
            for player in self.players:
                print("NAME                   HP                                    MP")
                player.getStats()

            print("NAME                   HP                                    MP")
            self.enemy.getEnemyStats()

            for player in self.players:
                player.chooseAction()
                choice = input("Chose action: ")
                index = int(choice) - 1

                if index == 0:
                    dmg = player.generateDamage()
                    self.enemy.takeDamage(dmg)

                    print("You attack for " + str(dmg) +
                        " points of damage. Enemy Hp: " + str(self.enemy.getHp()))
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
                        self.enemy.takeDamage(magicDamage)
                        print(Bcolors.OKBLUE + "\n" + spell + " deals " +
                            str(magicDamage) + " points of Damage " + Bcolors.ENDC)

                        player.reduceMp(cost)
                    print("Enemy Hp: " + str(self.enemy.getHp()))

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
                        self.enemy.takeDamage(item["item"].prop)
                        print(Bcolors.OKBLUE + "\n" + str(item["item"].name) + " deals " + str(
                            item["item"].prop) + " points of Damage " + Bcolors.ENDC)

                    item["quantity"] -= 1

            #enemyChoice = 1
            enemyDmg = self.enemy.generateDamage()
            player.takeDamage(enemyDmg)
            print("Enemy attacks for " + str(enemyDmg))

            print("______________________________")
            print("Enemy Hp: " + Bcolors.FAIL + str(self.enemy.getHp()) +
                "/" + str(self.enemy.getMaxHp()) + Bcolors.ENDC)
            print("")

            print("Your Hp: " + Bcolors.OKGREEN + str(player.getHp()) +
                "/" + str(player.getMaxHp()) + Bcolors.ENDC)
            print("Your Mp: " + Bcolors.OKBLUE + str(player.getMp()) +
                "/" + str(player.getMaxMp()) + Bcolors.ENDC)
            print("")

            if self.enemy.getHp() == 0:
                print(Bcolors.OKGREEN + "You Win" + Bcolors.ENDC)
                self.running = False
            elif player.getHp() == 0:
                print(Bcolors.FAIL + "Your enemy has defeat you!!" + Bcolors.ENDC)
                self.running = False

    def announcement(self):
        print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)
