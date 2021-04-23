from Item.item import Item
from enum import Enum

# The weapon damage types
class DamageType (Enum):
    MELEE = 1
    MAGIC = 2

'''
Parent class of weapon
'''
class Weapon (Item):
    def __init__(self, args, level=1, name="weapon"):
        Item.__init__(self, args, name)
        
        self.level = level
        self.name = name
        self.damage = args['damage'] # Damage of weapon