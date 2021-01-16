#program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))

#Write a Python program to check a triangle is equilateral, isosceles or scalene. Go to the editor
#An equilateral triangle is a triangle in which all three sides are equal.
#A scalene triangle is a triangle that has three unequal sides.
#An isosceles triangle is a triangle with (at least) two equal sides.
#Expected Output:


x= input("x= ")
y= input("y= ")
z= input("z= ")
if(x==y==z):
    print("equilateral triangle")
elif x==y or y==z or z==x:   #using the logic operators.
    print("Isosceles triangle")
else:
    print("Scarlet triangle")