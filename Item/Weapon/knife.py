from Item.Weapon.weapon import Weapon, DamageType

class Knife (Weapon):

    # Constructor
    def __init__(self, args, level=1, name="stick"):
        Weapon.__init__(self, args, level, name)

        self.level = 1
        self.name = name
        self.attack_type = DamageType.MELEE

    # Deals damage based on half of the weapon's level
    # times the weapon's base damage
    # 
    # Eventually will add bleed
    def slash(self):
        return round(0.5 * self.level * self.damage)