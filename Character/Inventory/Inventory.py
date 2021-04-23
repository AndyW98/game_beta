        """Returns the weight of the inventory"""
        """Returns the bag of the inventory"""
        """Adds item to the inventory

        Keyword arguments:
        item -- an Item object
        """
        if isinstance(item, Item):
        else:
            print(str(item) + "is not an item!")
        """Removes item from the inventory

        Keyword arguments:
        item -- an Item object
        """
        if (isinstance(item, Item) and item in self.bag):
        else:
            print(str(item) + " is not in the bag!")
