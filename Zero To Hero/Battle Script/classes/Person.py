import random
from .Bcolors import Bcolors

class Person():
    def __init__(self, hp, mp, atk, df, magic):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkLow = atk - 10
        self.atkHigh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

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

        print(Bcolors.OKBLUE + Bcolors.BOLD + "Actions" + Bcolors.ENDC)
        for item in self.actions:
            print(str(i) + ": " + str(item))
            i += 1

    def chooseMagic(self):
        i = 1

        print("Magic")
        for spell in self.magic:
            print(str(i) + ": " + str(spell.name) + " cost: " + str(spell.cost))
            i += 1