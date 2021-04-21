
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
        self.max_health = args['max_health']
        self.base_stats = args['base_stats']
    
    # You'll notice that I'm defining the first parameter
    # of every function as 'self', this is because it's a
    # self-referential thing declaring it as a class function
    def print_name(self):
        print(self.name)

    # Getters

    def get_stats(self):
        my_dict = {
            'name': self.name,
            'level': self.level,
            'health': self.health,
            'max_health': self.max_health,
            'base_stats': self.base_stats
        }
        return json.dumps(my_dict, indent=2)

    def pretty_print_stats(self):
        stats = "--------------------\n" + \
                "Name:   " + self.name + "\n" \
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

    def level_up(self):
        self.level += 1
        self.max_health += int(0.5 * self.base_stats['con'])
        self.health = self.max_health

