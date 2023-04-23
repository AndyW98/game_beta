import json
from os import listdir
from os.path import isfile, join

from Character.character import Character
from Character.villain import Villain
from Character.hero import Hero

CONF_FOLDER = "src/Config/conf_dump"

class Config():

    """
    This is for managing the config files. It reads the conf_dump
    folder for all files and serializes them into a single dictionary.
    Use get_data() to retrieve the compiled config dictionary.
    """
    def __init__(self, params=[]):
        self.files = [f for f in listdir(CONF_FOLDER) if isfile(join(CONF_FOLDER, f))]
        self.char_list = {}

        self.data = {}
        self.read()
        if self.data is not None:
            self.make_chars()

        # Write to file if given parameters
        #if params!=[]:
        #    self.write(params)

    #def write(self, params):

    def get_data(self):
        """Return the config data"""
        return self.data
    
    def get_char_list(self):
        """Returns the character list"""
        return self.char_list

    def read(self):
        """Reads the config file"""
        for file in self.files:
            if file.split('.')[1] == 'json':
                with open(join(CONF_FOLDER, file)) as f:
                    self.data[file.split('.')[0]] = json.load(f)
    
    def make_chars(self):
        """Dynamically make character objects from the config file"""
        for file in self.data.keys():
            if file == 'characters':
                for char_type in self.data['characters'].keys():
                    for char in self.data['characters'][char_type].keys():
                        if char_type == "villains":
                            self.char_list[char] = Villain(self.data['characters'][char_type][char])
                        elif char_type == "heroes":
                            self.char_list[char] = Hero(self.data['characters'][char_type][char])
                        else:
                            self.char_list[char] = Character(self.data['characters'][char_type][char])