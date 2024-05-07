import retailitem
import cashregister
# ---------------------------------------------------------------------
def retail_main(): # Exercise 5
    # retail_main accepts no arguments
    # creates three RetailItem objects and stores data in them
        
    # creates three objects from the RetailItem class
    item1 = retailitem.RetailItem('Jacket', 12, 59.95)
    item2 = retailitem.RetailItem('Designer Jeans', 40, 34.95)
    item3 = retailitem.RetailItem('Shirt', 20, 24.95)
    
    # outputs the data for item 1
    print('Item #1:')
    print('Description:', item1.get_description())
    print('Units in inventory:', item1.get_units())
    print('Price:', item1.get_price())
    print()
    
    # outputs the data for item 2
    print('Item #2:')
    print('Description:', item2.get_description())
    print('Units in inventory:', item2.get_units())
    print('Price:', item2.get_price())
    print()
    
    # outputs the data for item 3
    print('Item #3:')
    print('Description:', item3.get_description())
    print('Units in inventory:', item3.get_units())
    print('Price:', item3.get_price())
    print()
    
# ---------------------------------------------------------------------
    
def register_main(): # Exercise 7
    # register_main accepts no arguments
    # allows the user to select several items for purchase
    # when the user is ready to check out,
    # the program should display a list of all items they have selected for purchase,
    # as well as the total price
    
    finished = False
    quantity1 = 12
    quantity2 = 40
    quantity3 = 20
    
    # creates a cash register object
    objectt = cashregister.CashRegister()
    
    while finished == False:
        
        # prints the menu choices
        print('-----------------')
        print('1: Jacket,', quantity1, 'units left in stock.')
        print('2: Designer Jeans,', quantity2, 'units left in stock.')
        print('3: Shirt,', quantity3, 'units left in stock.')
        print('4: Clear cart')
        print('0: Check out')
        print()
        
        # gets input from the user for what items they would like to purchase
        purchased_item = int(input('Enter a number choice from the menu: '))
        
        # validation
        while purchased_item > 4:
            purchased_item = int(input('Error. Please enter a valid number choice from the menu: '))
            
        # ends the loop if the user decides to finish purchasing
        if purchased_item == 0:
            finished = True
            
        # clears the cart is the user wants to
        if purchased_item == 4:
            objectt.clear()
        
        # else it calls purchased item to add the item to the list
        elif finished != True:
            amount = int(input('How many of this item would you like to purchase? '))
            print()
            
            # checks to make sure there is enough quantity of the item
            if purchased_item == 1:
                while (quantity1 - amount) < 0:
                    amount = int(input('There are not enough of this item in stock. Please enter a valid amount: '))
                quantity1 -= amount
                    
            # checks to make sure there is enough quantity of the item
            if purchased_item == 2:
                while (quantity2 - amount) < 0:
                    amount = int(input('There are not enough of this item in stock. Please enter a valid amount: '))
                    
                quantity2 -= amount
                
            # checks to make sure there is enough quantity of the item
            if purchased_item == 3:
                while (quantity3 - amount) < 0:
                    amount = int(input('There are not enough of this item in stock. Please enter a valid amount: '))
                    
                quantity3 -= amount
                
            objectt.purchase_item(purchased_item, amount)
    
    # calls show_items to display a list of all the items the user checked out
    print()
    objectt.show_items()
    
    # calls get_total to calculate total at check out
    # and displays it to the user
    print()
    objectt.get_total()
    