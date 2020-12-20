
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#returns a list that contains only the elements that are common between the lists 
# (without duplicates). 
# Make sure your program works on two lists of different sizes.



common = [x for x in a if x in b ]
unique_results = []

for element in common:
    if element not in unique_results:
        unique_results.append(element)

print(unique_results)

