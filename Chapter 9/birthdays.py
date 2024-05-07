# ---------------------------------------------------------------------

def birthday_main():
    
    birthdays = {}
    choice = 0
    
    LOOK_UP = 1
    ADD = 2
    CHANGE = 3
    DELETE = 4
    QUIT = 5
    
    while choice != QUIT:
        
        choice = get_menu_choice()
        
        if choice == LOOK_UP:
            look_up(birthdays)
            
        if choice == ADD:
            birthdays = add_bday(birthdays)
         
        if choice == CHANGE:
            change_bday(birthdays)
            
        if choice == DELETE:
            delete_bday(birthdays)
        
def get_menu_choice():
    
    print('Friends and their birthdays')
    print('------------------------------')
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit the program')
    print()
    
    choice = int(input('Enter your menu choice: '))

    return choice

def look_up(birthdays):
    
    name = input('Enter a name to look up: ')
    
    if birthdays == {}:
        print()
        print('There are no birthdays to search!')
        print()
        
    else:
        birthday = birthdays.get(name, 'Name not found.')
        print()
        print('Birthday for', name, ':', birthday)
        print()
            
def add_bday(birthdays):
    
    name = input('Enter a name: ')
    birthday = input('Enter a birthday: ')
    
    if name not in birthday:
        
        birthdays[name] = birthday
   
        print()
        print('Birthday added for', name)
        print()
    
    else:
        print(name, 'has already been added to the dictionary.')
        print()
        
    return birthdays
 
def change_bday(birthdays):
    
    name = input('Enter a name to change the birthday for: ')
    
    if name in birthdays:
        birthday = input('Enter a new birthday: ')
        birthdays.pop(name)
        birthdays[name] = birthday
        print()
        print('Birthday was changed for', name)
        print()
        
    else:
        print(name, 'was not found.')
        print()
      
def delete_bday(birthdays):
    
    name = input('Enter a name to delete: ')
    print()
    
    if name in birthdays:
        birthdays.pop(name)
        print(name, 'deleted.')
        print()
    
    else:
        print(name, 'was not found.')
        print()