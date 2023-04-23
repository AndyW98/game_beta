from Combat.dice_roller import d8

class Combat:
    """How combat is conducted"""

    def __init__(self, attack_type, characters):
        """Constructor

        Keyword arguments:
        attack_type -- type of attack damage
        characters  -- characters in combat
        """        
        if attack_type == "melee":
            self.trade_damage(characters[0], characters[1])

    # Takes two characters and trades their damages at
    # each other
    def trade_damage(self, char_1, char_2):
        # Save damage before applying, to simulate
        # simultaneous damage
        char_1_dmg = char_1.deal_damage() + d8()[0][0]
        char_2_dmg = char_2.deal_damage() + d8()[0][0]

        # Apply unmodified damage to each character
        char_1.take_damage(char_2_dmg)
        char_2.take_damage(char_1_dmg)