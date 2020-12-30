#python practise exercise #16

import random
import string


import time
from random import choice

start_time = time.time()

def createPassword():
    password = ""
    while True:
        answer = int(input("Press #1 to Select Difficult Password, #2 for Easy Password: "))
        if answer == 1:
            # Difficult Password
            allchar = string.ascii_letters + string.punctuation + string.digits
            password = "".join(choice(allchar) for x in range(12))
            break
        elif answer == 2:
            # Easy Password
            allchar = string.ascii_letters + string.digits
            password = "".join(choice(allchar) for i in range(8))
            break
    print(password)

createPassword()
print("--- %s run-time code in seconds ---" % round((time.time() - start_time),2))



#def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
#    return ''.join(random.choice(chars) for _ in range(size))

#print(pw_gen(int(input('How many char'))))



#s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

#passlen = 8
#p = "".join(random.sample(s, passlen))
#print(p)
