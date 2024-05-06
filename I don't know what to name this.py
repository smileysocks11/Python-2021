def comment_example():
    # comment example receives no arguments
    # it explains how to create a function header
    # and outputs or returns "Hello World!"
    print('Hello World!')
    
def program2_1():
    # apostrophe output
    print('Kate Austen')
    print('123 Full Cirlce Drive')
    print('Asheville, NC 28899')
    
def program2_2():
    # double quote output
    print("Kate Austen")
    print("123 Full Cirlce Drive")
    print("Asheville, NC 28899")
    
def program2_3():
    # display apostrophe
    print("Don't fear!")
    print("I'm here!")
    
def program2_4():
    # display quotes
    print('Your assignment is to read "Hamlet" by tomorrow.')
    
def program2_5():
    # This function displays a person's name and address
    print('Kate Austen')
    print('123 Full Cirlce Drive')
    print('Asheville, NC 28899')
    
def program2_6():
    print('Kate Austen') # Display the Name
    print('123 Full Cirlce Drive') # Display the address
    print('Asheville, NC 28899') # Display the city, state, and ZIP
    
def program2_7():
    room = 503
    print('I am staying in room number ' + str(room))
    
def program2_8():
    # assigning two variables and outputing strings
    top_speed = 160
    distance = 200
    
    print('The top speed is')
    print(top_speed)
    print('The distance traveled is')
    print(distance)
    
def program2_9():
    room = 503
    print('I am staying in room number', room)
    
def program2_10():
    # putting varible in string then reassigning it and printing again
    dollars = 2.75
    print('I have', dollars, 'in my account.')
    dollars = 99.95
    print('But now I have', dollars, 'in my account!')
    
def program2_11():
    # prints Kathryn Marino by using two variables
    first_name = 'Kathryn'
    last_name = 'Marino'
    print(first_name, last_name)
    
def program2_12():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Hello', first_name, last_name)
    
def program2_13():
    name = input('What is your name? ')
    age = input('What is your age? ')
    income = input('What is your income? ')
    
    print('Here is the data you entered:')
    print('Name:', name)
    print('Age:', age)
    print('Income:', float(income))
    
def program2_14():
    salary = 3600
    bonus = 100
    print('Your pay is', float(salary + bonus))
    
def sale_price():
    # get the original price of the item
    original_price = float(input('''Enter the item's original price: '''))
    
    # calcuate a 20 percent discount from the original_price
    discount = .20 * original_price
    
    # output the sale price
    sale_price = original_price - discount
    print('The sale price is', sale_price)
    
def get_average():
    # gets the average of three test scores
    
    # get the first test score
    first_score = int(input('Enter the first test score: '))
    
    # get the second test score
    second_score = int(input('Enter the second test score: '))
    
    # get the third test score
    third_score = int(input('Enter the third test score: '))
    
    # calcuate the average
    average = (first_score + second_score + third_score) / 3
    
    # output the average
    print('The average score is:', float(average))
    
def get_average2():
    print('The average score is:', (int(input('Enter the first test score:')) + int(input('Enter the second test score:')) + int(input('Enter the third test score:'))) / 3)
    
def program2_17():
    total_seconds = int(input('Enter the number of seconds: '))
    hours = float(total_seconds // 3600)
    minutes = float((total_seconds // 60) % 60)
    seconds = float(total_seconds % 60)
    print('Here is the time in hours, minutes, and seconds:')
    print('Hours:', hours)
    print('Minutes:', minutes)
    print('Seconds:', seconds)
    
def future_value():
    # get the desired future value
    future_value = int(input('Enter the desired future value: '))
    
    # get the annual interest rate
    interest_rate = float(input('Enter the annual interest rate: '))
    
    # get the number of years that the money will accrue interest
    years = int(input('Enter the number of years the money will grow: '))
    
    # calcuate the amount that will need to be deposited
    deposit = (future_value / (1 + interest_rate) ** years)
    
    # output the amount that will need to be deposited
    print('You will need to deposit', float(deposit))
    
def program2_19():
    # calcuates monthly payment after 12 months
    amount_due = 5000.0
    monthly_payment = amount_due / 12.0
    
    print('Your monthly payment is', monthly_payment)
    
def program2_20():
    # calcuates monthly payment after 12 months with formatting 
    amount_due = 5000.0
    monthly_payment = amount_due / 12.0
    
    # prints monthly payment with two decimal points and as a float
    print('Your monthly payment is', format(monthly_payment, '.2f'))
    
def program2_21():
    monthly_pay = 5000.0
    annual_pay = monthly_pay * 12.0
    
    print('Your annual pay is $', format(annual_pay, ',.2f'),
          sep='')

def future_value2():
    # get the desired future value
    future_value = int(input('Enter the desired future value: '))
    
    # get the annual interest rate
    interest_rate = float(input('Enter the annual interest rate: '))
    
    # get the number of years that the money will accrue interest
    years = int(input('Enter the number of years the money will grow: '))
    
    # calcuate the amount that will need to be deposited
    deposit = (future_value / (1 + interest_rate) ** years)
    
    # output the amount that will need to be deposited
    print('You will need to deposit $', format(float(deposit), '.2f'),
        sep='')
    
def program2_22():
    num1 = 127.90
    num2 = 3465.15
    num3 = 3.78
    num4 = 264.82
    num5 = 88.08
    num6 = 800.00
    
    print(format(num1, '7.2f'))
    print(format(num2, '7.2f'))
    print(format(num3, '7.2f'))
    print(format(num4, '7.2f'))
    print(format(num5, '7.2f'))
    print(format(num6, '7.2f'))

# import turtle
#turtle.clear()
#for i in range(1,10):
 #   turtle.shape('turtle')
  #  turtle.color('yellow')
   # turtle.bgcolor('black')
    #turtle.write('turtle')
    # turtle.forward(50)
    turtle.circle(90)

import turtle
def orion():
    
    # setup le turtle
    turtle.setup(500,600)
    turtle.penup()
    turtle.hideturtle()
    
    # use constants for each star
    LEFT_SHOULDER_X = -70
    LEFT_SHOULDER_Y = 200
    
    RIGHT_SHOULDER_X = 80
    RIGHT_SHOULDER_Y = 180
    
    LEFT_BELTSTAR_X = -40
    LEFT_BELTSTAR_Y = -20
    
    MIDDLE_BELTSTAR_X = 0
    MIDDLE_BELTSTAR_Y = 0
    
    RIGHT_BELTSTAR_X = 40
    RIGHT_BELTSTAR_Y = 20
    
    LEFT_KNEE_X = -90
    LEFT_KNEE_Y = -180
    
    RIGHT_KNEE_X = 120
    RIGHT_KNEE_Y = -140
    
    turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
    turtle.pendown()
    turtle.dot()
    turtle.write('Betelgeuse')
    
    turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
    turtle.dot()
    turtle.write('Alnitak')
    
    turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
    turtle.dot()
    turtle.write('Alnilam')
    
    turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
    turtle.dot()
    turtle.write('Mintaka')
    
    turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
    turtle.dot()
    turtle.write('Meissa')
    
    turtle.penup()
    turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
    turtle.pendown()
    turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
    turtle.dot()
    turtle.write('Rigel')
    
    
    turtle.penup()
    turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
    turtle.pendown()
    turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
    turtle.dot()
    turtle.write('Saiph')