
#ask user
name = input("Give me your name: ")
age = int(input("Give me your age:"))
copy = (input("How many copies"))


#calc age100_year 
age100_year= str(((100 - age) + 2020))

#print hello name you will turn 100 in year age100_year
#printing out that of prev mess per copy
i=0
while i < int(copy):
    print("\nhello " + name + ", you will turn 100 in year" + age100_year)
    i=i+1
