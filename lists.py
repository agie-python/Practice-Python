#creating a list
friends = ["jesus" ,"grace", "God", "Ivan", "mary", "jim"]

print(friends)     #printing information in the list but with the actual list

#printing a specific element inside the list, using index

print(friends[1])
print(friends[-1])    #accessing elements from back of the list.
print(friends[1:])     #prints all elements after index one.

#selecting a range.
print(friends[1:3])   #prints those from one  but doesnt give 3

friends[2]="Agnes"     #modifying values inside python list.

print(friends[2])

#LIST FUNCTIONS
numbers = [4, 6, 8, 10]

friends.extend(numbers)  #appending two lists together
#print(friends)    #so friend includes the list of numbers too


#Adding individual elements onto a list.
#Adding another name onto a list of friends.
friends.append("Jean")   #Append function adds the new element at the end of the list.
print(friends)

#Adding an element in the middle or at a certain index of the list.
friends.insert(2,"great") #the insert function carries two pieces, the index to
# replace and the character you want to replce
print(friends)

#removing a particular elements from the list
friends.remove("Jean")
print(friends)

#removing all the elements from the list.
#friends.clear()
#print(friends)   #it gives an empty list

#checking if a certain element is in the list.
print(friends.index("jesus")) #it gives the index of that particular element.


friends.append("jesus")
print(friends)

#counting the number of similar elements in the list.
print(friends.count("jesus"))

#sorting elements in the list
friends.sort()   #by default it sorts in alphabetical order.
print(friends)

numbers.sort()
print(numbers)

numbers.reverse()    #sorting in descending order
print(numbers)

#COPYINF A LIST
friends2= friends.copy()
print(friends2)




















