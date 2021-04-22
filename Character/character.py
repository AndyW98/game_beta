import json

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

        self.max_health = 2 * args['base_stats']['con'] * args['level']
        self.health = self.max_health
        self.exp = 200 * (self.level - 1) * self.level

        self.damage = args['damage']
        self.defense = args['defense']
    
    # You'll notice that I'm defining the first parameter
    # of every function as 'self', this is because it's a
    # self-referential thing declaring it as a class function
    def print_name(self):
        print(self.name)

    def get_damage(self):
        return self.damage
    
    def get_defense(self):
        return self.defense
    
    # Expects incoming unmodified damage
    def take_damage(self, incoming_damage):
        self.health -= max(0, (incoming_damage - self.get_defense()))

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
                "Stats            \n" + \
                "--------------------\n"
        print(stats)



    # Setters

    def set_name(self, name):
        self.name = name

    # Functions

    def level_up(self, level_add=1):
        self.level += level_add
        self.max_health += int(0.5 * self.base_stats['con'])
        self.health = self.max_health
        self.exp = 200 * (self.level - 1) * self.level