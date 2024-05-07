def bug_collector(): # Exercise 1
    # bug_collector accepts no arguments
    # keeps a running total of bugs collected over 5 days
    # displays total number of bugs collected
    
    # total bugs variable
    total_bugs = 0
    bug = 0
    
    # welcomes the user to the system
    print('Welcome to the Bug Masters bug collection system.')
    print()
    
    # collects input from the user
    for day in range(1, 6):
       
        print('How many bugs did you collect on day ', day, '?', sep='', end='')
        bug = int(input(': '))
        
        # validation
        while bug < 0:
            print('Error. Please enter a valid amount of bugs collected on day ', day, '?', sep='', end='')
            bug = int(input(': '))
        
        # adds number of bugs to total
        total_bugs += bug
        
    # outputs the total number of bugs collected
    print()
    print('Great job, you collected', total_bugs, '''bugs this week. You're the bug master!''')
    
    
def distance_traveled(): # Exercise 4
    # distance_traveled accepts no arguments
    # prompts user for the speed in mph and how many hours of travel
    # then loops through the hours, displaying the distance traveled for each hour
    
    # gets input from user
    mph = int(input('Enter the speed of the vehicle in mph: '))
    
    # validation
    while mph < 0:
        
        mph = int(input('Error. Please enter a valid speed of the vehicle in mph: '))
        
    hours = int(input('Enter how many hours the vehicle traveled: '))
    
    # validation
    while hours < 0:
        hours = int(input('Error. Please enter a valid number of hours the vehicle traveled: '))
    
    
    # outputs
    print()
    print('Hour\t\tDistance Traveled')
    print('___________________________________')
    
    for hour in range(1, hours + 1):
        distance = mph * hour
        print(hour, '\t\t\t', distance)
        
        
def pennies(): # Exercise 7
    # pennies accepts no arguments
    # gets input from user for number of days
    # calcuates how much money they have by the end of the days
    # outputs table with the salary for each day
    
    # gets number of days input from user
    days = int(input('How many days do you want to accure pennies? '))
    
    # validation
    while days < 0:
        days = int(input('Error. Please enter a valid amount of days you want to accure pennies for: '))
        
    # outputs table with the salary for each day
    print()
    print('Day\t\tSalary')
    print('-----------------------------------')
    
    total = .005
    for day in range(1, days + 1):
        salary = total * 2
        print(day, '\t\t\t', '$', format(salary, '.2f'))
        total = salary
        
        
def hogwarts_tuition(): # Exercise 10
    # hogwarts_tuition accepts no arguments
    # loops and displays the projected semester tutition amount for the next five years
        
    # outputs table with the tuition cost per each year
    print()
    print('Year\t\tTuition Cost')
    print('-----------------------------------')
    
    total = 16000
    tuition = 16000
    for year in range(1, 6):
        tuition += total * .03
        print(year, '\t\t\t', '$', format(tuition, '.2f'))
        total = tuition
        
        
def population(): # Exercise 13
    # population accepts no arguments
    # inputs a starting number of organisms, the average daily increase %, and the number of days to simulate
    # simulates population growth
    
    # starting pop input from user
    starting = int(input('Enter the starting population: '))
    # validation
    while starting < 0:
        starting = int(input('Error. Please enter a valid starting population: '))
    
    # daily growth input from user
    daily_growth = int(input('Enter the percent of daily growth: '))
    # validation
    while daily_growth < 0:
        daily_growth = int(input('Error. Please enter a valid percent of daily growth: '))
        
    # days to simulate input from user
    days = int(input('Enter the number of days to simulate: '))
    # validation
    while days < 0:
        days = int(input('Error. Please enter a valid number of days to simulate: '))
    
    
    # outputs table with the projected population for each day
    print()
    print('Day\t\tProjected Population')
    print('-----------------------------------')
    
    total = starting
    projected = starting
    for day in range(1, days + 1):
        if day == 1:
            print(day, '\t\t\t', (starting))
         
        else:
            projected += total * (daily_growth / 100)
            print(day, '\t\t\t', projected)
            total = projected
            
            
def reverse_triangle(): # Exercise 14
    # reverse_triangle accepts no arguments
    # outputs triangle pattern
    
    # gets input from user
    base = int(input('Enter the base size of the triangle: '))
    
    number = base
     
    # loop to create triangle
    for base in range(1, base + 1):
        for star in range(1, number + 1):
            print('*', end='')
        number = number - 1
        print()
        
        
def stair_pattern2(): # Exercise 15
    # stair_pattern2 accepts no arguments
    
    # gets input from user
    num_steps = int(input('Enter the number of stairs: '))
    print()
    
    spaces = 0
    # loop for each stair in steps, add spaces, then symbol
    for stairs in range(num_steps):
        print('✰', end='')
        # adds certain number of spaces
        for space in range(spaces):
            print(' ', end='')
        print('✰')
        # increases number of spaces for next time
        spaces += 1
        
        
        
def repeating_squares(): # Exercise 16
    # repeating_squares accepts no arguments
    # asks user for number of squares to draw
    # makes a weird pattern square thing
    
    import turtle
    
    # prompts user
    squares = int(input('Enter a number of squares to draw: '))
    
    # validation
    while squares < 0:
        squares = int(input('Error. Plesae enter a valid number of squares to draw: '))
    # puts turtle in bottom right corner
    turtle.penup()
    turtle.goto(200, -200)
    turtle.pendown()
    
    # creates square thing
    width = 10
    turtle.speed(5)
    for square in range(squares):
        # draw square
        turtle.setheading(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(width)
        turtle.setheading(-180)
        
        # increase square width
        width += 5
        
        
def hypnotic_pattern(): # Exercise 18
    # hypnotic_pattern accepts no arguments
    # asks user for number of patterns to draw
    # makes a weird hypnotic pattern square thing
    
    import turtle
    
    # prompts user
    patterns = int(input('Enter a number of patterns to draw: '))
    
    # validation
    while patterns < 0:
        patterns = int(input('Error. Plesae enter a valid number of patterns to draw: '))
        
    width = 5
    turtle.setheading(90)
    
    # creates pattern
    for pattern in range(patterns):
        for i in range(1, 5):
            turtle.forward(width)
            turtle.left(90)
            width += 5