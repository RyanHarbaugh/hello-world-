#practise python exercise 9
import random
attempt_counter = 0

#generate random number between 1 and 9//including 1 and 9
correct_num = random.randint(1, 9)

#ask user to guess
stop = input("Guess a number between 1 and 9, type q to exit :")

#Check guess - 
while True:
    if stop == 'q':
        print("Killing game, good bye")
        break
    try:
        guess = int(stop)
        attempt_counter += 1
        if guess >9 or guess <1:
            print("outside of scope! try again!")
        elif guess < correct_num and guess >0:
            print("Nope! Wrong! Try a higher number! ")
        elif guess > correct_num and guess <=9: 
            print("Nope! Wrong! Try a lower number! ")
    except:
        stop = input("invalid input, guess again, a number 1 -9! ")
        continue
    if guess == correct_num:
        attempt_counter = str(attempt_counter)
        print("Congro-rats you found it after" + attempt_counter + " attempts")
        break
    stop = input("Guess again ")




    
    
   

#continue game untill user types "exit"

#Track # guesses, print out on game end


