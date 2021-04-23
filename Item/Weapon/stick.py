from Item.Weapon.weapon import Weapon, DamageType

class Stick (Weapon):

    # Constructor
    def __init__(self, args, level=1, name="stick"):
        Weapon.__init__(self, args, level, name)

        self.level = level
        self.name = name
        self.attack_type = DamageType.MELEE

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

    # Deals damage based on half of the weapon's level
    # times the weapon's base damage
    def smack(self):
        return round(0.5 * self.level * self.damage)

    

