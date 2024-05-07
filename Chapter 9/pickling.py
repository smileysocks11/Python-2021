import pickle

def write_main():
    
    again = 'y'
    
    outfile = open('info.dat', 'wb')
    
    while again.lower() == 'y':
        save_data(outfile)
        
        again = input('Enter more data: (y/n): ')
        
    outfile.close()
    
def read_main():
    
    end_of_file = False
    
    infile = open('info.dat', 'rb')
    
    while not end_of_file:
        try:
            person = pickle.load(infile)
            display_data(person)
        except EOFError:
            end_of_file = True
            
    infile.close()
    
def display_data():
    
    print('Name: ', person['name'])
    print('Age: ', person['age'])
    print('Weight: ', person['weight'])
    print()
    
def save_data(file):
    
    person = {}
    
    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = float(input('Weight: '))
    
    pickle.dump(person, file)