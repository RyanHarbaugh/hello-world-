num = int(input("hi user, please provide number"))
num2 = int(input("...and a second...:)"))

#test number for even/odd, print message depending
if num % 2==0:
    print("your number is even")
else:
    print("your number is odd") 

if num % num2 == 0:
    print("your numbers divide evenly")
else:
    print("your numbers dont divide :(")

#test multiple of 4
if num % 4 == 0:
    print("your number is a multiple of four!!")

