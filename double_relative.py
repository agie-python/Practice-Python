#calculating relative energy.
a = open('double_trip.txt', 'r').readlines()
print (a)
for i in a:
    b = -619.4274001913
    d = (float(i) - 2*b) * 627.509
    print (d)
