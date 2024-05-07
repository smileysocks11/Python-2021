def commission():
    
    keep_going = 'y'
    
    while keep_going == 'y':
        
        sale_amount = float(input('Enter the sale amount: '))
        commission_rate = float(input('Enter the commission rate: '))
        commission1 = format(sale_amount * commission_rate, '.2f')
        
        print('The commission is', '$', commission1)
        
        keep_going = input('Do you want to calculate another? (y/n) ')
        

def temperature():
    
    MAX_TEMP = 102.5
    
    sub_temp = int(input('Please enter the current substance temperature in degrees Celcius: '))
    
    while sub_temp > MAX_TEMP:
        
        print('')
        print('The temperature is too high.')
        print('Turn the thermostat down and wait for it to cool.')
        print('Then wait 5 minutes and measure again.')
        print('')
        sub_temp = int(input('Please enter the current substance temperature in degrees Celcius: '))
        
    print('The temperature is acceptable.')
    print('Measure it again in 15 minutes.')
    
    
def infinite():
    
    keep_going = 'y'
    
    while keep_going == 'y':
        
        sale_amount = float(input('Enter the sale amount: '))
        commission_rate = float(input('Enter the commission rate: '))
        commission2 = format(sale_amount * commission_rate, '.2f')
        
        print('The commission is', '$', commission2)
        
        # keep_going = input('Do you want to calculate another? (y/n) ')
        
        
def simple_loop1():
    
    print('I will display the numbers 1 - 5')
    
    for number in range(1, 11):
        print(number)
        
        
def simple_loop2():
    
    print('I will display all odd numbers from 1- 10')
    
    for number in range(1, 10):
        divide = isinstance((number / 2), int)
        print(divide)
        if divide:
            print(number)
            
            
def simple_loop3():
    
    mcu = ['Steve', 'Tony', 'Thor', 'Wanda']
    
    for character in mcu:
        print(character)
        
        
def while_example2():
    
    counter = 0
    
    while counter < 5:
        print('Hello World!')
        counter += 1
        
        
def squares():
    
    print('Number\t', 'Square')
    print('---------------')
    
    for i in range(1, 11):
        print(i, '\t', i*i)
        
        
def speed_converter():
    
    print('KPH\tMPH')
    print('--------------')
    
    for i in range(60, 131, 10):
        print(i, '\t', i * .6241)
        
        
def user_squares1():
    
    print('This program will display a list of numbers (starting at 1) and their squares.')
    amount_squares = int(input('How many squares? '))
    print('')
    print('Number\tSquares')
    print('--------------')
    
    for square in range(1, amount_squares + 1):
        print(square, '\t', square * square)
        
        
def user_squares2():
    
    print('This program will display a list of numbers and their squares.')
    starting_number = int(input('Enter the starting number: '))
    ending_number = int(input('Enter the ending number: '))
    print('')
    print('Number\tSquares')
    print('--------------')
    
    for square in range(starting_number, ending_number + 1):
        print(square, '\t', square * square)
        
        
def sum_numbers():
    
    print('This program calculates the sum of 5 numbers you will enter.')
    number_total = 0
    
    for i in range(1, 6):
        number = int(input('Please enter a number: '))
        number_total += number
        
    print('The total of your 5 numbers is:', format(number_total, '.2f'))
    
    
def property_tax():
    
    lot_number = 1
    PROP_TAX = .0065
    
    lot_number = int(input('Please enter a lot number (enter 0 to end): '))

    while lot_number != 0:
        
        property_value = int(input('Please enter the property value: '))
        
        property_tax = property_value * PROP_TAX
        print('Property tax: ', '$', property_tax)
        lot_number = int(input('Please enter a lot number (enter 0 to end): '))

    print('')
    print('Thank you for using the Cyberdyne Systems property tax calculator, all your rights reserved.')
    
    
def gross_pay():
    
    hours = int(input('Enter the number of hours worked for 1 week: '))
    
    while hours > 168:
        hours = int(input('Error. Enter a valid number of hours worked for 1 week: '))
        
    pay_rate = int(input('Enter the hourly rate: '))
    
    gross_pay = hours * pay_rate
    
    print('Gross pay: $', format(gross_pay, ',.2f'), sep='')
    
    
def retail_no_validation():
    
    MARK_UP = 1.25
    another = 'y'
    
    while another == 'y' or another == 'Y':
        wholesale = float(input('Enter the wholesale cost: '))
        
        while wholesale == 0:
            wholesale = float(input('Error. Enter a valid wholesale cost: '))
            
        retail = wholesale * MARK_UP
        
        print('Retail price: $', format(retail, ',.2f'), sep='')
        
        another = input('Do you want to enter another item?' +
                        ' (Enter y for yes): ')
        
        
def test_score_averages():
    
    # asks user for input
    students = int(input('How many students? '))
    tests = int(input('How many tests per student? '))
    
    # for every student
    for student in range(1, students + 1):
        print('Student number', student)
        print('--------------------')
        
        # for every test
        for test in range(1, tests + 1):
            average = 0
            print('Test number', test, end='')
            average += float(input(': '))
            
        # calcuates average
        average = average / 3
        print('The average for student number 1 is:', average)
            
            
def rectangle_pattern():
    
    rows = int(input('Enter the number of rows to print: '))
    columns = int(input('Enter the number of columns to print: '))
    
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            print('*', end='')
        print()
        
        
def triangle_pattern():
    
    base = int(input('Enter the base size of the triangle: '))
    number = (base - base) + 1
     
    for base in range(1, base + 1):
        for star in range(1, number + 1):
            print('*', end='')
        number = number + 1
        print()
        
        
def stair_pattern():
    
    stairs = int(input('Enter the number of stairs: '))
    
    space = 1
    
    for i in range(1, space + 1):
        print(' ', end='')
        space = space + 1
        
        for stair in range(1, stairs + 1):
            print('✰', end='')
        
        print()
        
        
def spiral_circles():
    
    import turtle
    
    NUM_CIRCLES = 36
    RADIUS = 100
    ANGLE = 10
    
    for x in range(NUM_CIRCLES):
        turtle.circle(RADIUS)
        turtle.left(ANGLE)
        
def starburst():
    
    import turtle
    
    START_X = -200
    START_Y = 0
    NUM_LINES = 36
    LINE_LENGTH = 400
    ANGLE = 170
    ANIMATION_SPEED = 0
    
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(START_X, START_Y)
    turtle.pendown()
    
    turtle.speed(ANIMATION_SPEED)
    
    for x in range(NUM_LINES):
        turtle.forward(LINE_LENGTH)
        turtle.left(ANGLE)
        