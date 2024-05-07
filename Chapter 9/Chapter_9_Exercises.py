import pickle
import random
# ---------------------------------------------------------------------

def encryption(): # Exercise 3
    # encryption accepts no arguments
    # uses a dictionary to assign 'codes' to each letter of the alphabet
    
    codes = {'A' : '~', 'a' : 'Ñ',
             'B' : '!', 'b' : '1',
             'C' : '@', 'c' : '2',
             'D' : '#', 'd' : '3',
             'E' : '$', 'e' : '4',
             'F' : '%', 'f' : '5',
             'G' : '^', 'g' : '6',
             'H' : '&', 'h' : '7',
             'I' : '*', 'i' : '8',
             'J' : '(', 'j' : '9',
             'K' : ')', 'k' : '0',
             'L' : '_', 'l' : '-',
             'M' : '+', 'm' : '=',
             'N' : '{', 'n' : '[',
             'O' : '}', 'o' : ']',
             'P' : ':', 'p' : ';',
             'Q' : '<', 'q' : ',',
             'R' : '>', 'r' : '.',
             'S' : '?', 's' : '/',
             'T' : '»', 't' : '≥',
             'U' : 'í', 'u' : '◘',
             'V' : '◙', 'v' : '└',
             'W' : '«', 'w' : '☼',
             'X' : '♥', 'x' : '',
             'Y' : '¿', 'y' : '⌡',
             'Z' : '÷', 'z' : '£' }
    
    message = ''
    
    # opens and reads the file
    encrypt_file = open('encrypt.txt', 'r')
    line = encrypt_file.readline()
    
    # loops to read each line in the file
    while line != '':
        
        # adds the corresponding character for each letter to the string message
        for letter in line:
            if letter != ' ':
                
                message += str(codes[letter])
                
        # reads new line
        line = encrypt_file.readline()
    
    # adds the encrypted message to a new file
    decrypt_file = open('decrypt.txt', 'wb')
    pickle.dump(message, decrypt_file)
    
    # closes files
    encrypt_file.close()
    decrypt_file.close()
    

def decryption():
    # decryption accepts no arguments
    # opens an encrypted file
    # displays its decrypted contents
    
    end_of_file = False
    message = ''
    
    codes = {'~' : 'A', 'Ñ' : 'a',
             '!' : 'B', '1' : 'b',
             '@' : 'C', '2' : 'c',
             '#' : 'D', '3' : 'd',
             '$' : 'E', '4' : 'e',
             '%' : 'F', '5' : 'f',
             '^' : 'G', '6' : 'g',
             '&' : 'H', '7' : 'h',
             '*' : 'I', '8' : 'i',
             '(' : 'J', '9' : 'j',
             ')' : 'K', '0' : 'k',
             '_' : 'L', '-' : 'l',
             '+' : 'M', '=' : 'm',
             '{' : 'N', '[' : 'n',
             '}' : 'O', ']' : 'o',
             ':' : 'P', ';' : 'p',
             '<' : 'Q', ',' : 'q',
             '>' : 'R', '.' : 'r',
             '?' : 'S', '/' : 's',
             '»' : 'T', '≥' : 't',
             'í' : 'U', '◘' : 'u',
             '◙' : 'V', '└' : 'v',
             '«' : 'W', '☼' : 'w',
             '♥' : 'X', '' : 'x',
             '¿' : 'Y', '⌡' : 'y',
             '÷' : 'Z', '£' : 'z' }
    
    # opens and reads file
    decrypt_file = open('decrypt.txt', 'rb')
    
    # loop to the end of the file
    while not end_of_file:
        try:
            # unpickles and displays next object
            line = pickle.load(decrypt_file)
            
            # converts each character to their corresponding letter
            for character in line:
                message += str(codes.get(character))
                
        except EOFError:
             # end of file error reached, change the loop flag
             end_of_file = True
    
    # displays decrypted contents
    print(message)
    
    # closes file
    decrypt_file.close()
    
# ---------------------------------------------------------------------

def unique_words(): # Exercise 4
    # unique_words accepts no arguments
    # opens any text file
    # displays a list of all unique words found in the file
    
    words = set([])
    word = ''
    string = ''
    
    # opens and reads file
    word_file = open('unique_words.txt', 'r')
    line = word_file.read()
        
    # converts file to string
    string += line
    
    # loops through the string
    for ch in string:
        
        # if a word is found, it adds it to the set
        if ch == ' ' or ch == '\n':
            words.add(word)
            word = ''
              
        # if not, the character is added to the word
        else:
            word += ch
    
    # displays each unique word in the set
    for item in words:
        print(item)
        
# ---------------------------------------------------------------------

def blackjack(): # Exercise 9
    # blackjack accepts no arguments
    # simulates a simplified version of Blackjack between two virtual players
    
    # generates the deck used for the game
    deck = create_deck()
    
    # simulates the game by dealing each round
    deal_cards(deck)
    
def create_deck():
    # create_deck accepts no arguments
    # creates a dictionary that includes all the cards of a deck and their values
    
    # creates deck
    deck = {'Ace of Spades' : 11, '2 of Spades' : 2, '3 of Spades' : 3,
        '4 of Spades' : 4, '5 of Spades' : 5, '6 of Spades' : 6,
        '7 of Spades' : 7, '8 of Spades' : 8, '9 of Spades' : 9,
        '10 of Spades' : 10, 'Jack of Spades' : 10, 'Queen of Spades' : 10,
        'King of Spades' : 10,
        
        'Ace of Hearts' : 11, '2 of Hearts' : 2, '3 of Hearts' : 3,
        '4 of Hearts' : 4, '5 of Hearts' : 5, '6 of Hearts' : 6,
        '7 of Hearts' : 7, '8 of Hearts' : 8, '9 of Hearts' : 9,
        '10 of Hearts' : 10, 'Jack of Hearts' : 10, 'Queen of Hearts' : 10,
        'King of Hearts' : 10,
        
        'Ace of Clubs' : 11, '2 of Clubs' : 2, '3 of Clubs' : 3,
        '4 of Clubs' : 4, '5 of Clubs' : 5, '6 of Clubs' : 6,
        '7 of Clubs' : 7, '8 of Clubs' : 8, '9 of Clubs' : 9,
        '10 of Clubs' : 10, 'Jack of Clubs' : 10, 'Queen of Clubs' : 10,
        'King of Clubs' : 10,
        
        'Ace of Diamonds' : 11, '2 of Diamonds' : 2, '3 of Diamonds' : 3,
        '4 of Diamonds' : 4, '5 of Diamonds' : 5, '6 of Diamonds' : 6,
        '7 of Diamonds' : 7, '8 of Diamonds' : 8, '9 of Diamonds' : 9,
        '10 of Diamonds' : 10, 'Jack of Diamonds' : 10, 'Queen of Diamonds' : 10,
        'King of Diamonds' : 10}
    
    # returns the deck dictionary
    return deck

def deal_cards(deck):
    # deal_cards accepts a dictionary deck
    # deals cards to each player until one player's hand is worth more than 21 points
    # when that happens, the other player is the winner
    # game repeats until all cards have been dealt from the deck
    
    winner1 = 0
    winner2 = 0
    game = 0
    
    # game repeats until all cards have been dealt
    while len(deck) != 0:
        
        hand1 = 0
        hand2 = 0
        game += 1
        
        # loops until one player's hand is greater than 21
        while hand1 <= 21 and hand2 <= 21 and len(deck) != 0:
            
            # deals each player a card from the deck and removes it from the deck
            card1 = random.choice(list(deck))
            value1 = deck.pop(card1)
            card2 = random.choice(list(deck))
            value2 = deck.pop(card2)
            
            # and adds cards to each hand value
            hand1 += value1
            hand2 += value2
            
            # if player 1's hand exceeds 21 because of an ace it turns the value into a 1
            if value1 == 11:
                if hand1 > 21:
                    hand1 -= 10
                    
            # if player 2's hand exceeds 21 because of an ace it turns the value into a 1
            if value2 == 11:
                if hand2 > 21:
                    hand2 -= 10
        
        # if one player's hand exceeds 21
        if hand1 > 21 or hand2 > 21:
            
            # adds a point to a player's score depending on the winner
            if hand1 > hand2:
                winner2 += 1
            else:
                winner1 += 1
            
            # outputs the final hands of both players
            print('Round', game, 'final hands:')
            print('Player 1:', hand1)
            print('Player 2:', hand2)
            print()
            
    # determines the winner and displays a winning message
    if winner1 > winner2:
        print('The winner of the game is Player 1 with', winner1, 'rounds won.')
    
    if winner1 < winner2:
        print('The winner of the game is Player 2 with', winner2, 'rounds won.')
        
    elif winner1 == winner2:
        print('The game resulted in a tie with both players winning', winner1, 'rounds.')
