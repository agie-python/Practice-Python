b = open('ttried.txt', 'r') #reads this file and copys
a = open('function.txt', 'w') #data from b is written into this file
for line in b:
    a.write(line)
