#practise python excercise#25
#In a previous exercise, we’ve written a program that 
# “knows” a number and asks a user to guess it.

#This time, we’re going to do exactly the opposite. 
# You, the user, will have in your head a number between 0 and 100. 
# The program will guess a number, and you, the user, 
# will say whether it is too high, too low, or your number.
#At the end of this exchange, your program should print out 
# how many guesses it took to get your number.


start_index = 1

end_index = 100
guess_check = ""
count = 0

print("Guessing game beginning!  Think of your number between 1 and 100, user!")
print("Type H, for too high...type L, for too low...type Y, for the correct number!")

while guess_check !='y':
    count+=1

    middle_index = (end_index + start_index)//2
    print(middle_index)

    guess_check = input("my guess is %s.  Did I get it right? H, L, Y?"%(middle_index))
    
    if guess_check == "y":
        print("great! I won!, took me %s"%(count))

    if guess_check == "h":
        end_index = middle_index

    if guess_check == 'l':
        start_index = middle_index
    
    
    





