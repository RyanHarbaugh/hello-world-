#practise python problem
# Create a dictionary (in your file) of names and birthdays. 
# When you run your program it should ask the user to enter a name, 
# and return the birthday of that person back to them.
#exercise#34 -pull dictionary from JSON file

import json

birthday_dictionary = {}
with open("bdays.json", 'r') as f:
        birthday_dictionary = json.load(f)

def add_entry():
    name = input('who do you want to add to the bday dictionary?\n').title()
    date = input('When is {} born? DD/MM/YYYY Format Please!'.format(name))
    birthday_dictionary[name] = date
    with open('bdays.json', 'w') as f:
        json.dump(birthday_dictionary, f)
    print('{} was added to the birthday dictionary\n'.format(name))

def find_date():
    print('We have the following entries in the bday dictionary')
    for name in birthday_dictionary:
        print(name)
    
    name = input('Who bday do you want to know?')
    try:
        if birthday_dictionary[name]:
            print('{} bday is {}'.format(name, birthday_dictionary[name]))
    except KeyError:
        print('{} is not in the list'.format(name))

def list_entries():
    print('We have the following entries in the bday dictionary')
    for name in birthday_dictionary:
        print(name)

    
if __name__ == "__main__":


    while True:
        next_task = input('Pick task for the dictionary: add, find, list, quit\n').capitalize()
        if next_task == 'Quit':
            print('Good Bye!')
            raise SystemExit()
        elif next_task == 'Add':
            add_entry()
        elif next_task == 'Find':
            find_date()
        elif next_task == 'List':
            list_entries()
    
 



    

    
    
    
    
    
    
    
    
    
    #print("Welcome to the birthday dictionary. We know the birthdays of:")
    #for name in birthday_dictionary:
    #    print(name)
    
    #print("Who's birthday do you want to look up?")
    #name = input()
    #if name in birthday_dictionary:
    #    print("{}\'s birthday is {}.".format(name, birthday_dictionary[name]))
    #else:
    #    print('saldy, we don\'t have {}\'s birthday.'.format(name))
    



#improrting this info from json file
#    birthday_dictionary = {
#        "Albert Einstein": "3/14/1879",
#        "Benjamin Franklin": "1/17/1706", 
#        "Ada Lovelace": "12/10/1815"}