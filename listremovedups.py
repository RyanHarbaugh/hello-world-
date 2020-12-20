#exercise 14, list remove duplicates 
#Write a program (function!) that takes a list and returns a new list that 
# contains all the elements of the first list minus all the duplicates.
#Write two different functions to do this - one using a loop and constructing a list, and another using sets.


#for loop it
def convertToUnique(x):
    unique = []
    [unique.append(num) for num in x if num not in unique]
    return [unique]

#set it up
def convertToUniqueSet(x):
    return list(set(x))


a = [1, 1, 2, 3, 4, 4, 5]
print(convertToUnique(a))
#print(a)

print(convertToUniqueSet(a))



