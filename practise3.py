a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#prints out all the elements of the list that are less than 5
for i in a:
    if i < 5:
        print(i)
    
#Instead of printing the elements one by one, make a new list that has all 
# the elements less than 5 from this list in it and print out this new list
#Write this in one line of Python

for i in a:
    if i > 5:
        a.remove(i)
print(a)

print([aa for aa in a if aa < 5])


#Ask the user for a number and 
# return a list that contains only elements from the original list  
# that are smaller than that number given by the user.

