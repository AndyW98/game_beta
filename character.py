
class Character():

    '''
    A character in the game
    '''
    def __init__(self, name, health):
        # __init__ is the function that is called when an
        # object is declared. Typically, you'll want to put
        # class variables here, defined from the init
        # parameters
        self.name = name
        self.health = health
    
    # You'll notice that I'm defining the first parameter
    # of every function as 'self', this is because it's a
    # self-referential thing declaring it as a class function
    def print_name(self):
        print(self.name)