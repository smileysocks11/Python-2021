def day_converter(): # Exercise 1
    # day_converter accepts no arguments
    # asks user for a number in range 1 - 7
    # displays corresponding day of the week in Spanish
    # shows an error message if the user enters any value outside of 1 - 7
    
    # asks user for a day of the week number
    number = int(input('Enter a number in the range 1 through 7 from Monday to Sunday: '))
    
    # list of days of the week in spanis
    days = ['filler', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    
    # prints the day of the week in spanish that corresponds with the number the user provided
    if number in range(1, 8):
        print(days[number])

    # displays error message if outside range
    else: print('Your number is not inside the range of 1 through 7.')
    
    
def roman_numerals(): # Exercise 4
    # roman_numerals accepts no arguments
    # asks user to enter a number from 1 through 10
    # displays the Roman numeral version of that number
    # if the number is outside the range 1 through 10, procedure should display error message
    
    # asks user for number
    number = int(input('Enter a number from 1 through 10: '))
    
    # list of roman numerals
    roman_numerals = ['filler', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    
    # prints roman numeral that corresponds with number user provided
    if number in range(1, 11):
        print(roman_numerals[number])
        
    # displays error message if number outside range
    else:
        print('The number you provided is outside of the range 1 through 10.')
        

def color_mixer(): # Exercise 7
    # color_mixer accepts no arguments
    # prompts user for two primary colours to mix
    # if user choices colour other than red, blue, yellow, displays error message
    # otherwise it displays name of secondary color that results
    
    # asks user
    colour1 = (input('Enter the first primary colour to mix: '))
    colour2 = (input('Enter the second primary colour to mix: '))
    
    # lower capitalization
    colour1.lower()
    colour2.lower()
    
    # checks is colour is primary
    if colour1 == 'red' or colour1 == 'blue' or colour1 == 'yellow' and colour2 == 'red' or colour2 == 'blue' or colour2 =='yellow':
        if colour1 == colour2:
            print('You need to enter two different primary colours.')
            exit()
            
        # finds out the secondary colour
        elif (colour1 == 'red' or colour1 == 'blue') and (colour2 == 'red' or colour2 == 'blue'):
            print('puRPLE')
                
        elif (colour1 == 'red' or colour1 == 'yellow') and (colour2 == 'red' or colour2 == 'yellow'):
            print('orAnGE')
                
        elif (colour1 == 'blue' or colour1 == 'yellow') and (colour2 == 'blue' or colour2 == 'yellow'):
            print('GreEN')
          
    # primary colours
    primary_colours = ['red', 'yellow', 'blue']
    
    # error message
    errors1 = 0
    errors2 = 0
    
    for i in primary_colours:
        if colour1 != i:
            errors1 = errors1 + 1
        if colour2 != i:
            errors2 = errors2 + 1

    if errors1 == 3 or errors2 == 3:
        print('One or more of your colours are not primary.')
        
    
def hot_dog(): # Exercise 8
    # hot_dog accepts no arguments
    # calcuates the min amount of packages of each item needed for cookout
    # prompts user for number of people attending and number of hotdogs each person can get
    
    # asks the user
    people = int(input('How many people are attending? '))
    per_person = int(input('How many hot dogs can each person get? '))
    
    # calcuations
    minimum_hotdogs = int((people * per_person) / 10)
    minimum_buns = int((people * per_person) / 8)
    
    if isinstance(minimum_buns, float):
        minimum_buns + 1
        
    leftover_hotdogs = (people * per_person) % 10
    leftover_buns = (people * per_person) % 8
  
    # prints the details
    print(minimum_hotdogs, 'packages of hotdogs are required.')
    print(minimum_buns, 'packets of hotdog buns are required.')
    print('There are', leftover_hotdogs, 'left over.')
    print('There are', leftover_buns, 'left over.')
    
    
def time_calcuator(): # Exercise 15
    # time_calcuator accepts no arguments
    # asks user to enter a number of seconds
    # converts seconds to minutes, hours, and days
    
    # asks user
    user_seconds = int(input('Enter a number of seconds: '))
    
    # conversions
    if user_seconds >= 86400:
        days = user_seconds // 86400
        leftover_seconds1 = user_seconds - (days * 86400)
        
        hours = leftover_seconds1 // 3600
        leftover_seconds2 = leftover_seconds1 - (hours * 3600)
        
        minutes = leftover_seconds2 // 60
        leftover_seconds3 = leftover_seconds2 - (minutes * 60)
        
        seconds = int(leftover_seconds3)
        
        print(user_seconds, 'seconds is equal to', days, 'day(s)', hours, 'hour(s)', minutes, 'minute(s), and', seconds, 'second(s).')
        
    elif user_seconds >= 3600:
        
        hours = user_seconds // 3600
        leftover_seconds1 = user_seconds - (hours * 3600)
        
        minutes = leftover_seconds1 // 60
        leftover_seconds2 = leftover_seconds1 - (minutes * 60)
        
        seconds = int(leftover_seconds2)
        print(user_seconds, 'seconds is equal to', hours, 'hour(s)', minutes, 'minute(s), and', seconds, 'second(s).')
        
    elif user_seconds >= 60:
        minutes = user_seconds // 60
        seconds = int(user_seconds % 60)
        print(user_seconds, 'seconds is equal to', minutes, 'minute(s) and', seconds, 'second(s).')
    
def leap_year(): # Exercise 16
    # leap_year accepts no arguments
    # calcuates if the year is a leap year
    # displays number of days in the month of February for that year
    
    # asks user
    year = int(input('Please enter a year: '))
    
    # figures out if it's a leap year
    if ((year % 100) == 0 and (year % 400) == 0):
        print(year, 'is a leap year. There are 29 days in the month of February.')
        
    elif year % 100 != 0 and year % 4 == 0:
        print(year, 'is a leap year. There are 29 days in the month of February.')
        
    else:
        print(year, 'is not a leap year. There are 28 days in the month of February.')
            
            
def sir_fix_alot(): # Exercise 17
    # sir_fix_alot accepts no arguments
    # troubleshoots a bad wifi connection
    # outputs the solution to the user's problem
    
    print('Reboot computer and try to connect.')
    if input('Did that fix the problem? ').lower() == 'no':
        print('Rebot router and try to connect.')
        
        if input('Did that fix the problem? ').lower() == 'no':
            print('Verify cables are firmly attached.')
            
            if input('Did that fix the problem? ').lower() == 'no':
                print('Move router to better location.')
                
                if input('Did that fix the problem? ').lower() == 'no':
                    print('Get a new router, fool.')
                    
                else:
                    print('Netflix and Chill.')
            else:
                print('Netflix and Chill.')
        else:
            print('Netflix and Chill.')
    else:
        print('Netflix and Chill')
        

def can_we_just_eat(): # Exercise 18
    # can_we_just_eat accepts no arguments
    # asks whether any members of your party are vegetarian, vegan, or gluten-free
    # only displays the restaurants your group may eat
    
    # asks user
    vegetarian = input('Is anyone in your party a vegetarian? ').lower()
    vegan = input('Is anyone in your party a vegan? ').lower()
    gluten = input('Does anyone in your party have celiac disease? ').lower()
    
    # finds restaruants
    print('')
    print('Here are your restaurant choices:')
    
    if vegetarian == 'no' and vegan == 'no' and gluten == 'no':
        print('''Joe's Gourmet Burgers''')
        print('Main Street Pizza Company')
        print('''Mama's Fine Italian''')
        print('''The Chef's Kitchen''')
        print('Corner Cafe')
    
    if vegetarian == 'no' and vegan == 'no' and gluten == 'yes':
        print('Main Street Pizza Company')
        print('''The Chef's Kitchen''')
        print('Corner Cafe')
        
    if vegetarian == 'no' and vegan == 'yes' and gluten == 'yes':
        print('Main Street Pizza Company')
        print('''The Chef's Kitchen''')
        print('Corner Cafe')
        
    if vegetarian == 'no' and vegan == 'yes' and gluten == 'no':
        print('''The Chef's Kitchen''')
        print('Corner Cafe')
        
    if vegetarian == 'yes' and vegan == 'no' and gluten == 'yes':
        print('Main Street Pizza Company')
        print('''The Chef's Kitchen''')
        print('Corner Cafe')
        
    if vegetarian == 'yes' and vegan == 'no' and gluten == 'no':
        print('''Mama's Fine Italian''')
        print('''The Chef's Kitchen''')
        print('Corner Cafe')
        
    if vegetarian == 'yes' and vegan == 'yes' and gluten == 'yes':
        print('''The Chef's Kitchen''')
        print('Corner Cafe')
        
    if vegetarian == 'yes' and vegan == 'yes' and gluten == 'no':
        print('Corner Cafe')
        print('''Chef's Kitchen''')
        
        
def hit_the_target(): # Exercise 19
    
    # hit_the_target accepts no arguments
    # asks user for the projectile's force and angle
    # shoots projectile and checks if it hit the target
    
    import turtle
    
    # named constants
    
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    TARGET_LEFT_X = 100
    TARGET_LEFT_Y = 250
    TARGET_WIDTH = 25
    FORCE_FACTOR = 30
    PROJECTILE_SPEED = 1
    NORTH = 90
    SOUTH = 270
    EAST = 0
    WEST = 180
    
    # set up the turtle window\
    turtle.clear()
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.speed(PROJECTILE_SPEED)
    turtle.shape('turtle')
    
    # draw the target
    
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(TARGET_LEFT_X, TARGET_LEFT_Y)
    turtle.pendown()
    turtle.setheading(EAST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(NORTH)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(WEST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(SOUTH)
    turtle.forward(TARGET_WIDTH)
    turtle.penup()
    
    # ask the user
    
    projectile_angle = float(input('''Enter the projectile's angle: '''))
    launch_force = float(input('Enter the launch force (1-10): '))
    
    
    # launch time
    
    turtle.goto(0,0)
    turtle.setheading(projectile_angle)
    turtle.pendown()
    turtle.forward(FORCE_FACTOR * launch_force)
    
    # figure out if it hit the target
    
    x = round(turtle.xcor(), 0)
    y = round(turtle.ycor(), 0)
    
    if x in range(TARGET_LEFT_X, TARGET_LEFT_X + 26) and y in range(TARGET_LEFT_Y, (TARGET_LEFT_Y + 26)):
        print('Target hit!')
    
    # figures out if the user needs to enter a different angle or power
    else:
        print('Here are some hints:')
        
        if y < TARGET_LEFT_Y:
            print('- Try using more power')
            
        if y > TARGET_LEFT_Y + 25:
            print('- Try using less power')
            
        if x < TARGET_LEFT_X:
            print('- Try using a smaller angle')
            
        if x > TARGET_LEFT_X + 25:
            print('- Try using a greater angle')
            