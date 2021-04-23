from Item.item import Item
from enum import Enum

# The weapon damage types
class DamageType (Enum):
    MELEE = 1
    MAGIC = 2

class Weapon (Item):

    """Weapons in the game"""

    def __init__(self, weight=1, power=1, level=1, name="Weapon", health=20):
        Item.__init__(self, weight, name)
        
        self.level = level     # Level of the weapon
        self.name = name       # Name of the weapon
        self.power = power     # Base power dealt by weapon
        self.m_health = health # Health/durability of weapon
        self.health = health   # Current health of weapon

    def __str__(self):
        weapon_str = "--------------------\n" + \
                     "Weapon - \n" + \
                     "  Name:   " + self.name + "\n" + \
                     "  Level:  " + str(self.level)  + "\n" + \
                     "  Power:  " + str(self.power) + "\n" + \
                     "  Weight: " + str(self.weight) + "\n" + \
                     "  Durability:  [" + str(self.health) + \
                         " / " + str(self.m_health) + \
                         "]\n"
        return weapon_str

    # Getters

    def get_power(self):
        if self.health > 0:
            return self.power
        else:
            return 1

    def get_name(self):
        return self.name

    # Setter

    # Printer

    def print_weapon_stats(self):
        print(self)

    # Methods

    def take_damage(self, power):
        self.current_health -= power

    def special_attack(self):
        self.health -= 1
        print("Weapon hurt itself in confusion!\n")

