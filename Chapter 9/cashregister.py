import retailitem
# ---------------------------------------------------------------------
class CashRegister:
    # can internally keep a list of RetailItem objects
    
    def __init__(self):
    
        self.__purchased = []
        self.__item_numbers = []
        self.__item_amounts = []
        self.__total = 0
        
        # creates three objects from the RetailItem class
        self.__item1 = retailitem.RetailItem('Jacket', 12, 59.95)
        self.__item2 = retailitem.RetailItem('Designer Jeans', 40, 34.95)
        self.__item3 = retailitem.RetailItem('Shirt', 20, 24.95)
        
    def purchase_item(self, purchased_item, amount):
        # accepts a RetailItem object as an argument
        # each time purchase_item is called, the RetailItem object
        # that is passed as an argument is added to the list
        
        # adds the object to the list depending on which ones
        # the user chose to purchase
        if purchased_item == 1:
            
            self.__purchased.append(self.__item1)
            self.__item_numbers.append(1)
            self.__item_amounts.append(amount)
           
        if purchased_item == 2:
            
            self.__purchased.append(self.__item2)
            self.__item_numbers.append(2)
            self.__item_amounts.append(amount)
            
        if purchased_item == 3:
            
            self.__purchased.append(self.__item3)
            self.__item_numbers.append(3)
            self.__item_amounts.append(amount)
            
    
    def get_total(self):
        # accepts the list of items and the total price
        # returns the total price of all the RetailItems objects stored in the CashRegister object's internal list
        
        index = 0
        
        # adds the price of each purchased item to the total
        for item in self.__item_numbers:
            
            if item== 1:
                # gets the price of the item from the retailitem class and
                price = self.__item1.get_price()
                # adds it to the total
                self.__total += (price * self.__item_amounts[index])
                
            if item == 2:
                # gets the price of the item from the retailitem class and
                price = self.__item2.get_price()
                # adds it to the total
                self.__total += (price * self.__item_amounts[index])
                
            if item == 3:
                # gets the price of the item from the retailitem class and
                price = self.__item3.get_price()
                # adds it to the total
                self.__total += (price * self.__item_amounts[index])
        
        # displays the total
        print('The total price of your items in the cart is: $' + str(format((self.__total), '.2f')))
        
    def show_items(self):
        # displays data about the RetailItems objects stored in the
        # CashRegister's internal list
        
        print('The following items are in your cart:')
        print('-------------------------')
        
        index = 0
        
        for item in self.__item_numbers:
            
            if item == 1:
                print(self.__item_amounts[index], 'jackets.')
            
            if item == 2:
                print(self.__item_amounts[index], 'designer jeans.')
                
            if item == 3:
                print(self.__item_amounts[index], 'shirts.')
             
            index += 1
             
    def clear(self):
        # accepts the list of items
        # clears the CashRegister's internal list
        
        self.__purchased = []
        self.__item_numbers = []
        self.__item_amounts = []
        
        