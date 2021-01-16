#creating a tuple

coordinates = (4, 5)
#coordinates[1] = 10    #we can access elements in the tuple but we cant change elements because tuples are immutable.
print(coordinates[1])

#DIFFERENCE BTN TUPLES AND LISTS.
#Tuples are usually used for elements that wont usually change like the coordinates
coordinates = [(4, 5), (6,7), (3,9)]
print(coordinates)


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)