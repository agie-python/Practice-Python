#reading data from a external file
with open('data.txt', 'r') as file1:
    a = file1.readline()
    print(a)
    #result = sum(map(int, f))