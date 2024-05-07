# ---------------------------------------------------------------------
class RetailItem:
    # holds data about an item in a retail store
    # stores item description, units in inventory, and price
    # in attributes
    
    def __init__(self, description, units, price):
        # intializes the attributes for item 1
        
        self.__description = description
        self.__units = units
        self.__price = price
        
    def get_description(self):
        
        return self.__description
    
    def get_units(self):
        
        return self.__units
    
    def get_price(self):
        
        return self.__price
    
    def __str__(self):
        return self.__description, self.__units, self.__price