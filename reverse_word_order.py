#practise python exercise 15

#input - user - long string containing multiple words

    
#calc - split string into list teststring.split


#calc - reverse order of list 


#calc - create new string to print or print list in reverse?


#output - user_input_string in reverse order


def reverseWord(w):
  return ' '.join(w.split()[::-1])

test = input("Enter words")
print(reverseWord(test))



