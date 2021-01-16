#allows us to check multiple coditions
age = 20
if(age>18):
    print("enter cinema")
elif(age==18):
    print("enter church")
else:
    print("go home")
print("move on")   #this will be printed out regardless the condition is met or not


#The number_group function should return "Positive" if the number received is positive, "Negative" if it's negative, and "Zero" if it's 0
def number_group(number):
  if number>0:
    return "Positive"
  elif number<0:
    return "Negative"
  else:
    return "Zero"
print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

