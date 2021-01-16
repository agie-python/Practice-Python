#calculating relative energy.
a = open('MP2_singlet.txt', 'r').readlines()
print (a)
for i in a:
    b = -309.1511968016
    d = (float(i) - 2*b) * 627.509
    print (d)
