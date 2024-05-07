def personal_info(): # Exercise 1
    # personal_info accepts no arguments
    # displays my name, address, phone number, and projected college major
    
    # displays my name
    print('Sophie')
    
    # displays my address (city, state, ZIP)
    print('326 South Limuel Court, Wichita, KS, 67235')
    
    # displays my telephone number
    print('326-282-5731')
    
    # displays my projected college major
    print('Computer Science')
    
def total_purchase(): # Exercise 4
    # total_purchase accepts no arguments
    # prompts the user for the the price of each item, calcuates the subtotal of the sale, the amount of the sales tax,
    # and the total.
    # then displays the subtotal, the sales tax, and the total in an even format
    
    # prompts the user for the price of each item and stores them in corresponding variables
    first_item = float(input('Please enter a price for your first item: '))
    second_item = float(input('Please enter a price for your second item: '))
    third_item = float(input('Please enter a price for your third item: '))
    fourth_item = float(input('Please enter a price for your fourth item: '))
    fifth_item = float(input('Please enter a price for your fifth item: '))
    
    # calcuates the subtotal, or the sum of all the items and displays it
    subtotal = first_item + second_item + third_item + fourth_item + fifth_item
    print('Subtotal:\t', '$', format(subtotal,'5.2f'))
    
    # calcuates the sales tax by multiplying the subtotal times .07
    sales_tax = subtotal * .07
    print('Tax:\t\t', '$', format(sales_tax,'5.2f'))
    
    # calcuates the total by finding the sum of the subtotal and the sales_tax
    total = subtotal + sales_tax
    print('Total:\t\t', '$', format(total,'5.2f'))

def distance_traveled(): # Exercise 5
    # distance_traveled accepts no arguments
    # prompts the user for miles per hour
    # calcuates the the distance the car will travel in various hours
    # displays the distance the car will travel in 6, 10, and 15 hours
    
    # prompts the user for mph
    mph = int(input('How fast are you driving? '))
    
    # calcuations for distance
    six_hours = mph * 6
    ten_hours = mph * 10
    fifteen_hours = mph * 15
    
    # displays the calcuated distances to the user
    print('At 60 miles per hour you will travel', six_hours, 'in 6 hours.')
    print('At 60 miles per hour you will travel', ten_hours, 'in 10 hours.')
    print('At 60 miles per hour you will travel', fifteen_hours, 'in 15 hours.')
    
def sales_tax(): # Exercise 6
    # sales_tax accepts no arguments
    # asks the user to enter the amount of purchase
    # computes the state and county sales tax
    # displays the amount of the purchase, the state sales tax, the county sales tax, the total sales tax, and the total sales
    
    # asks the user to enter the sale amount
    sale_amount = float(input('Enter the sale amount: '))
    
    # calcuations
    state_tax = .05 * sale_amount
    county_tax = .025 * sale_amount
    total_tax = state_tax + county_tax
    total_sale = total_tax + sale_amount
    
    # displays the sale and tax amounts
    print('Your purchase price was:\t', '$\t', format(total_sale,'5.2f'))
    print('Your state tax amount is:\t', '$\t', format(state_tax, '5.2f'))
    print('Your county tax amount is:\t', '$\t', format(county_tax, '5.2f'))
    print('Your total tax is:\t\t', '$\t', format(total_tax, '5.2f'))
    print('Your total sale is:\t\t', '$\t', format(total_sale, '5.2f'))
    
def tip_tax_total(): # Exercise 8
    # tip_tax_total accepts no arguments
    # calcuates the total amount of a meal purchased at a restaurant
    # asks user to enter the charge for the food
    # calcuates the amounts of a 18 percent tip and 7 percent sales tax
    # displays each of these amounts and the total
    
    # prompts the user to enter the sale amount
    sale_amount = int(input('Please enter the sale amount: '))
    
    # calcuations
    tip_amount = .018 * sale_amount
    sales_tax = .07 * sale_amount
    total_bill = tip_amount + sales_tax
    
    # displays the sale, tip, tax, and total amounts
    print('The sale was:\t\t\t', '$', format(sale_amount,'5.2f'))
    print('THe tip amount is:\t\t', '$', format(tip_amount,'5.2f'))
    print('The sales tax amount is:\t', '$', format(sales_tax,'5.2f'))
    print('Your total bill was:\t\t', '$', format(total_bill,'5.2f'))
    
def temp_converter(): # Example 9
    # temp_converter accepts no arguments
    # converts Celsius temperatures to Fahrenheit temperatures
    # asks user to enter a temperature in degrees Celsius
    # displays the temperature converted to Fahrenheit
    
    # prompts the user to enter temp in celsius
    celsius = int(input('Please enter the degrees Celsius: '))
    
    # calcuations
    fahrenheit = 1.8 * celsius + 32
    
    # displays the temp in fahrenheit
    print(celsius, 'degrees celsius is', fahrenheit, 'degrees fahrenheit.')
    
def cookie_monster(): # Example 10
    # cookie_monster accepts no arguments
    # asks user how many cookies they want to bake
    # displays number of cups and ounces of each ingredient needed for the specified number of cookies
    
    # prompts user for number of cookies
    cookies = int(input('How many cookies do you want to make? '))
    
    # calcuations for ounces
    sugar_oz = .5 * float(cookies)
    butter_oz = ((1 / 3) * float(cookies))
    flour_oz = .9167 * float(cookies)
    
    # calcuations for cups
    sugar_cups = int(sugar_oz / 8)
    sugar_remainder = int(sugar_oz % 8)
    
    butter_cups = int(butter_oz / 8)
    butter_remainder = int(butter_oz % 8)
    
    flour_cups = int(flour_oz / 8)
    flour_remainder = int(flour_oz % 8)
    
    # displays recipe
    print('For', cookies, 'cookies you will need:')
    print(sugar_cups, 'cups(s)', sugar_remainder, 'ounces of sugar.')
    print(butter_cups, 'cups(s)', butter_remainder, 'ounces of butter.')
    print(flour_cups, 'cups(s)', flour_remainder, 'ounces of flour.')
    
def class_demographics(): # Exercise 11
    # class_demographics accepts no arguments
    # asks user for the number of females and the number of males registered for a class
    # displays the percentage of females and males enrolled
    
    # asks user for # of females and males
    females = int(input('Enter the number of females: '))
    males = int(input('Enter the number of males: '))
    
    # calcuations
    total = females + males
    female_percentage = (females / total) * 100
    male_percentage = (males / total) * 100
    
    # displays percentage of females and males
    print('The class consists of ', int(round(female_percentage, 0)), '% females and ', int(round(male_percentage, 0)), '% males.', sep = '')
    
def tortuga_1(): # Exercise 15
    # tortuga_1 accepts no arguments
    # uses turtle to create ring colors from left to right: light blue, yellow, black, green, red
    
    import turtle
    
    
    
    # yellow circle
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    turtle.color('yellow')
    turtle.width(10)
    turtle.circle(90)
    
    # green circle
    turtle.penup()
    turtle.goto(100, -50)
    turtle.pendown()
    turtle.color('light green')
    turtle.width(10)
    turtle.circle(90)
    
    # light blue
    turtle.penup()
    turtle.goto(-200, 50)
    turtle.pendown()
    turtle.color('light blue')
    turtle.width(10)
    turtle.circle(90)
    
    # black circle
    turtle.penup()
    turtle.goto(0, 50)
    turtle.pendown()
    turtle.color('black')
    turtle.width(10)
    turtle.circle(90)
    
    # red circle
    turtle.penup()
    turtle.goto(200, 50)
    turtle.pendown()
    turtle.color('red')
    turtle.width(10)
    turtle.circle(90)
    
def tortuga_2(): # Exercise 15
    # tortuga_2 accepts no arguments
    # creates a simple 3d house
    
    import turtle
    
    # north south
    turtle.width(3)
    turtle.forward(150)
    turtle.backward(300)
    
    # west east
    turtle.goto(0,0)
    turtle.setheading(90)
    turtle.forward(150)
    turtle.backward(300)
    
    # north east and south east
    turtle.goto(0,0)
    turtle.width(1)
    turtle.setheading(45)
    turtle.forward(100)
    turtle.backward(200)
    
    # north west and south west
    turtle.goto(0,0)
    turtle.setheading(-45)
    turtle.forward(100)
    turtle.backward(200)
    
    # writing the N
    turtle.penup()
    turtle.goto(-7, 175)
    turtle.width(5)
    turtle.write('N', font=('Arial', 20,"normal"))
    
    # writing the S
    turtle.goto(-7, -200)
    turtle.write('S', font=('Arial', 20, 'normal'))
    
    # writing the W
    turtle.goto(-200, -15)
    turtle.write('W', font=('Arial', 20, 'normal'))
    
    # writing the E
    turtle.goto(175, -15)
    turtle.write('E', font=('Arial', 20, 'normal'))