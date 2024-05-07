# ---------------------------------------------------------------------

def sum_of_digits(): # Exercise 2
    # sum_of_digits accepts no arguments
    # asks the user to enter a series of single-digit numbers
    # displays sum of all single digit numbers in the string
    
    total = 0
    
    # gets input from the user
    string = input('Please enter a string of single digit numbers without spaces: ')
    
    # validates for numerical input
    while string.isnumeric() == False:
        string = input('Please only enter numbers: ')
        
    # adds each digit in the string to the total
    for character in string:
        total += int(character)
        
    # outputs the sum of the string
    print('The sum of your string is', total)
    
# ---------------------------------------------------------------------

def date_converter(): # Exercise 3
    # date_converter accepts no arguments
    # reads a string from user containing a date in the form mm/dd/yy
    # prints date in the format March 12, 2018
    
    # list of months
    MONTHS = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    # gets input from the user
    date = input('Enter a date in the format mm/dd/yyyy: ')
    
    # validates that the format is correct and each mm dd yyyy is a valid number
    while (date[:2].isnumeric() == False) or (date[3:5].isnumeric() == False) or (date[6:].isnumeric() == False) or (date[2] != '/') or (date[5] != '/'):
        date = input('Enter a date valid in the format mm/dd/yyyy: ')
        
    # outputs the date in the correct format
    print()
    month_index = int(date[:2])
    month = MONTHS[month_index - 1]
    day = date[3:5]
    year = date[6:]
    print('The date is: ' + month + ' ' + day + ', ' + year)
    
# ---------------------------------------------------------------------

def morse_code(): # Exercise 4
    # morse_code accepts no arguments
    # asks the user to enter a message
    # converts and outputs it in morse code
    
    CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    MORSE = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••',
             '•---', '-•-', '•-••', '--', '-•', '---', '•--•', '--•-', '•-•',
             '•••', '-', '••-', '•••-', '•--', '-••-', '-•--', '--••', '•----',
             '••---', '•••--', '••••-', '•••••', '-••••', '--•••', '---••', '----•', '-----']
    
    morse_code = ''
    string = ''
    
    # gets input from the user
    message = input('Enter a message to encode to morse code: ')
    
    # removes spaces from message
    message = message.split(' ')
    
    for word in message:
        string += word
    
    # validates for only alphanumeric numbers as input
    while string.isalnum() == False:
        
        message = input('Enter only numbers and letters: ')
        for word in message:
            string += word
        
    # converts each character in the message to morse and puts it in a string
    for ch in string:
        
        ch = ch.upper()
        ch_index = CHARACTERS.index(ch)
        morse_ch = MORSE[ch_index]
        morse_code += ' '
        morse_code += morse_ch
        
    # outputs message in morse code
    print()
    print(morse_code)
    
# ---------------------------------------------------------------------

def phone_converter(): # Exercise 5
    # phone_converter accepts no arguments
    # asks user to enter a 10 digit telephone number
    # displays the telephone number with any alpha characters that appeared in the original
    # translated to their numeric equivalents
    
    LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    NUMBERS = ['2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9']
    
    string = ''
    phone_number = ' '
    
    # gets input from the user
    number = input('Enter a telephone number in the form of XXX-XXX-XXXX: ')
    
    # validates for a 10 digit telpehone number in the correct format
    while number[:3].isalnum() == False or number[4:7].isalnum() == False or number[8:].isalnum() == False or number[3] != '-' or number[7] != '-':
        number = input('Enter a valid telephone number in the form of XXX-XXX-XXXX: ')
        
    # removes -'s from message
    number = number.split('-')
    
    for ch in number:
        string += ch
    
    # converts phone number into a numeric one
    for ch in string:
        
        if ch.isdigit():
            number_ch = ch
        
        else:
            ch = ch.upper()
            ch_index = LETTERS.index(ch)
            number_ch = NUMBERS[ch_index]
        
        phone_number += number_ch
        
    # outputs converted phone number
    final_phone_number = phone_number[:4] + '-' + phone_number[4:7] + '-' + phone_number[7:]
    print('Here is your converted telephone number:', final_phone_number)

# ---------------------------------------------------------------------

def avg_num_words(): # Exercise 6
    # avg_num_words accepts no arguments
    # reads text.txt's contents and calculates the total number of words,
    # total number of sentences, and avg number of words per sentence
    
    sentences = 0
    words = 1
    string = ''
    
    # opens and reads file
    text_file = open('text.txt', 'r')
    line = text_file.read()
    
    # converts file to string
    string += line
    
    # figures out how many sentences and words are in the file
    for ch in string:
        if ch == '.':
            sentences += 1
            
        if ch == ' ' or ch == '\n':
            words += 1
            
    # figures out the average number of words per sentence
    average = format(words / sentences, '.2f')
    
    # outputs the information
    print('The file text.txt has', words, 'words.')
    print('There are', sentences, 'total sentences.')
    print('The average number of words per sentence is:', average)
    
# ---------------------------------------------------------------------

def igpay_atinlay(): # Exercise 12
    # igpay_atinlay accepts no arguments
    # accepts a sentence as input and converts each word to pig latin
    
    new_message = ''
    
    # gets input from the user
    message = input('Enter a message to convert to pig latin: ')
    
    # converts message to pig latin
    message = message.upper()
    message = message.split()
    for word in message:
        # removes first letter
        first_letter = word[0]
        word = word.replace(first_letter, '')
        # adds first letter to the end of the word
        word += first_letter
        # adds ay to the end of the word
        word += 'AY'
        new_message += word + ' '
    # puts any periods at the end of the sentence
    if '.' in new_message:
        new_message = new_message.replace(word, '')
        new_message = new_message.replace('.', '')
        word = word.replace('.', '')
        word += '.'
        new_message += word
    # outputs message converted to pig latin
    print()
    print('Here is your message in pig latin:')
    print(new_message)
    
# ---------------------------------------------------------------------

def pb_main(): # Exercise 13
    # pb_main accepts no arguments
    # calls other functions
    # performs outputs
    
    # receives values from pb_frequency
    labels, pb_labels, frequencies, pb_frequencies = pb_frequency()
    
    # calls the function which determines the most common numbers
    pb_most_common(labels, pb_labels, frequencies, pb_frequencies)
    
    # calls the function which determines the least common numbers
    pb_least_common(labels, pb_labels, frequencies, pb_frequencies)
    
def pb_frequency():
    # pb_frequency accepts no arguments
    # determines how often each number 1-69 was drawn and each powerball was drawn
    
    numbers = []
    powerballs = []
    labels = []
    pb_labels = []
    frequencies = []
    pb_frequencies = []
    
    # opens and read file
    pb_file = open('pbnumbers.txt', 'r')
    line = pb_file.readline()
    
    # loops to read each ticket in the file
    while line != '':
        
        # strips the newline
        line = line.rstrip('\n')
        
        # splits the ticket into a list of numbers
        ticket = str(line)
        ticket = ticket.split(' ')
        
        # adds the first four numbers to the list of numbers
        # adds the last number to the list of powerball numbers
        index = 0
        for number in ticket:
            if index == 5:
                powerballs.append(number)
            else:
                numbers.append(number)
            index += 1
            
        # reads new ticket
        line = pb_file.readline()
        
    # creates empty frequency list
    for i in range(0, 69):
        frequencies.append(0)
    
    # creates empty powerball frequency list
    for i in range(0, 69):
        pb_frequencies.append(0)
        
    # figures out frequency of each number
    for number in numbers:
        # adds to two parallel lists where each number corresponds with a frequency
        if number not in labels:
            labels.append(number)
        index = labels.index(number)
        frequency = frequencies[index]
        frequency += 1
        frequencies[index] = frequency
        
    # figures out frequency of each powerball number
    for number in powerballs:
        # adds to two parallel lists where each number corresponds with a frequency
        if number not in pb_labels:
            pb_labels.append(number)
        index = pb_labels.index(number)
        frequency = pb_frequencies[index]
        frequency += 1
        pb_frequencies[index] = frequency
        
    # removes any empty values in the list of powerball frequencies
    length = len(pb_labels)
    if length != len(pb_frequencies):
        pb_frequencies = pb_frequencies[:length + 1]
    
    # returns values
    return labels, pb_labels, frequencies, pb_frequencies

def pb_most_common(labels, pb_labels, frequencies, pb_frequencies):
    # pb_most_common accepts four lists; one corresponding with the other for the frequency of numbers and powerball numbers
    # determines the 10 most common numbers, ordered by frequency
    
    most_common_numbers = ''
    most_common_pb_numbers = ''
    common_frequency = 0
    common_number = 0
    
    # determines the top 10 most common numbers
    for i in range(0, 10):
        
        # if the frequency is higher than the current highest, it is now the highest
        for frequency in frequencies:
            if frequency > common_frequency:
                common_frequency = frequency
                index = frequencies.index(frequency)
                common_number = labels[index]
                
        # adds the number to the list of most common numbers
        most_common_numbers += str((common_number)) + ' '
        labels.remove((common_number))
        frequencies.remove(common_frequency)
        common_frequency = 0
        common_number = 0
    
    # determines the top 10 most common powerball numbers
    for i in range(0, 10):
        
        # if the frequency is higher than the current highest, it is now the highest
        for frequency in pb_frequencies:
            if frequency > common_frequency:
                common_frequency = frequency
                index = pb_frequencies.index(frequency)
                common_number = pb_labels[index]
                
        # adds the number to the list of most common numbers
        most_common_pb_numbers += str((common_number)) + ' '
        pb_labels.remove((common_number))
        pb_frequencies.remove(common_frequency)
        common_frequency = 0
        common_number = 0
        
    # outputs the most commonly occuring numbers and powerball numbers
    print('The most commonly occuring numbers are:', most_common_numbers)
    print('The most commonly occuring powerball numbers are:', most_common_pb_numbers)
    
def pb_least_common(labels, pb_labels, frequencies, pb_frequencies):
    # pb_most_common accepts four lists; one corresponding with the other for the frequency of numbers and powerball numbers
    # determines the 10 least common numbers, ordered by frequency
    
    least_common_numbers = ''
    least_common_pb_numbers = ''
    common_frequency = 100
    common_number = 100
    
     # removes any empty values in the list of powerball frequencies
    for frequency in pb_frequencies:
        if frequency == 0:
            pb_frequencies.remove(0)
            
    # determines the top 10 least common numbers
    for i in range(0, 10):
        
        # if the frequency is less than the current lowest, it is now the lowest
        for frequency in frequencies:
            if frequency < common_frequency:
                common_frequency = frequency
                index = frequencies.index(frequency)
                common_number = labels[index]
                
        # adds the number to the list of least common numbers
        least_common_numbers += str((common_number)) + ' '
        labels.remove((common_number))
        frequencies.remove(common_frequency)
        common_frequency = 100
        common_number = 100
    
    # determines the top 10 least common powerball numbers
    for i in range(0, 10):
        
        # if the frequency is less than the current lowest, it is now the lowest
        for frequency in pb_frequencies:
            if frequency < common_frequency:
                common_frequency = frequency
                index = pb_frequencies.index(frequency)
                common_number = pb_labels[index]
                
        # adds the number to the list of least common numbers
        least_common_pb_numbers += str((common_number)) + ' '
        pb_labels.remove((common_number))
        pb_frequencies.remove(common_frequency)
        common_frequency = 100
        common_number = 100
        
    # outputs the most commonly occuring numbers and powerball numbers
    print()
    print('The least commonly occuring numbers are:', least_common_numbers)
    print('The least commonly occuring powerball numbers are:', least_common_pb_numbers)
    
# ---------------------------------------------------------------------

def gas_prices_main(): # Exercise 14
    # gas_prices_main accepts no arguments
    # runs all the necessary functions
    
    dates, prices, both = gas_prices_list()
    
    high_to_low(dates, prices)

    dates, prices, both = gas_prices_list()
    
    low_to_high(dates, prices)
    
    dates, prices, both = gas_prices_list()
    
    avg_price(dates, prices)
    
    dates, prices, both = gas_prices_list()
    
    highest_and_lowest(dates, prices, both)
    
def gas_prices_list():
    # gas_prices_list accepts no arguments
    # reads the file and assigns the dates and prices to separate lists
    # returns the lists
    
    dates = []
    prices = []
    both = []
    
    # opens and reads the file
    gas_file = open('GasPrices.txt', 'r')
    line = gas_file.readline()
    
    # loops to read each line in the file
    while line != '':

        # strips the newline
        line = line.strip('\n')
        
        # assigns each date and price to their own list
        dates.append(line[:10])
        prices.append(line[11:])
        both.append(str(line))
        
        # reads the next line in the file
        line = gas_file.readline()

    # closes the file
    gas_file.close()
    
    
    # returns the lists
    return dates, prices, both

def low_to_high(dates, prices):
    # low_to_high accepts a list of dates and a list of gas prices for those dates
    # generates a text file that lists the dates and prices,
    # sorted by the lowest price to the highest price

    # generates a new file
    sort_file = open('low_to_high.txt', 'w')

    length = len(prices)
    
    current_price = 1000
    current_date = 1000
    
    # sorts the prices by low to highest value
    for i in range(0, length):

        # if the price is less than the current lowest, it is now the lowest
        for price in prices:
            if float(price) < float(current_price):
                current_price = price
                index = prices.index(price)
                current_date = dates[index]
                
        # adds the date and price to the file
        sort_file.write(str(current_date) + ':' + str(current_price) + '\n')
        dates.remove((current_date))
        prices.remove(current_price)
        current_price = 1000
        current_date = 1000
        

def high_to_low(dates, prices):
    # high_to_low accepts a list of dates and a list of gas prices for those dates
    # generates a text file that lists the dates and prices,
    # sorted by the highest price to the lowest price

    # generates a new file
    sort_file = open('high_to_low.txt', 'w')

    length = len(prices)
    current_price = 0
    current_date = 0
    
    # sorts the prices by highest to lowest value
    for i in range(0, length):
    
        # if the price is more than the current highest, it is now the highest
        for price in prices:
            
            if float(price) > float(current_price):
                current_price = price
                index = prices.index(price)
                current_date = dates[index]
                
        # adds the date and price to the file
        sort_file.write(str(current_date) + ':' + str(current_price) + '\n')
        dates.remove((current_date))
        prices.remove(current_price)
        current_price = 0
        current_date = 0
        
def avg_price(dates, prices):
    # calculates the average price per year for each year in the file
    # avg_price accepts a list of dates and a list of gas prices for those dates
    
    years = []
    total = 0
    dividend = 0
    index = 0
    
    print('Average price per year:')
    print()
    
    # adds each year to a list of all the years
    for date in dates:
        year = date[6:10]
        years.append(year)
       
    current_year = '1993'
    
    # goes through each year in the file
    for year in years:
        
        # ends the function if it is the last entry in the list
        if index == len(prices) - 1:
            
            # output the average per year
            average = total / dividend
            average = format(average, '.2f')
            print(str(current_year) + ': $' + str(average))
            
            # resets the current year, total, and dividend
            current_year = int(current_year) + 1
            total = 0
            dividend = 0
            
            return False
        
        else:
            index += 1
        
        # if the year matches the current year it is calculating the average of
        if year == str(current_year):
            # adds that price to the average and increases the dividend by 1
            total += float(prices[index])
            dividend += 1
            
        # if it has reached a new year
        else:
            # output the average per year
            average = total / dividend
            average = format(average, '.2f')
            print(str(current_year) + ': $' + str(average))
            
            # resets the current year, total, and dividend
            current_year = int(current_year) + 1
            total = 0
            dividend = 0
            
def highest_and_lowest(dates, prices, both):
    # highest_and_lowest accepts a list of years, dates, and a list of gas prices for those years
    # determines the date and amount for the lowest to the highest price of each year
    
    current_year = '1993'
    highest_date = 0
    
    # outputs header
    print()
    print('Highest and Lowest Prices per year:')
    
    # for each year
    for current_year in range(1993, 2014):
        
        current_year = str(current_year)
        lowest_price = 1000
        highest_price = 0
        sort = []
        
        # adds each date in the current year to the list of items to sort
        for item in both:
            if item[6:10] == current_year:
                sort.append(item)
                
        # finds out the highest and lowest values per year
        for item in sort:
                 
            # if the price is less than the current lowest, it is now the lowest
            if float(item[11:]) < float(lowest_price):
                lowest_price = float(item[11:])
                index = sort.index(item)
                lowest_date = item
                    
            # if the price is more than the current highest, it is now the highest
            if float(item[11:]) > float(highest_price):
                highest_price = float(item[11:])
                index = sort.index(item)
                highest_date = item
                    
        # outputs
        print('The lowest for', current_year, 'was', lowest_date, 'and the highest was', highest_date)
        