import json

class Config():

    # This is for managing the config file
    def __init__(self, filename, params=[]):
        self.filename = filename

        # Write to file if given parameters
        if params!=[]:
            self.write(params)

    #def write(self, params):

    def read(self):
        with open(self.filename) as f:
            data = json.load(f)
        return data
    

        