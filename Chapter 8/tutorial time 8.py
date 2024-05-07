import login
# ---------------------------------------------------------------------

def count_t():
    
    word = input('Please enter a word: ')
    count = 0
    
    for ch in word:
        if ch.lower() == 't':
            count += 1
            
    print('The letter T or t appears', count, 'times in the word')
    
# ---------------------------------------------------------------------

def concatenate():
    
    name = 'Carmen'
    
    print('Where in the world is ' + name)
    
    name = 'Sandiego'
    
    print('Where in the world is ' + name)
    
# ---------------------------------------------------------------------

def generate_login():
    
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    idnumber = input('Enter your id number: ')
    
    user_login = login.get_login_name(first, last, idnumber)
    
    print('Your system login name is: ')
    print(user_login)
    
# ---------------------------------------------------------------------

def string_test():
    
    user_string = input('Enter a string to evaluate: ')
    
    if user_string.isalnum():
        print('The string only contains alphanumeric characters.')
        
    if user_string.isdigit():
        print('The string only contains digits.')
        
    if user_string.isalpha():
        print('The string only contains alpha characters.')
        
    if user_string.isspace():
        print('The string only contains whitespaces.')
        
    if user_string.islower():
        print('The string is all lowercase.')
        
    if user_string.isupper():
        print('The string is all uppercase.')
        
    print()
    print('Your string converted to all uppercase is: ', user_string.upper())
    print('Your string converted to all lowercase is: ', user_string.lower())
    
# ---------------------------------------------------------------------

def validate_password():
    
    password = input('Please enter your password: ')
    
    is_valid = login.valid_password(password)
    
    while is_valid == False:
        print('The password you entered is not valid. Please try again.')
        is_valid = login.valid_password(password)
        print()
        password = input('Please enter your password: ')
        
    print()
    print('Password accepted.')
    
# ---------------------------------------------------------------------

def repetition():
    
    for count in range(1,10):
        print('Z' * count)
        
    for count in range(8, 0, -1):
        print('Z' * count)
        
# ---------------------------------------------------------------------

def string_split():
    
    list1 = []
    
    string_one = 'one=two=three=four'

    string_two = string_one.split('=')
    
    list1.append(string_two)
    
    print(string_two)
    
# ---------------------------------------------------------------------

def split_date():
    
    date = '11/26/2018'
    
    date.split('/')
    
    print('Month:',  date[0])
    print('Day', date[1])
    print('Year', date[2])