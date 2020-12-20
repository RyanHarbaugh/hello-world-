a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]

#write a program that returns a list that contains only the 
# elements that are common between the lists (without duplicates). 

#similarList = [x for x in a + b if x not in a or x not in b]

#print(similarList)
#if not similarList:
#    print("List a and b or equal")
#else:
#    print("List a and b are not equal")

for num in a:
    if num in b:
        if num not in c:
            c.append(num)

print(c)
