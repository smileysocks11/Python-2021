def rectangle_pattern():
    
    rows = int(input('Enter the number of rows to print: '))
    columns = int(input('Enter the number of columns to print: '))
    print()
    
    for row in range(1, rows + 1):
        
        for column in range(1, columns + 1):
            
            print('*', end='')
            
        print()
        
rectangle_pattern() # auto starts program