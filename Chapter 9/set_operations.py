
def set_operations():
    
    # sets
    softball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
    basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
    
    # softball
    print('The following students are on the softball team:')
    for person in softball:
        print(person)

    # basketball
    print()
    print('The following students are on the basketball team:')
    for person in basketball:
        print(person)
        
    # baseball and basketball
    print()
    print('The following students play both softball AND basketball:')
    both = softball & basketball
    for person in both:
        print(person)
        
    # baseball or basketball
    print()
    print('The following students play either softball OR basketball:')
    orr = softball | basketball
    for person in orr:
        print(person)
        
    # softball but not basketball
    print()
    print('The following students play softball, BUT NOT basketball:')
    softballbutnot = softball - basketball
    for person in softballbutnot:
        print(person)
        
    # play basketball but not softball
    print()
    print('The following students play basketball, BUT NOT softball:')
    basketballbutnot = basketball - softball
    for person in basketballbutnot:
        print(person)
        
    # play one sport, but not both
    print()
    print('The following students play one sport, but not both:')
    onesport = softball ^ basketball
    for person in onesport:
        print(person)