def rock_paper_scissors():
    
    from time import sleep
    import random
    
    print('Rock')
    sleep(1)
    print('Paper')
    sleep(1)
    print('Scissors')
    sleep(1)
    print('sHOot')
    
    print('')
    choice = input('Enter your choice here: ')
    
    options = ['rock', 'paper', 'scissors']
    
    computer_choice = (random.choice(options)).lower()
    print('')
    print('The computer chose', computer_choice)
    print('You chose', choice)
    
    print('')
    
    if choice == 'rock' and computer_choice == 'rock':
        print('The round ended in a tie.')
        
    elif choice == 'scissors' and computer_choice == 'scissors':
        print('The round ended in a tie.')
        
    elif choice == 'paper' and computer_choice == 'paper':
        print('The round ended in a tie.')
        
    elif choice == 'rock' and computer_choice == 'paper':
        print('Rock beats Paper. You win this round.')
        
    elif choice == 'rock' and computer_choice == 'scissors':
        print('Scissors beats Rock. You lost this round.')
        
    elif choice == 'paper' and computer_choice == 'scissors':
        print('Scissors beats Paper. You lost this round.')
        
    elif choice == 'paper' and computer_choice == 'rock':
        print('Paper beats Rock. You won this round.')
        
    elif choice == 'scissors' and computer_choice == 'rock':
        print('Rock beats Scissors. You lost this round.')
        
    elif choice == 'scissors' and computer_choice == 'paper':
        print('Scissors beats paper. You won this round.')