'''
Abstract class of items
'''

class Item():

    def __init__(self, args, name="item"):
        self.weight = args['weight']
        self.name = name
        self.cost = 0

    # Gets weight of item
    def get_weight(self):
        return self.weight