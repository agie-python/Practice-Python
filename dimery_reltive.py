#calculating relative energy.
a = open('double_tripp.txt', 'r').readlines()
print (a)
for i in a:
    b = -619.4966645683
    d = (float(i) - 2*b) * 627.509
    print (d)