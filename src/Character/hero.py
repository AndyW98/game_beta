import json

from Character.character import Character

class Hero (Character):

    '''
    This is a Hero character
    '''
    def __init__(self, args):
        Character.__init__(self, args)
