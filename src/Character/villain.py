import json

from Character.character import Character
from random import sample

class Villain (Character):

    """This is a Villain character"""

    def __init__(self, args):

        Character.__init__(self, args)

        # Villains have 5 more health
        self.max_health += 5
        self.health = self.max_health

        # Villains have 1 more defense
        self.defense += 1

        # Villains have 1 more strength 
        # and 1 more intelligence

        rand_stat = sample(super().stat_list, 2)

        self.base_stats[rand_stat[0]] += 1
        self.base_stats[rand_stat[1]] += 1