'''
Abstract class of items
'''
class Item():

    def __init__(self, weight=1, name="item"):
        self.weight = weight
        self.name = name
        self.cost = 0

    # Gets weight of item
    def get_weight(self):
        return self.weight