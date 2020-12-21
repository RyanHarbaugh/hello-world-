
#take ordered list of numbers
#user input test number - test against list
#output boolean
#bonus use binary search

def element_search(data, test_case):
    if test_case in data:
        return True
    else:
        return False

    #for element in data:
    #    if element == test_case:
    #        return True
    #    else:
    #        return False

           
            






test_case = int(input("Please provide number: "))

data = [ 1, 2, 5, 7, 9, 11]

print(element_search(data, test_case))
