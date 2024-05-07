import math
import random
import turtle
import my_graphics as graphics

# ---------------------------------------------------------------------

def sales_tax(): # Exercise 2
    # sales_tax accepts no arguments
    # prompts the user to enter the sale amount
    # calls functions
    
    sale_amount = int(input('Enter the sale amount: '))
    
    # validation
    while sale_amount < 0:
        sale_amount = int(input('Error. Please enter a valid sale amount: '))
    
    find_total_sale(sale_amount)
    state_tax = find_state_tax(sale_amount)
    county_tax = find_county_tax(sale_amount)
    total_tax = find_total_tax(state_tax, county_tax)
    find_purchase_price(sale_amount, total_tax)

def find_total_sale(sale_amount):
    # find_total_sale accepts integer sale_amount
    # calculates the total sale
    # returns total sale amount
    
    # calculates
    total_sale = sale_amount + (sale_amount * .05) + (sale_amount * .025)
    
    # outputs
    print('Your total sale is:\t\t$\t', format(total_sale, '.2f'))
    

def find_purchase_price(sale_amount, total_tax):
    # find_purchase_price accepts integers sale_amount and total_tax
    # calculates the total purchase price
    # returns purchase price
    
    # calculates
    purchase_price = sale_amount + total_tax
    
    # outputs
    print('Your purchase price was:\t$\t', format(purchase_price, '.2f'))
    
    # returns
    return purchase_price

def find_state_tax(sale_amount):
    # find_state_tax accepts an integer sale_amount
    # calculates the state tax on the sale amount
    # returns and outputs the state tax amount
    
    # calculates
    state_tax = sale_amount * .05
    
    # outputs
    print('Your state tax amount is:\t$\t', format(state_tax, '.2f'))
    
    # returns
    return state_tax

def find_county_tax(sale_amount):
    # find_county_tax accepts an integer sale_amount
    # calculates the county tax on the sale amount
    # returns and outputs the county tax amount
    
    # calculates
    county_tax = sale_amount * .025
    
    # outputs
    print('Your county tax amount is:\t$\t', format(county_tax, '.2f'))
    
    # returns
    return county_tax

def find_total_tax(state_tax, county_tax):
    # total_tax accepts integers state_tax and county_tax
    # calculates the total tax amount
    # returns and outputs the total tax amount
    
    # calculates
    total_tax = state_tax + county_tax
    
    # outputs
    print('Your total tax amount is:\t$\t', format(total_tax, '.2f'))
    
    # returns
    return total_tax

# ---------------------------------------------------------------------

def calories(): # Exercise 6
    # calories() accepts no arguments
    # prompts user to enter the amount of carbs and fat they consumed in grams
    # calls functions carbs and fat
    
    # prompts user
    carb_grams = int(input('How many grams of carbs did you consume? '))
    
    # validation
    while carb_grams < 0:
        carb_grams = int(input('Error. Please enter a valid number of grams of carbs you consumed: '))
        
    # prompts user
    fat_grams = int(input('How many grams of fat did you consume? '))
    
    # validation
    while fat_grams < 0:
        fat_grams = int(input('Error. Please enter a valid amount of grams of fat you consumed: '))
        
    print()
    print('Here is your calorie intake for the day.')
    
    # calls functions
    carbs(carb_grams)
    fat(fat_grams)
    
def carbs(carb_grams):
    # carbs accepts an integer carb_grams
    # calculates the number of calories that result from the calories
    # outputs calories
    
    # calculates
    carb_calories = carb_grams * 4
    
    # outputs
    print('You consumed', carb_calories, 'worth of carbs today. Nice work...')
    
def fat(fat_grams):
    # fat accepts an integer fat_grams
    # calculates the number of calories that result from the fat
    # outputs calories
    
    # calculates
    fat_calories = fat_grams * 9
    
    # outputs
    print('You consumed', fat_calories, 'calories worth of fats today. Nice work...')
    
# ---------------------------------------------------------------------

def stadium_seating(): # Exercise 7
    # stadium_seating accepts no arguments
    # calls functions
    a_total = class_a()
    b_total = class_b()
    c_total = class_c()
    total_sales(a_total, b_total, c_total)
    
def class_a():
    # class_a accepts no arguments
    # prompts user to enter the number of class a tickets that were sold
    # calculates the amount of money sold from those tickets
    
    # prompts user
    a_tickets = int(input('Enter the number of Class A tickets sold: '))
    
    # validation
    while a_tickets < 0:
        a_tickets = int(input('Error. Enter a valid number of Class A tickets sold: '))
    
    # calculates and returns 
    return a_tickets * 20

def class_b():
    # class_b accepts no arguments
    # prompts user to enter the number of class b tickets that were sold
    # calculates the amount of money sold from those tickets
    
    # prompts user
    b_tickets = int(input('Enter the number of Class B tickets sold: '))
    
    # validation
    while b_tickets < 0:
        b_tickets = int(input('Error. Enter a valid number of Class B tickets sold: '))
    
    return b_tickets * 15

def class_c():
    # class_c accepts no arguments
    # prompts user to enter the number of class c tickets that were sold
    # calculates the total amount of money sold from those tickets
    
    # prompts user
    c_tickets = int(input('Enter the number of Class C tickets sold: '))
    
    # validation
    while c_tickets < 0:
        c_tickets = int(input('Error. Enter a valid number of Class C tickets sold: '))
        
    return c_tickets * 10

def total_sales(a, b, c):
    # total_sales accepts integers a_tickets, b_tickets, and c_tickets
    # calculates the total amount of income generated from ticket sales
    # outputs total
    
    # calculations
    total = a + b + c
    
    # outputs
    print()
    print('The total income sales from tickets is: $', format(total, '.2f'), sep = '')
    
# ---------------------------------------------------------------------

# constants
GALLONS_PER_FOOT = .00892857142
HOURS_PER_FOOT = .07142857142
COST_PER_HOUR = 35

def paint_estimator(): # Exercise 8
    # paint_estimator accepts no arguments
    # asks the user to enter the square feet of wall space to be painted and the price of paint per gallon
    # calls the functions
    
    # prompts user
    total_feet = float(input('Please enter the total square feet to be painted: '))
    cost_per_gallon = int(input('How much does each gallon of paint cost? '))
    
    # outputs beginning of chart
    print('The cost breakdown to paint', total_feet, 'square feet is: ')
    print('--------------------------------------------------')
    
    # calls all necessary functions
    total_paint_cost = find_paint_cost(total_feet, cost_per_gallon)
    total_labor_cost = find_labor_cost(total_feet)
    total_cost = find_total_cost(total_paint_cost, total_labor_cost)
    
def find_paint_cost(total_feet, cost_per_gallon):
    # find_paint_cost accepts integers total_feet and cost_per_gallon
    # calculates the total cost of paint
    # outputs and returns the total cost of paint
    
    # calculates
    gallons_needed = GALLONS_PER_FOOT * total_feet
    total_paint_cost = math.ceil(gallons_needed * cost_per_gallon)
    
    if (total_paint_cost % cost_per_gallon) > 0:
       total_paint_cost += cost_per_gallon - (total_paint_cost % cost_per_gallon)
    
    # outputs
    print('Total cost of paint: $', format(total_paint_cost, '.2f'), sep = '')
    
    # returns
    return total_paint_cost

def find_labor_cost(total_feet):
    # find_labor_cost accepts integer total_feet
    # calculates the total labor cost
    # outputs and returns the total labor cost
    
    # calculates
    hours_needed = HOURS_PER_FOOT * total_feet
    total_labor_cost = hours_needed * COST_PER_HOUR
    
    # outputs
    print('Total labor cost: $', format(total_labor_cost, '.2f'), sep = '')
    
    # returns
    return total_labor_cost

def find_total_cost(total_paint_cost, total_labor_cost):
    # find_total_cost accepts integers total_paint_cost and total_labor_cost
    # calculates the total cost of the job
    # outputs the total cost of the job
    
    # calculates
    total_cost = total_paint_cost + total_labor_cost
    
    # outputs to user
    print('Total cost of the job is: $', format(total_cost, '.2f'), sep = '')
    
# ---------------------------------------------------------------------

def math_quiz(): # Exercise 11
    # math_quiz accepts no arguments
    # calls get_numbers to get two random numbers
    # loops while continue = y
    # outputs the problem to the user and prompts to answer the question
    # prompts the user to continue (y/n)
    
    continues = 'y'

    # loops until the user wants to stop
    while continues == 'y':
        
        # calls functions to get random numbers
        number1 = get_numbers()
        number2 = get_numbers()
    
        # outputs the math problem to the user
        print('\t', number1)
        print('+\t', number2)
        
        # asks the user to enter the answer
        print()
        guess = int(input('What is the answer to this problem? '))
        print()
        answer = number1 + number2
        
        # if the user is correct, show a correct message
        if guess == answer:
            print('You are correct!')
          
        # if the user is incorrect, show an incorrect message
        else:
            print('You are incorrect. The correct answer was', answer)
            
        # asks the user if they want to continue
        continues = input('Do you want another problem? (y/n) ')
        continutes = continues.lower()
        
def get_numbers():
    # get_numbers accepts no arguments
    # generates and returns two random integers from 1-200
    
    # generates two random integers
    number1 = random.randint(1, 200)
    number2 = random.randint(1, 200)
    
    # returns those integers
    return number1
    return number2

# ---------------------------------------------------------------------

def time_loop(): # Exercise 13
    # time_loop accepts no arguments
    # loops 10 times
    # calls falling_distance passing time
    # outputs a table with each second and how far the object fell that second
    
    # outputs table
    print()
    print('Here is the distnace an object will fall for 10 seconds:')
    print('------------------------------------------------------')
    
    # for each second, outputs the distance the object will fall
    for time in range(1, 11):
        
        distance = falling_distance(time)
        print(time, 'sec\t\t\t', format(distance, '.2f'), 'm')
        
def falling_distance(time):
    # falling_distance accepts an integer time
    # calculates the distance fallen
    # returns distance
    
    # calculates
    distance = ( .5 * 9.8 * time * time)
    
    # returns
    return distance
    
# ---------------------------------------------------------------------

# constants

ROCK = 1
PAPER = 2
SCISSORS = 3
LIZARD = 4
SPOCK = 5

def game(): # Exercise 21
    # game accepts no arguments
    # calls functions to play the game
    # outputs a greeting, each player's weapon, and prompts to continue
    
    continues = 'y'
    
    while continues == 'y':
        
        # calls functions
        computer = comp_choice()
        player, player2 = player_choice()
        
        # outputs each player's choice
        print('You chose....', player2)
        print()
        
        if computer == ROCK:
            print('The computer chose.... rock.')
        
        if computer == PAPER:
            print('The computer chose.... paper.')
        
        if computer == SCISSORS:
            print('The computer chose.... scissors.')
        
        if computer == LIZARD:
            print('The computer chose.... lizard.')
        
        if computer == SPOCK:
            print('The computer chose.... Spock.')
        
        print()
    
        # calls functions
        winner(computer, player)
        print()
    
        # asks user if they wish to continue
        continues = input('Would you like to play again? (y/n) ')
        continues = continues.lower()
        print()
        
def comp_choice():
    # comp_choice accepts no arguments
    # chooses a random integer from 1-5 and returns the integer
    
    # generates random number
    computer = random.randint(1, 5)
    
    return computer

def player_choice():
    # player_choice accepts no arguments
    # prompts user for their weapon, and returns the weapon
    
    player = str(input('Choose your weapon. (rock, paper, scissors, lizard, spock): '))
    print()
    player = player.lower()
    player2 = player.lower()
    
    if player == 'rock':
        player = ROCK
        
    if player == 'paper':
        player = PAPER
        
    if player == 'scissors':
        player = SCISSORS
        
    if player == 'lizard':
        player = LIZARD
        
    if player == 'spock':
        player == SPOCK
        
    return player, player2;

def winner(computer, player):
    # winner accepts strings computer and player
    # determines the winner
    # outputs who won the game
    
    if computer == player:
        print('The round resulted in a tie.')
        
    if computer == SPOCK and player == SCISSORS:
        print('The computer won this round, Spock smashes scissors.')
    
    if player == SPOCK and computer == SCISSORS:
        print('You won this round, Spock smashes scissors.')
        
    if computer == SCISSORS and player == LIZARD:
        print('The computer won this round, scissors decapitates lizard.')
        
    if player == SCISSORS and computer == LIZARD:
        print('You won this round, scissors decapitates lizard.')
        
    if computer == SCISSORS and player == PAPER:
        print('The computer won this round, scissors cuts paper.')
    
    if player == SCISSORS and computer == PAPER:
        print('You won this round, scissors cuts paper.')
        
    if computer == PAPER and player == SPOCK:
        print('The computer won this round, paper disaproves Spock.')
        
    if player == PAPER and computer == SPOCK:
        print('You won this round, paper disaproves Spock.')
        
    if computer == SPOCK and player == ROCK:
        print('The computer won this round, Spock vaporizes rock.')
        
    if player == SPOCK and computer == ROCK:
        print('You won this round, Spock vaporizes rock.')
        
    if computer == LIZARD and player == SPOCK:
        print('The computer won this round, lizard poisons Spock.')
        
    if player == LIZARD and computer == SPOCK:
        print('You won this round, lizard poisons Spock.')
        
    if computer == LIZARD and player == PAPER:
        print('The computer won this round, lizard eats paper.')
        
    if player == LIZARD and computer == PAPER:
        print('You won this round, lizard eats paper.')
        
    if computer == ROCK and player == LIZARD:
        print('The computer won this round, rock crushes lizard.')
        
    if player == ROCK and computer == LIZARD:
        print('You won this round, rock crushes lizard.')
        
    if computer == ROCK and player == SCISSORS:
        print('The computer won this round, rock crushes scissors.')
        
    if player == ROCK and computer == SCISSORS:
        print('You won this round, rock crushes scissors.')
        
    if computer == PAPER and player == ROCK:
        print('The computer won this round, paper covers rock.')
        
    if player == PAPER and computer == ROCK:
        print('You won this round, paper covers rock.')
        
# ---------------------------------------------------------------------

def drawSnowman(): # Exercise 23
    # drawSnowman accepts no arguments
    # calls all other functions
    
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawFace()
    drawHat()
    
def drawBase():
    # drawBase accepts no arguments
    # draws the base of the snowman
    # outputs the bottom-most large circle

    graphics.circle(0, -150, 100, '#CCCCFF')
    
def drawMidSection():
    # drawMidSection accepts no arguments
    # draws the mid section of the snowman
    # outputs the second largest circle on top of the first

    graphics.circle(0, 25, 75, '#CCCCFF')
    
def drawArms():
    # drawArms accepts no arguments
    # draws the arms for the snowman
    # seven total lines depicting arms
    turtle.color('brown')

    # right arm
    turtle.penup()
    turtle.goto(75, 30)
    turtle.pendown()
    turtle.setheading(45)
    turtle.forward(100)
    
    turtle.setheading(90)
    turtle.forward(25)
    
    turtle.penup()
    turtle.setheading(-90)
    turtle.forward(25)
    
    turtle.pendown()
    turtle.setheading(-45)
    turtle.forward(25)
    
    # left arm
    turtle.penup()
    turtle.goto(-75, 30)
    
    turtle.pendown()
    turtle.setheading(135)
    turtle.forward(50)
    
    turtle.setheading(100)
    turtle.forward(75)
    
    turtle.setheading(110)
    turtle.forward(25)
    
    turtle.penup()
    turtle.backward(25)
    
    turtle.setheading(200)
    turtle.pendown()
    turtle.forward(25)
    
def drawHead():
    # drawHead accepts no arguments
    # draws the head for the snowman, with eyes and a mouth
    # a smaller circle on top of the middle circle
    # and two filled circles for eyes and a line for the mouth
    
    turtle.color('black')
    turtle.setheading(0)
    graphics.circle(0, 150, 50, '#CCCCFF')
    
def drawFace():
    # drawFace accepts no arguments
    # draws eyes, a mouth, and a corncob pipe, with smoke billowing out
    # outputs two filled circles for eyes, a line for the mouth, a filled square attached to a line,
    # attached to the mouth for the pipe
    # loop to create grey smoke billowing out of the pipe with a thicker pen size
    
    # mouth
    turtle.penup()
    turtle.goto(-10, 115)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(30)
    turtle.setheading(45)
    turtle.forward(35)
    
    # corncob pipe
    
    # line
    turtle.penup()
    turtle.color('#654321')
    turtle.goto(20, 115)
    turtle.pendown()
    turtle.setheading(-35)
    turtle.forward(60)
    
    # square part
    graphics.square(69, 81, 10, '#654321')
    
    turtle.penup()
    turtle.goto(72, 83)
    
    # each smoke thing
    heading = 45
    
    for i in range(1, 4):
        
        turtle.setheading(heading)
        turtle.pendown()
        turtle.pensize(2)
        turtle.color('dark gray')
        turtle.forward(25)
    
        graphics.circle_nofill(turtle.xcor(), turtle.ycor(), 3.5, 'dark gray')
    
        heading -= 5
        
    # last smoke thing
    turtle.setheading(heading)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('dark gray')
    turtle.forward(35)
    
    # eyes
    turtle.pensize(1)
    turtle.color('black')
    turtle.setheading(0)
    graphics.circle(-30, 150, 5, 'black')
    
    graphics.circle(20, 150, 5, 'black')
    
def drawHat():
    # drawHat accepts no arguments
    # draws the hat for the snowman
    # outputs two rectangular shapes, filled, to depict a hat
    
    # base of hat
    turtle.penup()
    turtle.fillcolor('dark grey')
    turtle.goto(-50, 200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(100)
    turtle.setheading(90)
    turtle.forward(20)
    turtle.setheading(-180)
    turtle.forward(100)
    turtle.setheading(-90)
    turtle.forward(20)
    turtle.end_fill()
    
    # top of hat
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.setheading(90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(50)
    turtle.setheading(0)
    turtle.forward(50)
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.end_fill()
    
# ---------------------------------------------------------------------

def checkerboard(): # Exercise 25
    # checkerboard accepts no arguments
    # creates a checkboard pattern using loops
    
    # constant width
    WIDTH = 100
    
    # coordinates
    x = -250
    y = -250
    
    # determines if square is black or white
    color = 1
    
    # for every row
    for i in range(1, 6):
        
        # for every square in the row
        for i in range(1, 6):
        
            # if color is an odd number, color the square black
            if (color % 2) > 0:
                graphics.square(x, y, WIDTH, 'black')
            
            # if color is an even number, color the square white
            else:
                graphics.square(x, y, WIDTH, 'white')
        
            # continues to the next column
            x += 100
            color += 1
       
        # continues to the next row
        y += 100
        x = -250