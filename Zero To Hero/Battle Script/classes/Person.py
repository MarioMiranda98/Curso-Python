import random
from .Bcolors import Bcolors

class Person():
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkLow = atk - 10
        self.atkHigh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generateDamage(self):
        return random.randrange(self.atkLow, self.atkHigh)

    def takeDamage(self, dmg):
        self.hp -= dmg

        if self.hp < 0:
            self.hp = 0
        
        return self.hp

    def heal(self, dmg):
        self.hp += dmg

        if self.hp >= self.maxHp:
            self.hp = self.maxHp

    def getHp(self):
        return self.hp

    def getMaxHp(self):
        return self.maxHp
    
    def getMp(self):
        return self.mp

    def getMaxMp(self):
        return self.maxMp

    def reduceMp(self, cost):
        self.mp -= cost
    
    def chooseAction(self):
        i = 1

        print("\n" + Bcolors.BOLD + self.name + Bcolors.ENDC)
        print(Bcolors.OKBLUE + Bcolors.BOLD + "Actions" + Bcolors.ENDC)
        for item in self.actions:
            print("   " + str(i) + ": " + str(item))
            i += 1

    def chooseMagic(self):
        i = 1

        print(Bcolors.OKBLUE + Bcolors.BOLD + "Magic" + Bcolors.ENDC)
        for spell in self.magic:
            print("   " + str(i) + ": " + str(spell.name) + " cost: " + str(spell.cost))
            i += 1

    def chooseItem(self):
        i = 1

        print(Bcolors.OKBLUE + Bcolors.BOLD + "Items" + Bcolors.ENDC)
        for item in self.items:
            print("   " + str(i) + ":" + str(item["item"].name) + ", desc: " + str(item["item"].description) + " {x" + str(item["quantity"]) + "}")
            i += 1
        
    def getStats(self):
        hpBar = ""
        hpBarTicks = (self.hp / self.maxHp) * 100 / 4

        mpBar = ""
        mpBarTicks = (self.mp / self.maxMp) * 100 / 10

        while hpBarTicks > 0:
            hpBar += "█"
            hpBarTicks -= 1

        while len(hpBar) < 25:
            hpBar += " "

        while mpBarTicks > 0:
            mpBar += "█"
            mpBarTicks -= 1

        while len(mpBar) < 10:
            mpBar += " "

        print(Bcolors.BOLD + str(self.name) + ":       "
        + Bcolors.OKGREEN + str(self.hp) + "/" + str(self.maxHp) +" "+ str(hpBar) + Bcolors.ENDC + "    "+ Bcolors.OKBLUE + str(self.mp) + "/" + str(self.maxMp) +" |" + mpBar +"|" + Bcolors.ENDC)

    def getEnemyStats(self):
        hpBar = ""
        hpBarTicks = (self.hp / self.maxHp) * 100 / 2

        mpBar = ""
        mpBarTicks = (self.mp / self.maxMp) * 100 / 4  

        while hpBarTicks > 0:
            hpBar += "█"
            hpBarTicks -= 1

        while len(hpBar) < 50:
            hpBar += " "

        while mpBarTicks > 0:
            mpBar += "█"
            mpBarTicks -= 1

        while len(mpBar) < 10:
            mpBar += " "

        print(Bcolors.BOLD + str(self.name) + ":       "
        + Bcolors.OKGREEN + str(self.hp) + "/" + str(self.maxHp) +" "+ str(hpBar) + Bcolors.ENDC + "    "+ Bcolors.OKBLUE + str(self.mp) + "/" + str(self.maxMp) +" |" + mpBar +"|" + Bcolors.ENDC)