

class Inventory():

    '''
    This is a Character's inventory
    '''
    # Constructor
    def __init__(self):
        self.bag = []
        self.current_weight = 0

    # String representation
    def __str__(self):
        return str(self.bag)

    # Getters

    def get_weight(self):
        return self.current_weight

    def get_bag(self):
        return self.bag

    # Add item
    # Expects an Item object
    def add_item(self, item):
        self.bag.append(item)
        self.current_weight += item.get_weight()

    # Remove item
    # Expects an Item object
    def remove_item(self, item):
        self.bag.remove(item)
        self.current_weight -= item.get_weight()
    
    