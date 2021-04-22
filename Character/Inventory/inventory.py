

class Inventory():

    '''
    This is a Character's inventory
    '''
    # Constructor
    def __init__(self):
        self.bag = []
        self.current_weight = 0

    # Getters

    def get_weight(self):
        return self.current_weight

    # Add item
    def add_item(self, item, weight):
        self.bag.append(item)
        self.current_weight += weight

    # Remove item
    def remove_item(self, item, weight):
        self.bag.remove(item)
        self.current_weight -= weight
    
    