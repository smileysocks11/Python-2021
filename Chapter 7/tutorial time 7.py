import random
import matplotlib.pyplot as plt
# ---------------------------------------------------------------------

def sales_list():
    
    NUM_DAYS = 5
    sales = []
    index = 0
    
    print('Enter the sales for each day: ')
    
    for day in range(0, 5):
        
        sales.append(input(day))
        
    print('Here are the values you entered: ')
    
    for sale in sales:
        print(sale)
        
# ---------------------------------------------------------------------

def in_list():
    
    PARTS = ['V45', 'V65', 'VF750', 'VFR1100', 'VTX1300']
    
    search = input('Enter a string to search: ')
    
    if search in PARTS:
        print('Part number', search, 'was found in the list of part numbers.')
        
    else:
        print('Part number was not found.')
        
# ---------------------------------------------------------------------

def list_append():
    
    names = []
    continues = 'y'
    
    while continues == 'y':
        name = input('Enter a name: ')
        names.append(name)
        continues = input('Add another name? (y to continue) ')
        
# ---------------------------------------------------------------------

def list_index():
    
    food = ['Fries', 'Pizza', 'Hotdog']
    
    query = input('Enter the string to search for: ')
    
    if query in food:
        replacement = input('Item found. Enter a new food item: ')
        
        food[index] = replacement
    else:
        print('Ice Cream was not found in the list. Check your spelling and try again.')
        
    print(food)
    
# ---------------------------------------------------------------------

def list_insert():
    
    names = ['Bruce', 'Steve', 'Tony']
    
    print('Here is the list before the insert method:', names)
    
    names.insert(2, 'Sam')
    
    print('Here is the new list after the insert method', names)
    
# ---------------------------------------------------------------------

def list_remove():
    
    food = ['Burger', 'Pizza', 'Hotdog']
    
    remove_item = input('Enter the string to remove: ')
    
    if remove_item in food:
        food.remove(remove_item)
        print('Item removed.')
    else:
        print(remove_item, 'was not found in the list. Check your spelling and try again.')
        
    print('Here is the list:', food)
    
# ---------------------------------------------------------------------

def barista_pay():
    
    hours = []
    employees = input('How many employees do you want to calculate pay for? ')
    total = 0
    index = 0
    
    for i in range(0, 4):
        hours.append(int(input('Enter the hours worked by employee:')))
        
    rate = int(input('Enter the hourly rate for all employees: '))
    
    for item in hours:
        print('Gross pay for employee', (index + 1), ':', rate * item)
        index += 1
        
# ---------------------------------------------------------------------

def list_total():
    
    numbers = [2, 4, 6, 8, 10]
    total = 0
    
    for number in numbers:
        total += number
        
    print('The sum of the numbers', numbers, 'is:', total)
    
# ---------------------------------------------------------------------

def list_avg():
    
    numbers = [2.5, 7.3, 6.5, 4.0, 5.2]
    total = 0
    
    for number in numbers:
        total += number
        
    average = total / len(numbers)
    
    print('The average of the numbers', numbers, 'is:', average)
    
# ---------------------------------------------------------------------

def list_function():
    
    numbers = [2, 4, 6, 8, 10]
    
    total = get_total(numbers)
    
    print('The total of', numbers, 'is:', total)
    
def get_total(numbers):
    
    total = 0
    
    for number in numbers:
        total += number
        
    return total

# ---------------------------------------------------------------------

def list_return():
    
    numbers = get_values()
    print('You entered the numbers:', numbers)
    
def get_values():
    
    continuing = 'y'
    numbers = []
    
    while continuing == 'y':
        number = int(input('Input a number: '))
        continuing = input('Do you want to enter another number? (y/n) ')
        numbers.append(number)
        
    return numbers

# ---------------------------------------------------------------------

def test_calc():
    total = 0
    scores = get_scores()
    
    try:
        lowest = min(scores)
        scores.remove(lowest)
        
        print()
        print('Dropping the lowest score of', lowest)
        
    except:
        print()
        print(food_item, 'was not found in the list. Check your spelling and try again.')
        
    for score in scores:
        total += score
        
    average = total / len(scores)
    
    print()
    print('The average score, with', lowest, 'dropped from the scores, is:', float(average))
    
    
def get_scores():
    
    scores = []
    again = 'y'
    
    while again == 'y':
        score = float(input('Enter a score: '))
        scores.append(score)
        print()
        again = input('Do you want to enter another score? (y/n) ')
        
    return scores

# ---------------------------------------------------------------------

def list_writelines():
    
    cities = ['Kansas City', 'Lawrence', 'Wichita', 'Manhattan']
    
    try:
        outfile = open('cities.txt', 'w')
        
        outfile.writelines(cities)
        
        print('All data written to cities.txt')
        outfile.close()
        
    except Exception as err:
        print(err)
        
# ---------------------------------------------------------------------

def list_write():
    
    cities = ['Kansas City', 'Lawrence', 'Wichita', 'Manhattan']
    
    try:
        outfile = open('cities.txt', 'w')
        
        for city in cities:
            
            outfile.write(city + '\n')
            
        print('All data written to cities.txt')
        outfile.close()
        
    except Exception as err:
        print(err)
        
# ---------------------------------------------------------------------

def list_read():
    
    try:
        infile = open('cities.txt', 'r')
        
        cities = infile.readlines()
        
        infile.close()
        
    except:
        print('Error reading from the file.')
        
    index = 0
    
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1
    print('Here is the information read from cities.txt.')
    print(cities)
    
# ---------------------------------------------------------------------

def list_write_numbers():
    
    numbers = [1, 2, 3, 4, 5, 6, 7]
    
    outfile = open('numberlist.txt', 'w')
    
    for number in numbers:
        outfile.write(str(number) + '\n')
        
    outfile.close()
    print('All numbers saved to numberlist.txt')
    
# ---------------------------------------------------------------------

def list_read_numbers():
    
    numbers = []
    
    try:
        infile = open('numberlist.txt', 'r')
        
        for num in infile:
            numbers.append(int(num.rstrip('\n')))
            
        infile.close()
            
    except Exception as err:
        print(err)
    print('Here is the list created from numberlist.txt: ')
    print(numbers)
    
# ---------------------------------------------------------------------

def random_numbers():
    
    ROWS = 3
    COLS = 4
    
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    for row in range(ROWS):
        for col in range(COLS):
            values[row][col] = random.randint(1, 100)
            
    print(values)
    
# ---------------------------------------------------------------------

def main():
    
    plt.title('Sales by Year')
    
    plt.xlabel('Year')
    plt.ylabel('Sales')
    
    # plt.xlim(xmin = -1, xmax = 10)
    # plt.ylim(ymin = -1, ymax = 6)
    
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
    
    
    plt.xticks([0, 1, 2, 3, 4],
               ['2016', '2017', '2018', '2019', '2020'])
    
    plt.yticks([0, 1, 2, 3, 4, 5],
               ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    
    plt.plot(x_coords, y_coords, marker = 'o')
    
    plt.show()
    

# ---------------------------------------------------------------------

def bar_chart():
    
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    
    bar_width = 10
    
    plt.bar(left_edges, heights, bar_width,
            color = ('r', 'g', 'b', 'y', 'k'))
    
    plt.title('Sales by Year')
    
    plt.xlabel('Year')
    plt.ylabel('Sales')
    
    plt.xticks([5, 15, 25, 35, 45],
               ['2016', '2017', '2018', '2019', '2020'])
    
    plt.yticks([0, 100, 200, 300, 400, 500],
               ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    
    plt.show()
    
# ---------------------------------------------------------------------

def pie_chart():
    
    values = [20, 60, 80, 40]
    
    plt.pie(values)
    
    plt.show()
    
# ---------------------------------------------------------------------

def pie_chart2():
    
    sales = [100, 400, 300, 600]
    
    slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']
    
    plt.pie(sales, colors = ('r', 'g', 'b', 'y', 'k'))
    
    plt.pie(sales, labels = slice_labels)
    
    plt.title('Sales by Quarter')
    
    plt.show()