from Item.Weapon.weapon import Weapon, DamageType

class Knife (Weapon):

    # Constructor
    def __init__(self, weight=1, power=1, level=1, name="stick", health=20):
        Weapon.__init__(self, weight, power, level, name, health)

        self.level = 1
        self.name = name
        self.attack_type = DamageType.MELEE

    # Methods

    def special_attack(self):
        """Deals a slash attack and inflicts bleed.
        This attack decreases the weapon's health by 1
        """
        if (self.health > 0):
            self.health -= 1
            return round(self.level * self.damage)
        else:
            return 1

    def inflict_bleed(self, char):
        pass