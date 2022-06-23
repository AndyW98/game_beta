import json
from enum import Enum

from Character.Inventory.inventory import Inventory
from Item.Weapon.weapon import Weapon

class Character():

    """A character in the game"""

    stat_list = ['str', 'dex', 'con', 'int', 'wis', 'cha']

    def __init__(self, args):
        # __init__ is the function that is called when an
        # object is declared. Typically, you'll want to put
        # class variables here, defined from the init
        # parameters
        self.name = args['name']
        self.sprite = args['sprite']
        self.level = args['level']
        self.base_stats = args['base_stats']

        self.inventory = Inventory()
        self.weapon = Weapon() # Held weapon

        # Derived Stats
        self.max_health = 2 * self.base_stats['con'] * self.level
        self.health = self.max_health
        self.exp = 200 * (self.level - 1) * self.level
        self.carry_cap = 5 * self.base_stats['str'] # Carrying Capacity

        self.damage = 2 * (self.base_stats['str'] - 10)
        self.magic = 2 * (self.base_stats['int'] - 10)
        self.defense = round(0.5 * (self.base_stats['dex'] - 10))

    def __str__(self):
        stats = "--------------------\n" + \
                "Name:   " + self.name + "\n" \
                "--------------------\n" + \
                "Level:  " + str(self.level) + "\n" + \
                "--------------------\n" + \
                "Exp:    " + str(self.exp) + "\n" + \
                "--------------------\n" + \
                "Health: " + str(self.health) + \
                " / " + str(self.max_health) + "\n" + \
                "--------------------\n" + \
                "Stats -\n" + \
                "  Strength:     " + str(self.base_stats['str']) + "\n" + \
                "  Dexterity:    " + str(self.base_stats['dex']) + "\n" + \
                "  Constitution: " + str(self.base_stats['con']) + "\n" + \
                "  Intelligence: " + str(self.base_stats['int']) + "\n" + \
                "  Wisdom:       " + str(self.base_stats['wis']) + "\n" + \
                "  Charisma:     " + str(self.base_stats['cha']) + "\n" + \
                str(self.weapon) + \
                "--------------------\n" + \
                "Inventory - [" + str(self.inventory.get_weight()) + \
                    " / " + str(self.carry_cap) + "]\n" + \
                str(self.inventory)

        return stats

    # You'll notice that I'm defining the first parameter
    # of every function as 'self', this is because it's a
    # self-referential thing declaring it as a class function
    def print_name(self):
        print(self.name)

    # Printers

    def print_inventory(self):
        print("Inventory Weight: " + \
              str(self.inventory.get_weight()) + " / " + \
              str(self.carry_cap))
        print(self.inventory)

    # Getters

    def get_damage(self):
        return self.damage
    
    def get_defense(self):
        return self.defense
    
    def get_weapon(self):
        return self.weapon

    def get_stats(self):
        """Returns the character's stats"""
        my_dict = {
            'name': self.name,
            'level': self.level,
            'health': self.health,
            'max_health': self.max_health,
            'base_stats': self.base_stats
        }
        return my_dict

    # Printers

    def pretty_print_stats(self):
        stats = self.__str__()
        print(stats)


    # Setters

    def set_name(self, name):
        """Sets character's name"""
        self.name = name

    def set_weapon(self, weapon):
        """Sets character's equipped weapon"""
        self.weapon = weapon

    # Functions

    # ------------------------------------------------
    # Levels up character
    # ------------------------------------------------
    # Expects a string for stat1 and stat2 to increase
    # the corresponding base stat

    def level_up(self, stat1, stat2, level_add=1):
        """Levels up character

        Keyword arguments:
        stat1     -- 1st stat to increase
        stat2     -- 2nd stat to increase
        level_add -- number of levels to add
        """
        self.level += level_add
        
        self.max_health += int(0.5 * self.base_stats['con'])
        self.health = self.max_health
        
        self.exp = 200 * (self.level - 1) * self.level

        self.base_stats[stat1] += level_add
        self.base_stats[stat2] += level_add

    def add_item(self, item):
        """Adds item to the character's inventory

        Keyword arguments:
        item -- an Item object
        """
        self.inventory.add_item(item)

    def equip_weapon(self, weapon):
        """Equips weapon to character

        Keyword arguments:
        weapon -- a Weapon object
        """
        if (weapon in self.inventory.get_bag()):
            self.set_weapon(weapon)

    def attack(self, character):
        """Attacks another character

        Keyword arguments:
        character -- another Character
        """
        if not isinstance(character, Character):
            # Character's cannot attack non-characters
            print("You can't attack that!")
        else:    
            damage = self.deal_damage()
            character.take_damage(damage)

    def deal_damage(self, modifiers=1):
        """Deals damage to something

        Keyword arguments:
        modifiers -- damage modifiers (default 1)
        """    
        damage = modifiers * (self.damage + self.weapon.get_power())

        return damage

    def take_damage(self, incoming_damage):
        """Decreases Character's health
        
        Keyword arguments:
        incoming_damage -- damage to be dealt to character
        """
        self.health -= max(0, (incoming_damage - self.get_defense()))
