def test_average():
    
    first_score = int(input('Enter the first score: '))
    second_score = int(input('Enter the second score: '))
    third_score = int(input('Enter the third score: ' ))
    
    average = (first_score + second_score + third_score) / 3
    
    print('The average score is:', format(average, '.2f'))
    
    if average > 95:
        print('Congratulations!')
        print('That is a high score!')
        
def auto_repair_payroll():
    
    hours_worked = int(input('Enter the number of hours worked: '))
    hourly_pay_rate = int(input('Enter the hourly pay rate: '))
    gross_pay = hours_worked * hourly_pay_rate
        
    if (hours_worked - 40) > 0:
        overtime = hours_worked - 40
        gross_pay = gross_pay * 1.5 * overtime
            
    print('Your gross pay is:', '$', gross_pay)

def password_verifier():
    # password_verifer accepts no arguments
    # get the password to check
    # if password = 'prospero':
    # output to user, 'password accepted.'
    # else output 'password invalid'
    
    password = input('Please enter the password: ')
    
    if password == 'prospero':
        print('Password accepted.')
        
    else:
         print('Password is invalid.')
         
def sort_names():
    
    first_name = input('Enter the first name (last, first): ')
    second_name = input('Enter the second name (last, first): ')
    
    print('Here are the names, alphabetically.')
    
    if first_name < second_name:
        print(first_name)
        print(second_name)
    else:
        print(second_name)
        print(first_name)
        
def loan_qualifier():
    
    salary = int(input('Enter your annual salary: '))
    years = int(input('Enter the number of years at your current job: '))
    
    if salary >= 30000:
        
        if years >= 2:
            print('You qualify for the loan.')
        else:
            print('You must have been on your current job for at least two years to qualify.')
            
    else:
        print('You must earn at least $30,000 per year to qualify.')
        
def grader():
    
    score = int(input('Enter your test score: '))
    
    if score >= 90:
        grade = 'A'
    else:
        if score >= 80:
            grade = 'B'
        else:
            if score >= 70:
                grade = 'C'
            else:
                if score >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
                    
    print('Your grade is ', grade, '.', sep = '')
    
def grader_v2():
    
    score = int(input('Enter your test score: '))
    
    if score >= 90:
        grade = 'A'
        
    elif score >= 80:
        grade = 'B'
            
    elif score >= 70:
        grade = 'C'

    elif score >= 60:
        grade = 'D'
    
    else:
        grade = 'F'
                    
    print('Your grade is ', grade, '.', sep = '')

def loan_qualifier_v2():
    
    salary = int(input('Enter your annual salary: '))
    years = int(input('Enter the number of years at your current job: '))
    
    if salary >= 30000 and years >= 2:
        
        print('You qualify for the loan.')
        
    else:
        print('You must have been on your current job for at least two years to qualify and have an annual salary of $30,000 or more.')
        
def loan_qualifier_v3():
    
    salary = int(input('Enter your annual salary: '))
    years = int(input('Enter the number of years at your current job: '))
    
    if salary >= 30000 or years >= 2:
        
        print('You qualify for the loan.')
        
    else:
        print('You must have been on your current job for at least two years to qualify or have an annual salary of $30,000 or more.')

def target_game():
    
    import turtle
    
    turtle.setup(600,600)
    
    # draw the target thing
    turtle.speed(10)
    turtle.penup()
    turtle.goto(100,250)
    turtle.pendown()
    turtle.forward(25)
    turtle.setheading(90)
    turtle.forward(25)
    turtle.setheading(-180)
    turtle.forward(25)
    turtle.goto(100,250)
    
    # return to center
    turtle.penup()
    turtle.goto(0,0)
    
    # ask stuff
    angle = int(input('''Enter the projectile's angle: '''))
    