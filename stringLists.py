#ask use for string

#check string for palindrome (reads same forw/back)

def reverse(word):
    x=''
    for i in range(len(word)):
        x += word[len(word)-1-i]
    return x

word = input('give me a word: \n')
x = reverse(word)

if x == word:
    print("This is a palindrom")
else:
    print("This is NOT a palindrome")
    