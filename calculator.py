#PICKIG TWO NUMBERS FROM THE USER AND THEN STORING THEM INTO A VARIABLE
# THEN CALCULATE AND PRINT ON THE SCREEN.

Numb_1 = input("enter the first number: ")
Numb_2 = input("enter the second number: ")
result = int(Numb_1) + int(Numb_2)   #int converts the inputs into numbers since python defines them as strings by default.
print(result)    #so this gives the addition other than concatenation.

name= input('my name is: ')
print('hello '  + name + '!')
