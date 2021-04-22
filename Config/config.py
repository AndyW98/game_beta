import json

from Character.character import Character
from Character.villain import Villain
from Character.hero import Hero

class Config():

    # This is for managing the config file
    def __init__(self, filename, params=[]):
        self.filename = filename
        self.char_list = {}

        self.data = self.read()
        if self.data is not None:
            self.make_chars()

        # Write to file if given parameters
        if params!=[]:
            self.write(params)

    #def write(self, params):

    # Returns the config data
    def get_data(self):
        return self.data
    
    # Returns the character list
    def get_char_list(self):
        return self.char_list

    # Read the config file
    def read(self):
        with open(self.filename) as f:
            data = json.load(f)
        return data
    
    # Dynamically make character objects from the config file
    def make_chars(self):
        for char_type in self.data['characters'].keys():
            for char in self.data['characters'][char_type].keys():
                if char_type == "villains":
                    self.char_list[char] = Villain(self.data['characters'][char_type][char])
                elif char_type == "heroes":
                    self.char_list[char] = Hero(self.data['characters'][char_type][char])
                else:
                    self.char_list[char] = Character(self.data['characters'][char_type][char])