
def main():
    
    ceasar_message = encryption()
    
    decryption(ceasar_message)
    
def encryption():
    # encryption accepts no arguments
    # takes in a string
    # returns the encrypted string
    
    reversed_message = ''
    ceasar_message = ''
    
    UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # asks user to enter a string input
    message = input('Please enter a string input to be decrypted: ')
    
    # reverse cypher phase
    while message != '':
        
        reversed_message += message[-1]
        message = message[:-1]
        
    # ceasar cypher phase
    # rotates the letters of the reversed string by 10 positions
    for character in reversed_message:
        
        if character in UPPER:
            index = UPPER.index(character)
            ceasar_message += UPPER[index + 10]
        
        if character in LOWER:
            index = LOWER.index(character)
            ceasar_message += LOWER[index + 10]
    
    print(ceasar_message)
    return ceasar_message
    
def decryption(ceasar_message):
    
    decrypted_ceasar = ''
    decrypted_reverse = ''
    
    UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for character in ceasar_message:
        
        if character in UPPER:
            index = UPPER.index(character)
            decrypted_ceasar += UPPER[index - 10]
        
        if character in LOWER:
            index = LOWER.index(character)
            decrypted_ceasar += LOWER[index - 10]
            
    # reverse cypher phase
    while decrypted_ceasar != '':
        
        decrypted_reverse += decrypted_ceasar[-1]
        decrypted_ceasar = decrypted_ceasar[:-1]
    
    print(decrypted_reverse)