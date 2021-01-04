#practise python excercise18
#Randomly gen 4 dig num
#ask user to guess
#for every digit user guess correctly && 
# in correct location - they get a  cow
# For every digit guess correctly, but in wrong
# position they get bull
#track total guesses

import random 

number = str(random.randint(1000, 9999))
cow = 0
guesses = 1

def calculate_cows_and_bulls(guess_number):
    cows = 0
    bulls = 0
    for i in range(0,4):
        if guess_number[i] == number[i]:
            cows += 1
        elif guess_number[i] in number:
            bulls +=1
    return cows, bulls

if __name__ == "__main__":
    while cow < 4:
        user_number = input("guess 4 digit number: ")
        cow, bull = calculate_cows_and_bulls(user_number)
        print("cows: ", cow)
        print("bulls: ", bull)
        print("correct num", number)
        if cow == 4:
            print("Congo-rats! you guess the correct number = ", number, "in", guesses, "guesses!")
        else:
            guesses += 1

         











