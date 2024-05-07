import os

# ---------------------------------------------------------------------

def write_names():
    
    print('Please enter the names of three friends.')
    friend1 = input('Friend 1: ')
    friend2 = input('Friend 2: ')
    friend3 = input('Friend 3: ')
    
    myfile = open('friends.txt', 'w')
    
    myfile.write(friend1 + '\n')
    myfile.write(friend2 + '\n')
    myfile.write(friend3 + '\n')
    
    myfile.close()
    
# ---------------------------------------------------------------------

def strip_newline():
    
    infile = open('lotr.txt', 'r')
    
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    infile.close()
    
    print(line1)
    print(line2)
    print(line3)
    
# ---------------------------------------------------------------------

def write_names2():
    
    print('Please enter the names of three friends.')
    friend1 = input('Friend 1: ')
    friend2 = input('Friend 2: ')
    friend3 = input('Friend 3: ')
    
    myfile = open('friends.txt', 'a')
    
    myfile.write(friend1 + '\n')
    myfile.write(friend2 + '\n')
    myfile.write(friend3 + '\n')
    
    myfile.close()
    
# ---------------------------------------------------------------------

def write_numbers():
    
    number1 = input('Please enter a number: ')
    number2 = input('Please enter a number: ')
    number3 = input('Please enter a number: ')
    
    myfile = open('numbers.txt', 'a')
    
    myfile.write(number1 + '\n')
    myfile.write(number2 + '\n')
    myfile.write(number3 + '\n')
    
    myfile.close()
    
# ---------------------------------------------------------------------

def write_sales():
    
    sales = int(input('How many days do you want to enter sales for? '))
    
    sales_file = open('sales.txt', 'w')
    
    for sale in range(1, sales + 1):
        sale = float(input('Enter the sales for day #' + str(sale) + ': '))
        
        sales_file.write(str(sale) + '\n')
        
    sales_file.close()
    print('All data has been saved to sales.txt.')
    
# ---------------------------------------------------------------------

def read_sales():
    
    sales_file = open('sales.txt', 'r')
    
    line = sales_file.readline()
    
    while line != '':
        amount = float(line)
        
        print(format(amount, ',.2f'))
        
        line = sales_file.readline()
        
    sales_file.close()
    
# ---------------------------------------------------------------------

def read_sales2():
    
    sales_file = open('sales.txt', 'r')
    
    for line in sales_file:
        
        amount = float(line)
        
        print(format(amount, ',.2f'))
        
    sales_file.close()
    
# ---------------------------------------------------------------------

def write_video_times():
    
    videos = int(input('How many videos are in the project? '))
    
    video_file = open('video_times.txt', 'w')
    
    for video in range(1, videos+1):
        
        length = (input('Enter the time for video #' + str(video)))
        
        video_file.write(length + '\n')
        
    print('All times have been written to video_times.txt.')
    
    video_file.close()
    
    
def read_video_times():
    
    video_file = open('video_times.txt', 'r')
    
    index = 0
    total_time = 0
    
    for line in video_file:
        
        index += 1

        print('Video #' + str(index), 'time:', line, 'seconds')
        
        total_time += int(line)
        
    print('The total running time of all videos is', total_time, 'seconds.')
        
# ---------------------------------------------------------------------

def save_emp_records():
    
    records = int(input('How many employee records do you want to enter? '))
    print()
    
    emp_file = open('employees.txt', 'w')
    
    for record in range(1, records + 1):
        
        print('Enter data for employee #' + str(record))
        name = input('Name: ')
        id_number = input('ID Number: ')
        department = input('Department: ')
        print()
        
        emp_file.write(name + '\n')
        emp_file.write(id_number + '\n')
        emp_file.write(department + '\n')
        
    print('All records were saved to employees.txt.')
    emp_file.close()
    
def read_emp_records():
    
    emp_file = open('employees.txt', 'r')
    index = 1
    name = emp_file.readline()
    
    while name !='':
        id_number = emp_file.readline()
        department = emp_file.readline()
        
        name = name.rstrip('\n')
        id_number = id_number.rstrip('\n')
        department = department.rstrip('\n')
        
        print('Record for employee #' + str(index))
        print('Name:', name)
        print('ID Number:', id_number)
        print('Department:', department)
        print()
        
        name = emp_file.readline()
        index += 1
    print()
    print(index - 1, 'records retrieved.')
    emp_file.close()
    
# ---------------------------------------------------------------------

def write_coffee():
    
    another = 'y'
    coffee_file = open('coffee.txt', 'a')
    
    while another.lower() == 'y':
        print('Enter the following coffee data:\n')
        desc = input('Description: ')
        pounds = input('Quantify (in pounds): ')
        
        coffee_file.write(desc + '\n')
        coffee_file.write(pounds + '\n')
        
        another = input('\nDo you wish to enter another coffee? (y to continue):')
        
    coffee_file.close()
    print('\nAll data appended to coffee.txt.')
    
def read_coffee():
    
    coffee_file = open('coffee.txt', 'r')
    desc = coffee_file.readline()
    
    while desc != '':
        pounds = coffee_file.readline()
        
        desc = desc.rstrip('\n')
        pounds = pounds.rstrip('\n')
        
        print('\nDescription:', desc)
        print('Quantity (in pounds):', pounds)
        
        desc = coffee_file.readline()
        
    coffee_file.close()
    print('\nAll records retrieved.')
    
def search_coffee():
    
    found = False
    
    search = input('Enter a coffee description to search for: ')
    
    coffee_file = open('coffee.txt', 'r')
    
    desc = coffee_file.readline()
    
    while desc != '':
        pounds = coffee_file.readline()
        
        desc = desc.rstrip('\n')
        
        if desc.lower == search.lower():
            print('\nRecord found!\n')
            print('Description:', desc)
            print('Quantity (in pounds):', pounds)
            found = True
            
        desc = coffee_file.readline()
        
    coffee_file.close()
    
    if not found:
        print('\nThe record was not found.')
        
def modify_coffee():
    
    # boolean flag variable
    found = False
    
    # get the search description and new quantity
    search = input('Enter the coffee description to modify: ')
    new_qty = input('ENter the new quantity: ')
    
    # open the coffee.txt file to read and a new temporary file to write
    coffee_file = open('coffee.txt', 'r')
    temp_file = open('temp.txt', 'w')
    
    # read the first description
    desc = coffee_file.readline()
    
    # loop to read and process each line
    while desc != '':
        qty = coffee_file.readline()
        
        # strip newline
        desc = desc.rstrip('\n')
        qty = qty.rstrip('\n')
        
        if search.lower == desc.lower(): # coffee found
            # write the description and new quantity to the temp file
            temp_file.write(desc + '\n')
            temp_file.write(new_qty + '\n')
            found = True
        
        else:
            # write the original record to the temp file
            temp_file.write(desc + '\n')
            temp_file.write(qty + '\n')
            
        # read the new description
        desc = coffee_file.readline()
        
    # all records have been processed, remove and rename files
    coffee_file.close()
    temp_file.close()
    
    # delete the original
    os.remove('coffee.txt')
    
    # rename the temp file to coffee.txt
    os.rename('temp.txt', 'coffee.txt')
    
    # description not found
    if found == False:
        print('\nRecord not found.')
        
    else:
        print('The quantity for', search, 'has been updated to', new_qty, 'pounds.')
        
        
def delete_coffee():
    
    # boolean flag variable
    found = False
    
    # get the search description and new quantity
    search = input('Enter the coffee description to modify: ')
    new_qty = input('ENter the new quantity: ')
    
    # open the coffee.txt file to read and a new temporary file to write
    coffee_file = open('coffee.txt', 'r')
    temp_file = open('temp.txt', 'w')
    
    # read the first description
    desc = coffee_file.readline()
    
    # loop to read and process each line
    while desc != '':
        qty = coffee_file.readline()
        
        # strip newline
        desc = desc.rstrip('\n')
        qty = qty.rstrip('\n')
        
        if search.lower() != desc.lower(): # coffee found
            # write the description and quantity to the temp file
            temp_file.write(desc + '\n')
            temp_file.write(qty + '\n')
        
        else:
            # toggle flag to true
            found = True
        
    # all records have been processed, remove and rename files
    coffee_file.close()
    temp_file.close()
    
    # delete the original
    os.remove('coffee.txt')
    
    # rename the temp file to coffee.txt
    os.rename('temp.txt', 'coffee.txt')
    
    # description not found
    if found == False:
        print('\nRecord not found.')
        
    else:
        print(search, 'has been deleted from coffee.txt.')
        
def coffee_shop():
    
    ADD = 1
    MODIFY = 2
    DELETE = 3
    DISPLAY = 4
    EXIT = 5
    
    # coffee shop accepts no arguments
    # calls coffee_shop_menu to display a menu to the user
    # and calls each function according to the user input
    
    # asks user for what they would like to do
    choice = int(input('Inventory option: '))
    
    if choice == ADD:
        write_coffee()
        
    if choice == MODIFY:
        modify_coffee()
        
    if choice == DELETE:
        delete_coffee()
        
    if choice == DISPLAY:
        read_coffee()

    if choice == EXIT:
        print('Thanks for choosing Caffeine Overload.')
        
def coffee_shop_menu():
    # coffee_shop_menu accepts no arguments
    # prints the menu
    print('Welcome to Caffeine Overload Inventory Control System. Please choose an inventory option.')
    print('1) Add a record')
    print('2) Modify a record')
    print('3) Delete a record')
    print('4) Display all saved records')
    print('5) Exit')
    
# ---------------------------------------------------------------------

def division():
    
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a second number: '))

    if num2 != 0:
        result = num1 / um2
        print(num1, 'divided by', num2, 'is', result)
    
    else:
        print('Cannot divide by 0.')
        
# ---------------------------------------------------------------------

def gross_pay1():
    
    hours = int(input('Enter the number of hours worked: '))
    rate = float(input('Enter the pay rate: '))
    
    pay = hours * rate
    
    print('Gross pay: $', format(pay, ',.2f'), sep = '')