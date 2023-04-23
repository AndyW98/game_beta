

class Inventory():

    '''
    This is a Character's inventory
    '''
    # Constructor
    def __init__(self, items=[]):
        self.bag = items
        self.current_weight = 0

    # String representation
    def __str__(self):
        return str(self.bag)

    # Getters

    def get_weight(self):
        """Returns the weight of the inventory"""
        return self.current_weight

    def get_bag(self):
        """Returns the bag of the inventory"""
        return self.bag

    def add_item(self, item):
        """Adds item to the inventory

        Keyword arguments:
        item -- an Item object
        """
        if isinstance(item, Item):
            self.bag.append(item)
            self.current_weight += item.get_weight()
        else:
            print(str(item) + "is not an item!")

    def remove_item(self, item):
        """Removes item from the inventory

        Keyword arguments:
        item -- an Item object
        """
        if (isinstance(item, Item) and item in self.bag):
            self.bag.remove(item)
            self.current_weight -= item.get_weight()
        else:
            print(str(item) + " is not in the bag!")
    
    