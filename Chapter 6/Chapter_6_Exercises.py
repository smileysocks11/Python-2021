import random
# ---------------------------------------------------------------------

def line_numbers(): # Exercise 3
    # line_numbers accepts no arguments
    # asks user for the name of a file
    # displays the contents of the file with each line preceded with the line number followed by a colon
    
    # prompts user for file name
    file_name = input('Enter the name of the file: ')
    
    try:
        # opens and reads the file
        user_file = open(file_name, 'r')
        line = user_file.readline()
    
        # for every line in the file
        line_number = 1
        while line != '':
        
            # prints the line number followed by the number
            print(line_number, ';', line)
            line_number += 1
            line = user_file.readline()
        
        # closes file
        user_file.close()
        
    except IOError as err: # if the file entered does not exist
        
        # outputs an error
        print(err)
        
# ---------------------------------------------------------------------

def line_counter(): # Exercise 4
    # line_counter accepts no arguments
    # prompts user for a filename
    # displays the number of lines that are stored in the file
    # outputs the total number of items in the file
    
    # gets input from the user
    file_name = input('Enter the file to read: ')
    
    
    try:
        # opens and reads the file
        user_file = open(file_name, 'r')
        line = user_file.readline()
    
        # figures out how many lines that are stored in the file
        total_lines = 0
        while line != '':
            
            total_lines += 1
            line = user_file.readline()
         
        # outputs the number of files in the file
        print(file_name, 'contains', total_lines, 'lines.')
        
        # closes file
        user_file.close()
        
    except IOError as err: # if file entered does not exist
        
        # outputs an error
        print(err)
        
# ---------------------------------------------------------------------

def average_of_numbers(): # Exercise 6
    # average_of_number accepts no arguments
    # opens a file named numbers.txt to read
    # reads and calculates the average of all numbers in the file
    
    # opens and reads the file
    number_file = open('numbers.txt', 'r')
    line = (number_file.readline())
    
    # sets variables
    summ = 0
    total_numbers = 0
    
    # calculates the average of all the items in the file
    while line != '':
        
        line = line.rstrip('\n')
        summ += int(line)
        total_numbers += 1
        line = (number_file.readline())
        
    # outputs the average
    average = summ / total_numbers
    print('There were', total_numbers, 'items with an average value of', float(average))
    
    # closes file
    number_file.close()

# ---------------------------------------------------------------------

def ran_num_writer(): # Exercise 7
    # ran_num_writer accepts no arguments
    # writes a series of random numbers to a file
    # outputs a completion message
    
    # gets input from user
    numbers = input('How many numbers do you want to generate? ')
    
    try:
            
        numbers = int(numbers)
        # opens file
        random_file = open('ran_number_list.txt', 'w')
    
        for number in range(1, numbers + 1):
        
            random_number = random.randint(1, 500)
            random_file.write(str(random_number) + '\n')
            
        # closes file
        random_file.close()
        # outputs a completion message
        print('All numbers written to ran_number_list.txt.')
        
    except ValueError as err: # if the file entered does not exist
        # outputs error message
        print(err)
# future Sophie figure out what exception is for the input that isn't a number

# ---------------------------------------------------------------------

def ran_num_reader(): # Exercise 8
    # ran_num_reader accepts no arguments
    # displays the random numbers,
    # total of all numbers,
    # and the number of numbers read
    
    # opens and reads file
    random_file = open('ran_number_list.txt', 'r')
    line = random_file.readline()
    
    # for every line in the file
    line_number = 0
    total = 0
    while line != '':
        
        # outputs the random number
        line = line.rstrip('\n')
        print(line)
        line_number += 1
        total += int(line)
        line = random_file.readline()

    # outputs total of the random numbers
    print('The total of the', line_number, 'random numbers is', total)
    
    # closes file
    random_file.close()
    
# ---------------------------------------------------------------------

def golf_main(): # Exercise 10
    # golf_main accepts no arguments
    # calls different functions to run the program
    
    # constant menu choices
    READ = 1
    APPEND = 2
    EXIT = 3
    
    # calls golf_menu that displays the menu
    choice = golf_menu()
    
    # calls function depending on the user's choice
    if choice == READ:
        golf_read()
        
    if choice == APPEND:
        golf_write()
        
    elif choice == EXIT:
        print()
        print('Thank you for using Hole in Twelve golf management system. Have a great day!')
        
        
def golf_menu():
    # golf_menu accepts no arguments
    # outputs a menu to the user
    # returns the user's choice
    
    # displays menu
    print('Welcome to Hole in Twelve golf management system.')
    print('Please choose from the following commands...')
    print()
    print('1) Read golf data')
    print('2) Append golf data')
    print('3) Exit')
    
    # asks user for their choice
    menu_choice = int(input('Menu choice: '))
    
    # returns their choice
    return menu_choice

def golf_read():
    # golf_read accepts no arguments
    
    # opens and reads the file
    golf_file = open('golf.txt', 'r')
    line = golf_file.readline()
    
    # for every line in the file
    print()
    space = 0
    while line != '':
        
        # prints the golfer and their score for each entry
        line = line.rstrip('\n')
        print(line)
        
        if space % 2 > 0:
            print()
            
        space += 1
        line = golf_file.readline()
        
    # closes file
    golf_file.close()
    print('All records successfully read!')
        
def golf_write():
    # golf_append accepts no arguments
    # allows the user to write more data to the file
    
    # opens the file
    another = 'y'
    golf_file = open('golf.txt', 'a')
    
    while another.lower() == 'y':
        
        # asks user to input the info
        print()
        name = input('''Golfer's name: ''')
        score = input('Score: ')
        
        # appends the info to golf.txt
        golf_file.write(name + '\n')
        golf_file.write(score + '\n')
        
        # asks the user if they want to continue
        print()
        another = input('Add another golfer? (y/n) ')
        
    # closes the file
    golf_file.close()
    print('Golf data written to golf.txt.')
    
# ---------------------------------------------------------------------

def webpage(): # Exercise 11
    # webpage accepts no arguments
    # prompts user to enter their name
    # asks user for a sentence that describes themself
    # creates html file with the input and the html code necessary to create the webpage
    
    # gets input from the user
    name = input('Enter your name: ')
    desc = input('Write a short description of yourself: ')
    
    # opens the file
    file_name = ('{}.html'.format(name))
    html_file = open(file_name, 'w')
    
    # makes the webpage
    html_file.write('<html>')
    html_file.write('<head>')
    html_file.write('</head>')
    html_file.write('<body>')
    html_file.write('\t<center>')
    html_file.write('\t\t<hl>' + name + '<hl>')
    html_file.write('\t<center>')
    html_file.write('<hr />')
    html_file.write('\t' + desc)
    html_file.write('\t<hr />')
    html_file.write('</body>')
    html_file.write('</html>')
    
    print()
    print('Webpage information saved to', file_name)
    
# ---------------------------------------------------------------------

def avg_steps(): # Exercise 12
    # avg_steps accepts no arguments
    # averages the number of steps taken each month
    # outputs the months and the average number of steps
    
    # constants
    DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MONTHS = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    EXTRA_TAB = ['January','March', 'April', 'May', 'June', 'July', 'August', 'October']
    
    # opens and reads file
    steps_file = open('steps1.txt', 'r')
    line = steps_file.readline()
    
    # preset variables
    index = 0
    summ = 0
    average = 0
    
    # for every month
    for month in MONTHS:
        
        # add the number of steps in a day to the sum for the month
        for days in range(1, int(DAYS_PER_MONTH[index]) + 1):
            summ += int(line)
            line = steps_file.readline()
           
        # calculates the average number of steps for the month
        average = summ / DAYS_PER_MONTH[index]
        
        # adds an extra tab if the month needs it to format correctly
        if month in EXTRA_TAB:
            print(month, '\t\t\t', format(average, ',.2f'),' steps', sep ='')
        
        # prints a table with the month name and the average number of steps
        else:
            print(month, '\t\t', format(average, ',.2f'),' steps', sep ='')
            
        # resets variables
        summ = 0
        average = 0
        index += 1
        
    # closes the file
    steps_file.close()