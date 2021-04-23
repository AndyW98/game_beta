from Item.Weapon.weapon import Weapon, DamageType
from Item.item import Item


class Stick (Weapon):

    # Constructor
    def __init__(self, weight=1, power=1, level=1, name="stick", health=10):
        Weapon.__init__(self, weight, power, level, name, health)

        self.level = level
        self.name = name
        self.attack_type = DamageType.MELEE

    def __str__(self):
        stick_str = Weapon.__str__(self) + "\n" + \
                    "  Weapon Type: Stick\n"
        return stick_str

    # Getter

    # Printer
    def print_weapon_stats(self):
        str(super())
    
    def special_attack(self):
        """Deals a smacck attack.
        This attack decreases the weapon's health by 1
        """
        if (self.health > 0):
            self.health -= 1
            return round(0.5 * self.level * self.damage)
        else:
            return 1

        

        
        
    

    

