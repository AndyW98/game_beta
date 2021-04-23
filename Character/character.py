import json
from enum import Enum

from Character.Inventory.inventory import Inventory
from Item.Weapon.weapon import Weapon

class Character():

    '''
    A character in the game
    '''
    def __init__(self, args):
        # __init__ is the function that is called when an
        # object is declared. Typically, you'll want to put
        # class variables here, defined from the init
        # parameters
        self.name = args['name']
        self.level = args['level']
        self.health = args['health']
        self.base_stats = args['base_stats']

        self.bag = Inventory()
        self.weapon = Weapon() # Held weapon

        # Derived Stats
        self.max_health = 2 * self.base_stats['con'] * self.level
        self.health = self.max_health
        self.exp = 200 * (self.level - 1) * self.level
        self.carry_cap = 5 * args['base_stats']['str'] # Carrying Capacity

        self.damage = 2 * (self.base_stats['str'] - 10)
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
                "  Strength:     " + str(self.base_stats["str"]) + "\n" + \
                "  Dexterity:    " + str(self.base_stats["dex"]) + "\n" + \
                "  Constitution: " + str(self.base_stats["con"]) + "\n" + \
                "  Intelligence: " + str(self.base_stats["int"]) + "\n" + \
                "  Wisdom:       " + str(self.base_stats["wis"]) + "\n" + \
                "  Charisma:     " + str(self.base_stats["cha"]) + "\n" + \
                str(self.weapon) + \
                "--------------------\n" + \
                "Inventory - [" + str(self.bag.get_weight()) + \
                    " / " + str(self.carry_cap) + "]\n" + \
                str(self.bag)

        return stats

    # You'll notice that I'm defining the first parameter
    # of every function as 'self', this is because it's a
    # self-referential thing declaring it as a class function
    def print_name(self):
        print(self.name)

    # Printers

    def print_bag(self):
        print("Inventory Weight: " + \
              str(self.bag.get_weight()) + " / " + \
              str(self.carry_cap))
        print(self.bag)

    # Getters

    def get_damage(self):
        return self.damage
    
    def get_defense(self):
        return self.defense
    
    def get_weapon(self):
        return self.weapon

    # Gets the stats of the caracter
    def get_stats(self):
        my_dict = {
            'name': self.name,
            'level': self.level,
            'health': self.health,
            'max_health': self.max_health,
            'base_stats': self.base_stats
        }
        return json.dumps(my_dict, indent=2)

    # Prints the character's stat prettily
    def pretty_print_stats(self):
        stats = self.__str__()
        print(stats)


    # Setters

    def set_name(self, name):
        self.name = name

    def set_weapon(self, weapon):
        self.weapon = weapon

    # Functions

    # ------------------------------------------------
    # Levels up character
    # ------------------------------------------------
    # Expects a string for stat1 and stat2 to increase
    # the corresponding base stat

    def level_up(self, stat1, stat2, level_add=1):
        self.level += level_add
        
        self.max_health += int(0.5 * self.base_stats['con'])
        self.health = self.max_health
        
        self.exp = 200 * (self.level - 1) * self.level

        self.base_stats[stat1] += level_add
        self.base_stats[stat2] += level_add

    # Adds item to the character's inventory
    # Expects an Item object
    def add_item(self, item):
        self.bag.add_item(item)

    # Expects that weapon is a Weapon
    def equip_weapon(self, weapon):
        if (weapon in self.bag.get_bag()):
            self.set_weapon(weapon)


    # ------------------------------------------------
    # Deal Damage
    # ------------------------------------------------
    # Expects
    def deal_damage(self, modifiers=1):
        
        damage = modifiers * (self.damage + self.weapon.get_damage())

        return damage

    # Expects incoming unmodified damage
    def take_damage(self, incoming_damage):
        self.health -= max(0, (incoming_damage - self.get_defense()))
