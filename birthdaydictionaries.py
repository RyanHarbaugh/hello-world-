#practise python problem
#keep track of when our friend’s birthdays are, 
# and be able to find that information based on their name. 
# Create a dictionary (in your file) of names and birthdays. 
# When you run your program it should ask the user to enter a name, 
# and return the birthday of that person back to them.

if __name__ == "__main__":

    birthday_dictionary = {
        "Albert Einstein": "3/14/1879",
        "Benjamin Franklin": "1/17/1706", 
        "Ada Lovelace": "12/10/1815"}

    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for name in birthday_dictionary:
        print(name)
    
    print("Who's birthday do you want to look up?")
    name = input()
    if name in birthday_dictionary:
        print("{}\'s birthday is {}.".format(name, birthday_dictionary[name]))
    else:
        print('saldy, we don\'t have {}\'s birthday.'.format(name))
    



#def findBirthday(find, birthday_dictionary):
 #   if find in birthday_dictionary:
  #      return birthday_dictionary[find]
   # else:
    #    print("Sorry, our dictionary is missing that one!")



    
    #print(birthday_dictionary.keys())
    #find = print(input("please provide name :"))
    #print(findBirthday(find))


