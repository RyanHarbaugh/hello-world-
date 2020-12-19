num = int(input("Please provide a whole number :"))

#prints out a list of all the divisors of that number

listRange = list(range(1, num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
