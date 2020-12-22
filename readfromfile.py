#practise problem - read from file
#Given a .txt file that has a list of a bunch of names, 
# count how many of each name there are in the file, 
# and print out the results to the screen



#with open("testdata.txt") as names:
#    test = {}
#    line = names.read()
#    for name in line.split('\n'):
#        if name in test:
#            test[name] +=1
 #       else:
  #          test[name] = 1

#    while line:
#        line = line.strip()
#        if line in names:
#            names[line] += 1
#        else:
#            names[line] = 1
#        line = b.readline()

#counter_dict = {}
#with open('testdata.txt') as f:
#	line = f.readline()
#	while line:
#		line = line.strip()
#		if line in counter_dict:
#			counter_dict[line] += 1
#		else:
#			counter_dict[line] = 1
#		line = f.readline()

#print(counter_dict)

names = {}

def upsertNames(line):
    global names
    if line in names.keys(): 
        names.update({line : names.get(line) + 1})
    else:
        names.update({line:1})

if __name__ == "__main__":
    open_file = open('testdata.txt', 'r')
    lines = open_file.readlines()
    for line in lines:
        upsertNames(str(line).rstrip())

    print(names)
    open_file.close() 




