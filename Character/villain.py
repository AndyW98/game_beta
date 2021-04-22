import json


class Villain (Character):

    def __init__(self, args):
        # Villains have 10 more health
        self.max_health += 10
        self.health = self.max_health

    