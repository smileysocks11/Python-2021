import random

# class Coin simulates a coin being tossed
# note that the name of the class has a capital leter for the first
# letter, this is a standard programming convnetion and should be followed

class Coin:
    
    # a class should begin with the _init_ method
    # this method executes first, as an intializiation of the class
    # the (self) parameter is a generally accepted naming convenion
    # for the parameter within a class, and is required
    
    # initialize the data attribute with 'Heads' to indicate
    # the coin begins in a head's up position
    
    def _init_(self):
        self.sideup = 'Heads'
        
    # the toss method generates a random number in the range of 0 through 1
    # if the number is 0, sideup is assigned 'Heads'
    # otherwise sideup is assigned 'Tails'
    
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
            
    # get sideup method returns the current state of the coin
    # or the side that is facing up
    
    def get_sideup(self):
        return self.sideup
    
    def coin_main():
        # coin man accepts no arguments
        # it uses the Coin class to create an object
        
        # create an object from the Coin class
        my_coin = Coin()
        
        # display the side of the coin that is facing up
        print('This side is up: ', my_coin.get_sideup())
        
        # toss the coin
        print('Tossing the coin...')
        my_coin.toss()
        
        # display the side of the coin that is facing up
        print('This side is up: ', my_coin.get_sideup())
        
    # call the coin main function to flip the coin
    coin_main()