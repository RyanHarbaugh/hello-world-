#practise python problem
#Implement a function that takes as input three variables, 
# and returns the largest of the three. 
# Do this without using the Python max() function!

def findlargestnum(test1, test2, test3):
    if test1 > test2:
        if test1 > test3:
            return test1
    elif test2 > test1: 
        if test2 > test3:
            return test2
        else: 
            return test3

if __name__ == "__main__":
   print(str(findlargestnum(5,2,3)))
