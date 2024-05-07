import turtle
import random
import math
import my_graphics

def message(): # 5-1
    # message() accepts no arguments
    # outputs one line I am Iron Man
    
    print('I am Iron Man.')
    
def main_5_2(): #5-2
    # main_5_2 accepts no arguments
    # outputs I am inevitable
    # calls procedure message()
    # outputs the message only one way to win
    
    print('I am inevitable.')
    message()
    print('Only one way to win...')
    
# ---------------------------------------------------------------------

def greeting():
    print('hello person')     
            
def acme_dryer():
    greeting()
    
    step_number = int(input('Enter the step number or 0 to exit: '))
    while step_number > 5:
        step_number = int(input('Enter a valid step number or 0 to exit: '))
        
    if step_number == 1:
        step1()
    if step_number == 2:
        step2()
    if step_number == 3:
        step3()
    if step_number == 4:
        step4()
    if step_number == 5:
        step5()
    if step_number == 0:
        goodbye()
    else:
        acme_dryer()
    print()
    
def step1():
    print('Step 1: Unplug the dryer and move it away from the wall.')
    
def step2():
    print('Step 2: Remove the six screws from the back of the dryer.')
    
def step3():
    print('Step 3: Remove the back panel.')
    
def step4():
    print('Pull the top of the dryer straight up.')
    
def step5():
    print('Pull the front of the dryer off.')
    
def goodbye():
    print('bye byeeeeeeee')
    
# ---------------------------------------------------------------------

def bad_scope():
    
    get_name()
    print('Hello', name)
    
def get_name():
    
    name = input('Enter your name: ')
    
# ---------------------------------------------------------------------

def bird_calculator():
    
    texas()
    kansas()
    
def texas():
    birds = 5000
    print('Texas has', birds, 'birds.')
    
def kansas():
    birds = 8000
    print('Kansas has', birds, 'birds.')
    
# ---------------------------------------------------------------------

def pass_arg():
    
    value = 5
    show_double(value)
    
def show_double(number):
    result = number * 2
    print(number, '* 2 =', result)
    
# ---------------------------------------------------------------------

def volume_conversion():
    intro()
    cups = int(input('Please enter the number of cups to convert to ounces: '))
    cups_to_ounces(cups)
    print()
    
def intro():
    print('Welcome to the cups to fluid ounces conversion program.')
    print('For your reference, 1 cup = 8 fluid ounces.')
    print()
    
def cups_to_ounces(cups):
    ounces = cups * 8
    print()
    print(cups, 'cups(s) is equal to', ounces, 'fluid ounces.')
    
# ---------------------------------------------------------------------

my_value = 10

def show_value():
    
    global my_value
    
    my_value += 1
    
    print('The value of the global variable my_value is', my_value)
    
# ---------------------------------------------------------------------

number = 0

def change_global():
    
    global number
    number = int(input('What do you want to change the global to? '))
    global_variables_are_bad()
    
def global_variables_are_bad():
    
    print('The value of the global variable number was changed in ', end='')
    print('change_global to the value of:', number)
    
# ---------------------------------------------------------------------

CONTRIBUTION_RATE = .05

def pay_me():
    gross = int(input('Please enter the amount for gross pay: '))
    bonus = int(input('Please enter the amount of bonuses: '))
    
    show_pay(gross)
    show_bonus(bonus)

def show_pay(gross):
    contribution_gross = gross * CONTRIBUTION_RATE
    print('Contribution for gross pay:', '$', contribution_gross)
    
def show_bonus(bonus):
    contribution_bonus = bonus * CONTRIBUTION_RATE
    print('Contribution for bonuses:', '$', contribution_bonus)
    
# ---------------------------------------------------------------------

def random_numbers():
    random_number = random.randint(1,10)
    print('The random number is:', random_number)

# ---------------------------------------------------------------------

def random_numbers2():
    
    for i in range(1, 6):
        number = random.randint(1,100)
        print(number)
        
# ---------------------------------------------------------------------

def random_numbers3():
    
    for count in range(5):
        print(random.randint(1,100))
        
# ---------------------------------------------------------------------

def dice():
    # dice accepts no arguments
    # loops until the user enters n or n to stop
    # each iteration prints two random 6-sided die rolls
    # it prompts the user to roll again (y/n)
    
    go = 'y'
    while go == 'y':
        
        print('Rolling your dice...')
        print('Your two rolls are:', random.randint(1,6), 'and', random.randint(1,6))
        
        go = input('Try your luck again? (y/n) ').lower()
        
# ---------------------------------------------------------------------

def coin_toss():
    HEADS = 1
    TAILS = 0
    TOSSES = 10
    
    for toss in range(TOSSES):
        number = random.randint(0,1)
        
        if number == HEADS:
            print('h e a d s')
            
        elif number == TAILS:
            print('taiLS')
            
# ---------------------------------------------------------------------

def sum_of_numbers():
    num1 = 5
    num2 = 7
    total = num1 + num2
    print(total)
    return total

# ---------------------------------------------------------------------

def total_ages():
    
    age1 = int(input('Please enter your age: '))
    age2 = int(input('Please enter the age of your best friend: '))
    
    total = calculate_ages(age1, age2)
    
    print('\nTogether you are', total, 'years old.')
    
def calculate_ages(age1, age2):
    
    total_ages = age1 + age2
    
    return total_ages

# ---------------------------------------------------------------------

DISCOUNT_PERCENT = .20

def sale_price():
    regular_price = get_regular_price()
    sale_price = regular_price - discount(regular_price)
    print('The sale price is', '$', sale_price)

def get_regular_price():
    price = float(input('Please enter the regular price of the item: '))
    return price

def discount(price):
    discount_price = (DISCOUNT_PERCENT * price)
    return discount_price

# ---------------------------------------------------------------------

def commission_rate():
    
    # calls get_sales and advanced_pay
    sales = get_sales()
    advanced = get_advanced_pay()
    
    # calls determine_comm_rate passing sales
    comm_rate = determine_comm_rate(sales)
    
    # calculates pay and outputs
    pay = ((sales * comm_rate) - advanced) + sales
    print('You need to pay (with commission)', pay)
    
    # determines if pay is negative, then outputs what the user must reinburse the company for
    if pay < 0:
        print('You need to reinburse the company', pay * -1)
    
def get_sales():
    
    # prompts user to input the total monthly sales
    sales = float(input('Please enter the total monthly sales: '))
    
    # returns monthly sales
    return sales

def get_advanced_pay():
    
    # prompts user to enter any advanced pay
    advanced_pay = int(input('Please enter any advanced pay, or 0 for none: '))
    
    # returns advanced_pay
    return advanced_pay

def determine_comm_rate(sales):
    
    # calculates commission rate for sales
    if sales >= 22000:
        comm_rate = .18
        
    elif sales >= 18000 and sales <= 21999:
        comm_rate = .16
        
    elif sales >= 15000 and sales <= 17999:
        comm_rate = .14
        
    elif sales >= 10000 and sales <= 14999:
        comm_rate = .12
        
    else:
        comm_rate = .10
        
    # returns calculated rate
    return comm_rate

# ---------------------------------------------------------------------

def get_name():
    
    first = input('Please enter your first name: ')
    last = input('Please enter your last name: ')
    
    return first, last

def validate_even(num):
    
    if (num % 2) == 0:
        return True
    else:
        return False
    
# ---------------------------------------------------------------------

def square_root():
    
    number = float(input('Please enter a value to find the square root: '))
    square = math.sqrt(number)
    print('The square root of', number, 'is', square)
    
# ---------------------------------------------------------------------

def hypotenuse():
    a = float(input('Enter the length of side A: '))
    b = float(input('Enter the length of side B: '))
    
    hypotenuse = math.hypot(a, b)
    
    print('The length of the hypotenuse is:',  hypotenuse)
    
# ---------------------------------------------------------------------

def graphic_fun():
    
    X1 = 0
    Y1 = 100
    X2 = -100
    Y2 = -100
    X3 = 100
    Y3 = -100
    RADIUS = 50
    
    my_graphics.square(-100, -100, 200, 'light gray')
    my_graphics.line(X2, Y2, X1, Y1, 'black')
    my_graphics.circle(X3, Y3, RADIUS, 'green')
    my_graphics.line(X3, Y3, X2, Y2, 'black')
    my_graphics.line(X1, Y1, X3, Y3, 'black')
    my_graphics.circle(X1, Y1, RADIUS, 'blue')
    my_graphics.circle(X2, Y2, RADIUS, 'red')