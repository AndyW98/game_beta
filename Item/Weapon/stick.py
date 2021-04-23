from Item.Weapon.weapon import Weapon, DamageType
from Item.item import Item


class Stick (Weapon):

    # Constructor
    def __init__(self, weight=1, damage=1, level=1, name="stick", health=10):
        Weapon.__init__(self, weight, damage, level, name, health)

        self.level = level
        self.name = name
        self.attack_type = DamageType.MELEE

    def __str__(self):
        stick_str = Weapon.__str__(self) + "\n" + \
                    "Weapon Type: Stick"
        return stick_str

    # Getter

    # Printer

    def print_weapon_stats(self):
        print("--------------------\n" + \
              "Weapon:\n" + \
              " " + self.name + "\n" + \
              "--------------------\n" + \
              "Level:  " + str(self.level)  + "\n" + \
              "Damage: " + str(self.damage) + "\n" + \
              "Weight: " + str(self.weight) + "\n" + \
              "--------------------\n")

    # Special Attack
    # 
    # Deals damage based on half of the weapon's level
    # times the weapon's base damage
    # 
    # Using this attack hurts the weapon
    def smack(self):
        if (self.current_health > 0):
            self.current_health -= 1
            return round(0.5 * self.level * self.damage)
        else:
            return 1

        

        
        
    

    

