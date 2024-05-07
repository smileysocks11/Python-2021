import random
import matplotlib.pyplot as plt
# ---------------------------------------------------------------------

def lottery(): # Exercise 2
    # lottery accepts no arguments
    # generates seven random numbers, each in the range 0-9
    # assigns each number to a list element
    # displays the contents of the list
    
    # creates empty list
    numbers = []
    
    print('Generating lotto numbers...')
    print('Your lotto numbers are:')
    
    for i in range(1, 8):
        
        # generates random number
        random_number = random.randint(0, 9)
        
        # adds the random number to the list
        numbers.append(random_number)
        
    # displays the contents of the list
    for number in numbers:
        print(number)
        
# ---------------------------------------------------------------------
    
def rainfall(): # Exercise 3
    # rainfall accepts no arguments
    # lets user enter total rainfall for each of the 12 months
    # calculates and displays the total rainfall for the year,
    # the average monthly rainfall, the months with the highest and lowest amounts
    
    MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    rainfall = []
    
    for month in MONTHS:
        
        # asks the user for input
        string = 'Enter the rainfall for ' + month + ': '
        rain_amount = (int(input(string)))
        
        # validation
        while rain_amount < 0:
            string = 'Error. Please enter a valid amount of rainfall for ' + month + ': '
            rain_amount = (int(input(string)))
            
        # appends the rain amount to the list
        rainfall.append(rain_amount)
      
    print()
    # figures out the month with the least rain
    min_inches = min(rainfall)
    min_index = rainfall.index(min(rainfall))
    min_month = MONTHS[min_index]
    
    # outputs month with the least rain
    print(min_month, 'had the most rain with', min_inches, 'of rain.')
    
    # figures out the month with the most rain
    max_inches = max(rainfall)
    max_index = rainfall.index(max(rainfall))
    max_month = MONTHS[max_index]
    
    # outputs month with the most rain
    print(max_month, 'had the most rain with', max_inches, 'of rain.')
    
    # calculates the total rain for the year and outputs it
    total = 0
    for inches in rainfall:
        total += inches
        
    print('Total rain for the year:', total, 'inches')
    
    # calculates the average rain per month and outputs it
    average = total / len(rainfall)
    print('Average rain per month:', average, 'inches')
    
# ---------------------------------------------------------------------

def charge_accts(): # Exercise 5
    # charge_accts accepts no arguments
    # reads the contents of a file into a list
    # asks user to enter a charge account number
    # determines whether the number is valid by passing the info
    # displays message indicating if the number is valid/invalid and prompts user for another number
    
    again = 'y'
    
    while again.lower() == 'y':
        # asks user to enter charge account number
        search = input('Enter an account number: ')
    
        # validates for numerical input
        while search.isnumeric() == False:
            search = input('Enter an account number (numeric only): ')
    
        print()
        
        # passes the account number
        found = IsValid((search))
    
        # if the number was found, display a message
        if found == True:
            print('The account number is valid.')
      
        # if the number was not found, display a message
        else:
            print('The number is invalid.')
        
        # asks user if they want to enter another account number
        print()
        again = input('Check another account number? (y/n) ')
        print()


def IsValid(search):
    # IsValid accepts an integer search
    # searches a file for the number
    # returns the outcome of the search
    
    # boolean flag to determine search status
    found = False
    
    # opens and reads the file
    account_file = open('charge_accounts.txt', 'r')
    line = account_file.readline()
    
    # loops to read each line of the file
    while line != '':
        
        # strip the newline
        line = line.rstrip('\n')
        
        # determines if the record is found
        if line.lower() == search.lower():
            found = True
            
        # reads the next line
        line = account_file.readline()
       
    # closes the file
    account_file.close()
        
    # returns the outcome of the search
    return found

# ---------------------------------------------------------------------

def drivers_exam(): # Exercise 7
    # drivers_exam accepts no arguments
    # asks user for the test to grade
    # reads the student's answers for each of the 20 question from a text file
    # displays message indicating whether the students passed or failed the exam
    # showing the question numbers of the incorrectly answered questions
    
    missed = []
    student_answers = []
    key_answers = []
    index = 0
    correct = 0
    incorrect = 0
    again = 'y'
    success = 0
# ---------
    # opens test key file
    key_file = open('driver_test_key.txt', 'r')
    line = key_file.readline()
    
    while line != '':
        
        # strip the newline
        line = line.rstrip('\n')
        
        # adds each answer to the answer key list
        key_answers.append(line)
    
        # reads new line
        line = key_file.readline()
        
    # closes file
    key_file.close()
    
    while again.lower() == 'y':
        
        # gets input from user
        file_name = input('Please enter the name of the file to read: ')
        
        try:
            # opens and reads file
            exam_file = open(file_name, 'r')
            line = exam_file.readline()
            
            # loops to read each line of the file
            while line != '':
            
                # strip the newline
                line = line.rstrip('\n')
            
                # adds student's answer to their answer list
                student_answers.append(line)
                
                # reads new line
                line = exam_file.readline()
                
            # closes the file
            exam_file.close()
            
            success = 1
# ---------
        # if the file entered does not exist
        except IOError:
            # outputs an error
            print()
            print(file_name,'not found.')
            
        if success == 1:
            
            # checks every item in the list
            for answer in student_answers:
                
                # if the student answer matches the answer on the key
                if answer == key_answers[index]:
                    
                    # adds a correct answer to the accumulator
                    correct += 1
                    
                # if the student answer does not match the answer on the key
                else:
                    
                    # adds the question number to the list of answers missed
                    missed.append(index + 1)
                    # adds an incorrect answer to the accumulator
                    incorrect += 1
                    
                # increments index
                index += 1
# ---------
            # outputs completion message
            print()
            print('Test grading complete.')
            
            # outputs the numbers of questions the student got correct
            print()
            print('You answered', correct, 'questions correct out of 20.')
            
            # outputs the number of questions the student got incorrect
            print('You missed', incorrect, 'questions. The minimum you could miss to pass is 5.')
            
            # figures out if the student passed the exam
            if incorrect <= 5:
                print()
                print('Congratulations, you passed the exam.')
                
            else:
                print()
                print('You did not pass, study and try again.')
                
            # outputs the question numbers, if any, that the user missed
            if incorrect > 0:
                print()
                print('Here are the questions you missed:')
                print(missed)
# ---------
        print()
        again = input('Check another test? (y/n): ')
        
# ---------------------------------------------------------------------

def tic_tac_toe(): # Exercise 11
    # tic_tac_toe accepts no arguments
    # simulates a game of tic tac toe
    # game plays out until X or O has won or the game board is filled with no winner
    # once a winner has been determined, outputs the game board and a winning message
    
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    
    player = 'O'
    tie = 0
    ROWS = 2
    COLS = 2
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    
    # while the game is still going
    winner = game_over(board)
    while winner == 'undecided':
        
        # replaces an empty slot with an X or O
        if board[row][column] == '-':
            board[row][column] = player
            if player == 'O':
                player = 'X'
            else:
                player = 'O'
                
        # creates new random coordinates for the board
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        winner = game_over(board)
     
    # prints the board and a winning message if someone won
    if winner != 'undecided' and winner != 'tie':
        
        print(winner, 'wins the match!')
        
    # prints the board and a draw message if it was a tie
    if winner == 'tie':
        print('''It's a draw!''')
        
def game_over(board):
    # game_over accepts two-dimensional list board
    # returns true/false depending if all plays have been made without winner
    
    ROWS = 2
    COLS = 2
    tie = 0
    winner = 'undecided'
    
    # for each slot in the board
    for row in range(0, ROWS + 1):
        
        for column in range(0, COLS + 1):
            
            # if the slot isn't empty
            if board[row][column] != '-':
                tie += 1
                # figures out what player symbol is in the slot
                player = board[row][column]
                
                # checks vertical winning path
                if row == 1:
                    if board[row - 1][column] == player and board[row + 1][column] == player:
                        winner = player
                        print(board[0])
                        print(board[1])
                        print(board[2])
                        return winner
              
                        
                # checks horizontal winning path
                if column == 1:
                    if board[row][column - 1] == player and board[row][column + 1] == player:
                        winner = player
                        print(board[0])
                        print(board[1])
                        print(board[2])
                        return winner
                        
                   
                # checks diagonal winning path
                if row == 1 and column == 1:
                    if board[0][0] == player and board[2][2] == player:
                        winner = player
                        print(board[0])
                        print(board[1])
                        print(board[2])
                        return winner

                   
                    if board[2][0] == player and board[0][2] == player:
                        winner = player
                        print(board[0])
                        print(board[1])
                        print(board[2])
                        return winner

    # if all the spaces are filled, its a tie
    if tie == 9:
        winner = 'tie'
        print(board[0])
        print(board[1])
        print(board[2])
        return winner
    
    # returns outcome if no winner is found
    return winner

# ---------------------------------------------------------------------

def magic_8_ball(): # Exercise 13
    # magic_8_ball accepts no arguments
    # reads the responses from the file into a list
    # prompts user to ask a question
    # then displays one of the responses by random
    # repeats until the user is ready to quit
    
    responses = []
    
    # opens test key file
    response_file = open('8_ball_responses.txt', 'r')
    line = response_file.readline()
    
    # reads responses from the file into a list
    while line != '':
        
        # strip the newline
        line = line.rstrip('\n')
        
        # adds each answer to the answer key list
        responses.append(line)
    
        # reads new line
        line = response_file.readline()
        
    # closes file
    response_file.close()
    
    # asks user for input
    question = input('What is your question? ')
    print()
    
    # chooses random response from the list and displays it
    response = random.randint(0, len(responses))
    print(responses[response])
    
# ---------------------------------------------------------------------

def white_elephant(): # Exercise 12
    # white_elephant accepts no arguments
    # decides which person will give a gift to what person
    # each person in the department gets someone from another department
    
    # who is in which department as lists
    DEVELOPMENT = ['Julia', 'Oliver', 'Abigail']
    HR = ['Camden', 'Kayleigh', 'Cooper', 'Kerrigan']
    SALES = ['Avery', 'Charlotte', 'Elle']
    
    # list of gifters and receivers
    gifters = ['Julia', 'Oliver', 'Abigail', 'Camden', 'Kayleigh', 'Cooper', 'Kerrigan','Avery', 'Charlotte', 'Elle']
    
    messages = []
    finished = False
    
    while finished == False:
        
        check = 0
        
        receivers = ['Julia', 'Oliver', 'Abigail', 'Camden', 'Kayleigh', 'Cooper', 'Kerrigan','Avery', 'Charlotte', 'Elle']
        
        # assigns the gifter's department
        for gifter in gifters:
            
                
            if gifter in DEVELOPMENT:
                department = DEVELOPMENT
                    
            if gifter in HR:
                department = HR
                
            if gifter in SALES:
                department = SALES
               
            # picks a random receiver from people who haven't gotten a gift yet
            receiver = random.choice(receivers)
            
            # picks a new receiver until the receiver isn't in the same department as the gifter and is not the gifter
            while (gifter == receiver) or (receiver in department):
                
                receiver = random.choice(receivers)
                    
                check += 1
                
                # prevents the program from going in an endless loop
                if check > 40:
                    receiver = 'redo'
            
            # if the app doesn't need to be reset
            if receiver != 'redo':
                # adds the gift message to the messages
                message = gifter + ' gifts to '+ receiver
                messages.append(message)
                
                # removes receiver from the people who haven't received gifts
                receivers.remove(receiver)
        
        # resets the list of receivers
        if receiver == 'redo':
            finished = False
            
        else:
            # prints each gifting message
            for line in messages:
                print(line)
                
            # ends the while loop
            finished = True
            
# ---------------------------------------------------------------------

def write_expenses(): # Exercise 14
    # record accepts no arguments
    # prompts user to enter information costs
    # saves it to a text file to record expenses for the last month
    
    CATEGORIES =  ['Rent', 'Gas', 'Food', 'Clothing', 'Car', 'Misc']
    
    # opens a new file
    expense_file = open('expenses.txt', 'w')
    
    # gets input from the user
    for category in CATEGORIES:
        
        message = 'Please enter the expenses last month for ' + category + ': '
        expense = input(message)
        
        # appends the data to the file
        expense_file.write(category + '\n')
        expense_file.write(expense + '\n')
        
    # closes the file
    expense_file.close()
    
    # creates the pie chart
    read_expenses()

def read_expenses():
    # read_expenses accepts no arguments
    # uses matplotlib to plot a pie chart showing how you spend your money
    
    expenses = []
    categories = []
    
    # opens the file
    expense_file = open('expenses.txt', 'r')
    
    # gets the first category from the file
    category = expense_file.readline()
    
    # loops to read each line of the file
    while category != '':
        
        # adds the category label to the list of labels
        category = category.rstrip('\n')
        categories.append(category)
        
        # gets expense and appends it to the list of expenses
        expense = expense_file.readline()
        expenses.append(expense)
        
        # gets the next category label
        category = expense_file.readline()
        
    # sets the pie colours
    plt.pie(expenses, colors=('b', 'orange', 'g', 'r', 'purple', 'brown'))
    
    # draws the pie chart
    plt.pie(expenses, labels=categories)
    
    # adds a title
    plt.title('Monthly Expenses')
    
    # shows the pie chart
    plt.show()
        
# ---------------------------------------------------------------------

def gas_graph(): # Exercise 15
    # gas_graph accepts no arguments
    # reads the contents of the file
    # plots the data as a line graph
    
    averages = []
    weeks = []
    
    # reads file
    gas_file = open('1994_Weekly_Gas_Averages.txt', 'r')
    
    # gets the first average from the file
    average = gas_file.readline()
    
    week = 0
    # loops to read every line in the file
    while average != '':
        
        # adds the average to the list of averages
        average = average.rstrip('\n')
        averages.append(average)
        
        # increments the week by 1 and adds to the list of week labels
        week += 1
        weeks.append(week)
        
        # reads the next average
        average = gas_file.readline()
    
    # creates the line graph
    plt.plot(weeks, averages)
    
    # adds a title
    plt.title('1994 Weekly Gas Averages')
    
    # adds labels to the each axis
    plt.xlabel('Weeks')
    plt.ylabel('Gas Prices / Gallon')
    
    # adds tick marks
    plt.xticks([0, 10, 20, 30, 40, 50])
    
    # displays the line graph
    plt.show()