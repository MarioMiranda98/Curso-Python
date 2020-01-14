from classes.Person import Person
from classes.Magic import Magic
from classes.Item import Item
from classes.Game import Game 

print("\n\n")
print("NAME               HP                                     MP")

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
player = Person("Mario", 3260, 200, 60, 34, playerSpells, playerItems)
player2 = Person("Mario", 4160, 200, 60, 34, playerSpells, playerItems)
player3 = Person("Robot", 3889, 200, 60, 34, [], playerItems)

enemy = Person("Evil Mario", 18200, 701, 525, 25, [], [])
enemy2 = Person("MXMXM", 1250, 130, 560, 325, [], [])
enemy3 = Person("Imp", 1250, 130, 560, 325, [], [])

players = [player, player2, player3]
enemies = [enemy, enemy2, enemy3]

game = Game(players, enemies)
game.announcement()
game.play()