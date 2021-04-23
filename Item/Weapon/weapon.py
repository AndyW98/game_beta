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
    def __init__(self, weight=1, damage=1, level=1, name="Weapon", health=20):
        Item.__init__(self, weight, name)
        
        self.level = level    # Level of the weapon
        self.name = name      # Name of the weapon
        self.damage = damage  # Base damage dealt by weapon
        self.m_health = health # Health/durability of weapon
        self.current_health = health

    def __str__(self):
        weapon_str = "--------------------\n" + \
                     "Weapon - \n" + \
                     "  Name:   " + self.name + "\n" + \
                     "  Level:  " + str(self.level)  + "\n" + \
                     "  Damage: " + str(self.damage) + "\n" + \
                     "  Weight: " + str(self.weight) + "\n" + \
                     "  Durability: [" + str(self.current_health) + \
                         " / " + str(self.m_health) + \
                         "]\n"
        return weapon_str

    # Getters

    def get_damage(self):
        if self.current_health > 0:
            return self.damage
        else:
            return 1

    def get_name(self):
        return self.name

    # Setter

    def take_damage(self, damage):
        self.current_health -= damage

